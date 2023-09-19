# from aws_cdk import aws_iam as iam
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subs
from aws_cdk import aws_sqs as sqs
from aws_cdk import Duration
from aws_cdk import Stack
from constructs import Construct


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
