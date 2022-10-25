import urllib.request as urllib
from urllib.parse import urlparse

def main(url):

    print('Checking Connection')

    response = urllib.urlopen(url)
    print('Connected to ', url, " successfully")
    print("Response Code: ",response.getcode())

print("This is our Site Connection Checker")
print("---------------------------------------------------")
input_url = input("Please enter the url of the website: ")

if not urlparse(input_url).scheme:
    input_url = 'http://' + input_url

main(input_url)