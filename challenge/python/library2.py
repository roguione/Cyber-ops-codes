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
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}

# Print the status code in plain terms
if response.status_code in status_codes:
    print(f"Status code: {response.status_code} - {status_codes[response.status_code]}")
else:
    print(f"Status code: {response.status_code}")
