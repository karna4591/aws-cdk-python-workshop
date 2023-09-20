from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subs
from aws_cdk import aws_sqs as sqs
from aws_cdk import Duration
from aws_cdk import Stack
from constructs import Construct

# from aws_cdk import aws_iam as iam


class CdkWorkshopStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self,
            'CdkWorkshopQueue',
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self,
            'CdkWorkshopTopic',
        )

        topic.add_subscription(subs.SqsSubscription(queue))

        # Define AWS Lambda resource.
        my_lambda = _lambda.Function(
            self,
            'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )

        print(my_lambda)
