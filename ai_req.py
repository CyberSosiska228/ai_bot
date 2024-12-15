import requests
import json


def send_req(send_param):
    r = requests.post(send_param["url"], headers=send_param["headers"], json=send_param["json"])
    return r

def resp_to_str(resp):
    res = ""
    lst = resp.split("\n")

    err = True
    for i in lst:
        ans_part = json.loads(i)
        res += ans_part["response"]
        if (ans_part["done"] and ans_part["done_reason"] == "stop"):
            err = False

    if (err):
        return "Sorry, error occured("
    return res

def ans_quest(send):
    r = send_req(send).content.decode("ascii")
    ans = resp_to_str(r)
    return ans

send = {
        "url" : "http://localhost:11434/api/generate",
        "headers" : {"Content-Type" : "applicatioin/json"},
        "json" : {
            "model": "llama3.2:3b",
            "prompt": "Hi"
        }
}

print(ans_quest(send))
