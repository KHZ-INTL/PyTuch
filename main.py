import requests
import random
import json
from flask import Flask
from flask import render_template
app = Flask(__name__)


def fetch(item="", page="1"):
    imageurl = 'http://tuchong.com/rest/search/posts?query={}&count=20&page={}'.format(item, page)
    head = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en;q=0.5', 'Connection': 'keep-alive',
            'Cookie': 'webp_enabled=0; log_web_id=5000125721', 'DNT': '1', 'Host': 'tuchong.com', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/4.0 (Windows NT 07.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/53.0'}
    conn = requests.get(imageurl, headers=head)
    cont = conn.json()
    print(conn)
    res = conn.content
    if conn.status_code == "ValueError: No JSON object could be decoded":
        res = conn.content
    else:
        res = conn.json()
    return res


def extractdic(dicIn):
    outDic = []
    response = dicIn
    resp = response["data"]["post_list"]
    print(len(resp))
    # lenvar = len(response["data"]["post_list"])

    for range1 in range(0, len(resp)):
        for k, v in resp[range1].items():
            lenvar2 = (resp[range1]["images"])
            for range2 in range(0, len(lenvar2)):
                # if lenvar2[range2]["width"] > 1000 and lenvar2[range2]["height"] > 1200:
                if lenvar2[range2]["source"]["l"] not in outDic:
                    outDic.append(lenvar2[range2]["source"]["l"])

    return outDic


@app.route('/<searchTerm><page>')
def drawmage(searchTerm, page):
    strm = searchTerm
    pag = page
    searchTerm= fetch(item=searchTerm, page= pag)
    dicout = extractdic(searchTerm)
    return render_template("index.html", imageDict=dicout, sterm = strm)


if __name__ == "__main__":
    app.run(debug=True)

