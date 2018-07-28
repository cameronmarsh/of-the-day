#!/usr/bin/python

from requests import get
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from contextlib import closing

################################################
# Web scraping functions
# Source: realpython.com
###############################################

def getUrl(url):
    """
    Make a HTTP GET request for the content at <url>
    Return the page if successful, otherwise return None
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux) Gecko/20100101 Firefox/61.0'}
        with closing(get(url, stream=True, headers=headers)) as resp:
	    if isGoodResponse(resp):
	        return resp.content
	    else:
                print "Bad response, got code", resp.status_code
	        return None

    except RequestException as e:
        logError("Error during requests to {0} : {1}", format(url, str(e)))
        return None



def isGoodResponse(resp):
    """
    Returns True if <resp> is HTML, returns False if not
    """
    contentType = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and contentType != None
            and contentType.find('html') > -1)


def logError(e):
    """
    Log errors to terminal output
    """
    print(e)



def getSoup(url):
    """
    Returns the html-parsed BeautifulSoup object based on the URL
    """
    resp = getUrl(url)

    if resp != None:
        return BeautifulSoup(resp, 'html.parser')
    else:
        return None

