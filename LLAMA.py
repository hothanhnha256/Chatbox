import os 
os.environ["REPLICATE_API_TOKEN"]="r8_atBi6V8bfGAyFHxxLbo3qXht74gEAWP0R4JSg"
import replicate

user_prompt = input("Enter your prompt: ")

for event in replicate.stream(
    "meta/llama-2-70b-chat",
    input={
        "top_k": 0,
        "top_p": 1,
        "prompt": user_prompt,
        "temperature": 0.5,
        "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
        "length_penalty": 1,
        "max_new_tokens": 500,
        "min_new_tokens": -1,
        "prompt_template": "<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST]",
        "presence_penalty": 0
    }
):
    print(str(event), end="")