import json
import logging

from llama_index.core.llms import ChatMessage
from llama_index.llms.bedrock import Bedrock

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def chat_assistant(user_query : str) -> str:

    try:
        messages = [
            ChatMessage(
                role = "system", 
                content = "You are a chat assistant to help users with their queries"
            ),
            ChatMessage(role="user", content = user_query),
        ]

        resp = Bedrock(
            model="amazon.titan-text-express-v1", profile_name='xxxx'
        ).chat(messages)

        return resp.message.content
    
    except Exception as e:
        logger.error(f"Unable to answer the query: {e}")
        return ""


def lambda_handler(event, context):
    try:
        event_body = json.loads(event['body'])
        user_query = event_body.get('user_query')

        if not user_query:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid input: user_query is required')
            }

        response = chat_assistant(user_query)

        if response:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': response})
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps('Failed to generate a response')
            }

    except Exception as e:
        logger.error(f"Exception in lambda_handler: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Internal server error: {e}')
        }

    



