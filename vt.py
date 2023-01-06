import requests

params = {}
params["domain"] = "google.com"
params["apikey"] = "97effa9293fe867afcff9a79a75b2bfe547cafa222b7bc7bc0cc6bf13d713429"
headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Splunk VirusTotal Technical Addon",
}

url = "https://www.virustotal.com/vtapi/v2/domain/report"

# headers = {
#     "accept": "application/json",
#     "x-apikey": "97effa9293fe867afcff9a79a75b2bfe547cafa222b7bc7bc0cc6bf13d713429"
# }

response = requests.get(url, headers=headers, params=params)

print(response.text)
