from datetime import datetime, timedelta
import requests
import os
import json


#montando url
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"

end_time = datetime.now().strftime(TIMESTAMP_FORMAT)
start_time = (datetime.now() + timedelta(-1)).date().strftime(TIMESTAMP_FORMAT)

print(end_time)
print(start_time)

query = "data science"

tweet_fields = "tweet.fields=author_id, conversation_id, created_at, id, in_reply_to_user_id,public_metrics, lang, text"
user_fields = "expansions=author_id&user.fields=id,name,username,created_at"

url_raw = f"https://labdados.com/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}&start_time={start_time}&end_time={end_time}"

#montando headers
bearer_token = os.environ.get("BEARER_TOKEN")
headers = {"Authorization" : "Bearer {}".format(bearer_token)}
response = requests.request("GET", url_raw, headers=headers)


#imprimir json
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))


#paginate
while "next_token" in json_response.get("meta", {}):
    next_token = json_response['meta']['next_token']
    url = f"{url_raw}&next_token={next_token}"
    response = requests.request("GET", url, headers=headers)
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))



# Admin/Connections
# Add
# Connection Id = twitter_default
# Connection Type = Http
# Host = https://labdados.com
# Extra = {"Authorization": "Bearer XXXXXXXXXXXXXXXXXXXXXX"}