from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from typing import Optional

def get_html(url: str):
    """
    Takes a URL as input and returns the HTML content at that URL.

    Args:
        url (str): The URL to retrieve HTML content from.

    Returns:
        str: The HTML content at the specified URL, or None if an error occurs.
    """
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e.reason)
        return None
    except URLError as e:
        print("error")
        return None
    else:
        return html.read().decode("utf-8")


def get_soup(url: str) -> Optional[BS]:
    """
    Retrieves HTML content from the specified URL and returns it as a BeautifulSoup object.

    Args:
        url (str): The URL to retrieve HTML content from.

    Returns:
        bs4.BeautifulSoup: A BeautifulSoup object representing the HTML content at the specified URL,
        or None if an error occurs.
    """
    html_content = get_html(url)
    if html_content is None:
        print("No HTML content")
        return None
    else:
        soup = BS(html_content, "html5lib")
        return soup


    
