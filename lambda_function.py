import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = os.environ['BUCKET_NAME']
    file_name = event.get('file_name', 'default.txt')
    file_content = event.get('file_content', 'Hello, S3!')

    try:
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        return {
            'statusCode': 200,
            'body': f'File {file_name} successfully written to {bucket_name}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }