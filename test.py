import requests
import json

def fetch(item=""):
    imageurl = 'http://tuchong.com/rest/search/posts?query="{}"&count=20&page=1'.format(item)
    conn = requests.get(imageurl)
    #conjs = conn.json()
    #res = conn.content
    #if conn.status_code == "ValueError: No JSON object could be decoded":
    #    res = conn.content
    #else:
    #    res = conn.json()
    return conn.content


def extractdic(dicIn):
    outDic = []
    jsfile = open("response.json", "r").read()
    response = json.loads(jsfile)
    resp = response["data"]["post_list"]
    # lenvar = len(response["data"]["post_list"])

    for range1 in range(0, len(resp)):
        for k, v in resp[range1].items():
            lenvar2 = (resp[range1]["images"])
            for range2 in range(0, len(lenvar2)):
                if lenvar2[range2]["width"] > 1000 and lenvar2[range2]["height"] > 800:
                    outDic.append(lenvar2[range2]["source"]["l"])
    return outDic

get = fetch("suzuki")
get2 = extractdic(get)



