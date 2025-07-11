#!/usr/bin/env bash
# enable auto-export
set -o allexport
# load all VAR=VALUE lines from .env
# (ignores blank lines and lines starting with “#”)
source .env
# disable auto-export
set +o allexport

echo $OPENAI_API_KEY
# now every variable in .env is in your environment
CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve $LLM_PATH --served-model-name $LLM_MODEL \
    --dtype auto --api-key $OPENAI_API_KEY  \
    --host 0.0.0.0 --port 26700 --tensor-parallel-size 4