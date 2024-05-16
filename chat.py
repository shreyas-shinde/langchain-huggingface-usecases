from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.schema import (
    HumanMessage,
    SystemMessage,
)

LLAMA_INSTRUCT = "meta-llama/Meta-Llama-3-8B-Instruct"
HF_ZEPHYR = "HuggingFaceH4/zephyr-7b-beta"

llm = HuggingFaceEndpoint(
    repo_id=LLAMA_INSTRUCT,  # if endpoint_url is used instead we need to also provide the model_id in ChatHuggingFace
    task="text-generation",
    streaming=True,
    max_new_tokens=1024,  # doesn't seem to have any impact on output length
    model="",  # this is a required field so we need to provide it but it doesn't seem to have any impact on output, only repo_id does
    client=None,
    async_client=None,
    return_full_text=True,
    repetition_penalty=1.1,
    cache=False,
    do_sample=False,
)
messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(
        content="What happens when an unstoppable force meets an immovable object?"
    ),
]
chat_model = ChatHuggingFace(llm=llm)
print(chat_model.invoke(messages))

# LLAMA_INSTRUCT:
# Output:
# content="The concept of an unstoppable force meeting an immovable object is a classic thought experiment in physics and philosophy. It's a paradox that challenges our understanding of energy and motion.\n\nFrom a purely physical perspective, the laws of physics suggest that:\n\n* An unstoppable force would have infinite energy, which is impossible according to our current understanding of physics.\n* An immovable object would have infinite mass, which is also physically impossible.\n\nIf we consider the scenario where an unstoppable force meets an immovable object, a few" response_metadata={'token_usage': ChatCompletionOutputUsage(completion_tokens=100, prompt_tokens=32, total_tokens=132), 'model': '', 'finish_reason': 'length'} id='run-b5c9be7e-b66e-415e-9621-32117e801867-0'

# HF_ZEPHYR:
# Output:
# content='The concept of an "unstoppable force" and an "immovable object" is a common philosophical paradox. It proposes a hypothetical situation where an object with limitless strength and power (unstoppable force) encounters an object that cannot be moved (immovable object).\n\nAccording to the principles of logic and physics, when an unstoppable force meets an immovable object, there are a few possible outcomes:\n' response_metadata={'token_usage': ChatCompletionOutputUsage(completion_tokens=100, prompt_tokens=58, total_tokens=158), 'model': '', 'finish_reason': 'length'} id='run-feefba23-59c7-426d-ba7a-63615560cb5b-0'
