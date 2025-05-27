from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_s3 as s3, # Add the missing imports
   )
from constructs import Construct

class CdkS3BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket with specified name
        bucket = s3.Bucket(self, "demo-cdk-code-catalyst-amarbvn",  # Changed from XXXXXXXXXXXXX to a meaningful ID
            bucket_name="test-bucket-s3-amarbvn",                   # Changed from XXXXXXXXXXXXX to a meaningful name
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,     # Block public access
            encryption=s3.BucketEncryption.S3_MANAGED,              # Enable encryption
            enforce_ssl=True,
            versioned=True,                                         # Enable versioning
            removal_policy=RemovalPolicy.DESTROY,                   # Optional: automatically delete bucket when stack is destroyed
            auto_delete_objects=True
        ) 
