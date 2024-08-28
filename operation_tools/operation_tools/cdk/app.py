from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3,
    aws_dynamodb as dynamodb
)
from constructs import Construct

class LocalTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # example resource
        sqs.Queue(
            self, "TestQueue1",
            queue_name='TestQueue1',
            visibility_timeout=Duration.seconds(300),
        )
        sqs.Queue(
            self, "TestQueue2",
            queue_name='TestQueue2',
            visibility_timeout=Duration.seconds(300),
        )

        dynamodb.Table(self, 
            'UserTable',
            table_name='UserTable',
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.NUMBER
            ),
            sort_key = dynamodb.Attribute(
                name="nickname",
                type=dynamodb.AttributeType.STRING
            ),
        )

        s3.Bucket(self,
            "TestBucket",
            bucket_name='test-bucket',
        )

