import requests


def send_req(send_param):
    r = requests.post(send_param["url"], headers=send_param["headers"], json=send_param["json"])
    return r


send = {
        "url" : "http://localhost:11434/api/generate",
        "headers" : {"Content-Type" : "applicatioin/json"},
        "json" : {
            "model": "llama3.2:3b",
            "prompt": "Hi"
        }
}

print(str(send_req(send).content))
