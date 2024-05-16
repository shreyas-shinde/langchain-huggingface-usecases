# langchain-huggingface-usecases

## Pre-requisites
```
python --version
Python 3.12.3
```

## Install requirements in virtualenv
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Export your huggingface token

1. Sign up on hugging face and get token https://huggingface.co/docs/hub/en/security-tokens
2. Export
```
cp .env.template .env
# add your token to .env
source .env
```

## Run
```
python chat.py
```
You can change the model by changing the repo_id parameter
