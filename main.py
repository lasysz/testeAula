import requests

reqUrl= "https://api.github.com/octocat"

hearderList = {
    "Aceppt" : "application/vnd.github+json",
    "User-Agent" : "Thunder Client (https://www.thunderclient.com)",
    "X-Github-Api-Version": "2022=11-18"
}

payload = ""

respobse = requests.requests("GET", reqUrl, data=payload, headers=hearderList)

print(response.text)