import urllib3, io, boto3

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

def lambda_handler(event, context):
    """Get zip file and upload to S3 bucket

    Args:
        event: Payload obtained from step function input. Expected Input:
                sales_records_url: Url used to fetch zip file from
                bucket: Bucket name where zip file should be uploaded to
                object_key: Name of file that is being uploaded to s3
        context: Object provides methods and properties that provide information about the invocation, function, and execution environment.

    Returns:
        None
    """
    http = urllib3.PoolManager()
    s3 = boto3.client("s3")
    
    response = http.request('GET', event["sales_records_url"], headers=header)
    
    if response.status == 200:
        s3.upload_fileobj(io.BytesIO(response.data), event["bucket"], event["object_key"])
    else: 
        raise Exception("Request not Successful")