from flask import Flask, render_template, request
import os
import replicate

os.environ["REPLICATE_API_TOKEN"] = "API_KEY"
# r8_bRL9i7D8bFY8vIX6VxWOwgPXcsIqlgn1ZPWOA
#r8_UcRdBGEv3oPSQL2qGysOccjdZi6VWcM4R4RJy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    response = ""
    for event in replicate.stream(
        "meta/llama-2-70b-chat",
        input={
            "top_k": 0,
            "top_p": 1,
            "prompt": userText,
            "temperature": 0.5,
            "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
            "length_penalty": 1,
            "max_new_tokens": 500,
            "min_new_tokens": -1,
            "prompt_template": "<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST]",
            "presence_penalty": 0
        }
    ):
        response += str(event)
    return "<p style='color: blue; font-size: 18px;'>" + response + "</p>"

if __name__ == "__main__":
    app.run()