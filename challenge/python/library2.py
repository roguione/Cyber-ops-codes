#!/usr/bin/env python3

# Script: Ops 301 ops chal-12
# Author: Justin H
# Date of latest revision: 3/28/23
# Purpose: Requests Library
# Team: Geneva, Nick, && Sierra

import requests

# Prompt the user to input the URL
url = input("Enter the URL: ")

# Prompt the user to select an HTTP method
http_method = input("Select an HTTP method: GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS: ")

# Ask for confirmation before proceeding
confirm = input(f"You are about to send a {http_method} request to {url}. Confirm (Y/N)? ")
if confirm.lower() != "y":
    exit()

# Perform the request using requests library
if http_method == "GET":
    response = requests.get(url)
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

# Print the entire request sent
print(f"\nRequest sent:\n{response.request.method} {response.request.url}\n")

# Translate the status code to plain terms
status_codes = {
    100: "Continue",
    200: "OK",
    205: "Reset Content",
    300: "Multiple Choices",
    305: "Use Proxy",
    400: "Bad Request",
    405: "Method Not Allowed",
    410: "Gone",
    415: "Unsupported Media Type",
    416: "Requested Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    444: "Connection Closed Without Response",
    451: "Unavailable For Legal Reasons",
    499: "Client Closed Request",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage"
}

# Print the plain language meaning of each status code
for code in status_codes:
    print(f"{code}: {status_codes[code]}")
