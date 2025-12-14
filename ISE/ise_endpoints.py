<<<<<<< HEAD
import requests
import urllib3
from getpass import getpass
from requests.auth import HTTPBasicAuth

# Disable insecure HTTPS warnings (sandbox has expired cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

hostname = input("IP address and hostname: ") or "devnetsandboxise.cisco.com"
username = input("Username: ") or "readonly"
password = getpass("") or "ISEisC00L"

basic_auth = HTTPBasicAuth(username, password)

base_url = f"https://{hostname}"
path = "/api/v1/endpoint"
url = f"{base_url}{path}"

ise_headers = {
        "Accept": "application/json"
}

print(f" Sending GET request to {url}")

# Add authentication + ignore SSL verification
rsp = requests.get(url, auth=basic_auth, headers=ise_headers, verify=False)

endpoints = rsp.json()
print(f" Received a {type(endpoints)} response containing {len(endpoints)} elements and HTTP status code {rsp.status_code}")

input("Press enter to show all MAC addresses...")

for endpoint in endpoints:
=======
import requests
import urllib3
from getpass import getpass
from requests.auth import HTTPBasicAuth

# Disable insecure HTTPS warnings (sandbox has expired cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

hostname = input("IP address and hostname: ") or "devnetsandboxise.cisco.com"
username = input("Username: ") or "readonly"
password = getpass("") or "ISEisC00L"

basic_auth = HTTPBasicAuth(username, password)

base_url = f"https://{hostname}"
path = "/api/v1/endpoint"
url = f"{base_url}{path}"

ise_headers = {
        "Accept": "application/json"
}

print(f" Sending GET request to {url}")

# Add authentication + ignore SSL verification
rsp = requests.get(url, auth=basic_auth, headers=ise_headers, verify=False)

endpoints = rsp.json()
print(f" Received a {type(endpoints)} response containing {len(endpoints)} elements and HTTP status code {rsp.status_code}")

input("Press enter to show all MAC addresses...")

for endpoint in endpoints:
>>>>>>> 71579013ceb74eacfdb5497cbdd634346bfe5746
        print(endpoint["mac"])