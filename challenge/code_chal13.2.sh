Justin H
2/22/2023
Team M-n-M 



#!/bin/bash

# Define domain_info function
function domain_info() {
    echo "WHOIS information for $1:"
    whois $domain
    echo ""

    echo "DNS information for $1:"
    dig $1 @8.8.8.8
    echo ""

    echo "Host information for $1:"
    host $1 8.8.8.8
    echo ""

    echo "NSLOOKUP information for $1:"
    nslookup $1 8.8.8.8
    echo ""
}

# Prompt user for domain name and store in variable
read -p "8.8.8.8: " domain

# Call domain_info function with user input
domain_info $domain