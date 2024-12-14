import requests


def send_req(send_param):
    r = requests.get(send_param.url, headers=send_param.headers)


send = {
        "url" : "http://localhost:11434/api/generate"
        "headers" : {
            "model": "llama3.2",
            "prompt": "Why is the sky blue?"
        }
}

send_req(send_param)
