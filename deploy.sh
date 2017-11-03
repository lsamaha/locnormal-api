#!/usr/bin/env bash

aws ecs run-task --cluster loc-api-dev --task-definition \
    $(aws ecs register-task-definition --cli-input-json file://ecs-task-def.json | jq -r '.taskDefinition.family') \
    | jq -r '.tasks[0].taskArn'
