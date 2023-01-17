"""These are some sample record processing functions. We are going to use it in the code later on."""

import requests

def upper_case(in_str: str)->str:
    """A dummy function that converts a string to upper case"""
    return in_str.upper()

def lower_case(in_str: str) -> str:
    return in_str.lower()

def capitalize(in_str: str) -> str:
    return in_str.capitalize()

def get_ip_city(ip_number:str) -> str:
    api_url: str = f"https://ipinfo.io/{ip_number}/geo"
    response = requests.get(api_url)
    return response.json().get('city')


