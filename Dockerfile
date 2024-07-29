FROM public.ecr.aws/lumigo/lumigo-log-collection-extension:19 AS lumigo-log-collecting-extension
FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY lambda_function.py .

COPY --from=lumigo-log-collecting-extension /opt/extensions/log-collector-extension /opt/extensions/log-collector-extension

CMD ["lambda_function.lambda_handler"]