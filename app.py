#!/usr/bin/env python3

from aws_cdk import core

from pipelines_webinar.pipeline_stack import PipelineStack

PIPELINE_ACCOUNT = '291757279686'
PIPELINE_REGION = 'eu-west-2'

app = core.App()
PipelineStack(app, 'PipelineStack', env={
  'account': PIPELINE_ACCOUNT,
  'region': PIPELINE_REGION,
})

app.synth()
