#!/usr/bin/env python3

# Script: Ops 301 ops chal-12
# Author: Justin H
# Date of latest revision: 3/28/23
# Purpose: Requests Library
# Team: Geneva, Nick, && Sierra

import requests

# Define the URLs to choose from
urls = [
    "https://www.google.com/",
    "https://api.github.com/users/octocat",
    "https://jsonplaceholder.typicode.com/posts/1"
]

# Prompt the user to select a URL
for i, url in enumerate(urls):
    print(f"{i+1}. {url}")
while True:
    choice = input("Select a number for the URL: ")
    if choice.isdigit() and int(choice) in range(1, len(urls)+1):
        url = urls[int(choice)-1]  # store the selected URL in the url variable
        break
    else:
        print("Invalid input. Please enter a number corresponding to the URL you want to select.")

# Prompt the user to enter the HTTP method
http_method = input("Enter HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Perform the request using requests library
try:
    if http_method == "GET":
        response = requests.get(url)  # use the selected URL for the request
    elif http_method == "POST":
        response = requests.post(url)
    elif http_method == "PUT":
        response = requests.put(url)
    elif http_method == "DELETE":
        response = requests.delete(url)
    elif http_method == "HEAD":
        response = requests.head(url)
    elif http_method == "PATCH":
        response = requests.patch(url)
    elif http_method == "OPTIONS":
        response = requests.options(url)
    else:
        print("Invalid HTTP method selected. Exiting...")
        exit()
except requests.exceptions.RequestException as e:
    print(f"An error occurred while performing the request: {e}")
    exit()

# Print the entire request sent
print(f"\nRequest sent:\n{response.request.method} {response.request.url}\n")

# Translate the status code to plain terms
status_codes = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed" ,
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required"
}

# Print the status code in plain terms
if response.status_code in status_codes:
    print(f"Status code: {response.status_code} - {status_codes[response.status_code]}")
else:
    print(f"Status code: {response.status_code}")
