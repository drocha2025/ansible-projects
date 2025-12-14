import requests
from getpass import getpass

pat = getpass("Personal Access Token: ") or "MjJkN2JjNDUtM2M0Mi00Mzc4LTk1NDMtNTI4Zjc5MjFhZjBmNjk1MTdmNTctZmUw_P0A1_ba774546-71bb-4b52-9725-a7e2c4a6fc52"

to = input("Recipient email address: ") or "MyBot2026@webex.bot"

message = input("Message: ") or "AUTOCOR"

base_url = "https://webexapis.com/v1"
path = "/messages"
url = f"{base_url}{path}"

webex_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {pat}"
}

webex_payload = {
    "toPersonEmail": to,
    "text": message
}

rsp = requests.post(url, headers=webex_headers, json=webex_payload)
print(f"Received HTTP status code {rsp.status_code}/ {rsp.reason}")