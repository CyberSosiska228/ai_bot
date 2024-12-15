import requests
import json


def send_req(send_param):
    r = requests.post(send_param["url"], headers=send_param["headers"], json=send_param["json"])
    return r

def resp_to_str(resp):
    res = ""
    lst = resp.split(b"\n")

    err = True
    for i in lst:
        ans_part = json.loads(i.decode("ascii"))
        res += ans_part["response"]
        if (ans_part["done"]):
            if (ans_part["done_reason"] == "stop"):
                err = False
            break

    if (err):
        return "Sorry, error occured("
    return res

def ans_quest(send):
    r = send_req(send).content
    ans = resp_to_str(r)
    return ans
