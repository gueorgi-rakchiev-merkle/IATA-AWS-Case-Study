import awswrangler as wr

def lambda_handler(event, context):
    """Transform zip file into partitioned parquet table

    Args:
        event: Payload obtained from step function input. Expected Input:
                s3_source_url: Where source zip file is found in s3
                s3_dest_url: Where the resulting parquet files should be stored
        context: Object provides methods and properties that provide information about the invocation, function, and execution environment.

    Returns:
        None
    """
    df = wr.s3.read_csv(event["s3_source_url"])
    wr.s3.to_parquet(df=df, path=event["s3_dest_url"], compression='gzip', partition_cols=['Country'], mode='overwrite', dataset=True)
    
    
