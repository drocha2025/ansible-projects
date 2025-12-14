from getpass import getpass
import requests
import urllib3

urllib3.disable_warnings()

hostname = input("IP address or hostname: ") or "sandboxdnac2.cisco.com"
username = "devnetuser"
password = "Cisco123!"

basic_auth = (username, password)

base_url = f"https://{hostname}"
path = "/dna/system/api/v1/auth/token"
url = f"{base_url}{path}"

catalyst_center_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

rsp = requests.post(url, auth=basic_auth, verify=False)

token = rsp.json()["Token"]
catalyst_center_headers["X-Auth-Token"] = token

path = "/dna/intent/api/v1/productNames"
url = f"{base_url}{path}"

rsp = requests.get(url, headers=catalyst_center_headers, verify=False)

products = rsp.json()["response"]

for product in products:
    print(product["productName"])