"""
Tests the creation of AWS CDK services.
"""
import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack


# SECTION: TESTS ============================================================ #


def test_sqs_queue_created():
    """
    Tests creating an AWS SQS queue.
    """

    app = core.App()
    stack = CdkWorkshopStack(app, 'cdk-workshop')
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        'AWS::SQS::Queue',
        {
            'VisibilityTimeout': 300,
        },
    )


def test_sns_topic_created():
    """
    Tests creating an AWS SNS topic.
    """

    app = core.App()
    stack = CdkWorkshopStack(app, 'cdk-workshop')
    template = assertions.Template.from_stack(stack)

    template.resource_count_is('AWS::SNS::Topic', 1)
