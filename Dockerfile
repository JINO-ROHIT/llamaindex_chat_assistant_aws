FROM public.ecr.aws/lambda/python:3.11

COPY my_lambda_function.py ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV region_name="xxxxxx"
ENV aws_access_key_id="xxxxxxx"
ENV aws_secret_access_key="xxxxxx"

CMD ["my_lambda_function.lambda_handler"]