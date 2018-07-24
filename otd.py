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
        with closing(get(url, stream=True)) as resp:
	    if isGoodResponse(resp):
	        return resp.content
	    else:
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





#################################################
# Get Of-The-Day content
################################################

def getWordOfDay():
    """
    Get the word of the day from Merriam Webster (https://www.merriam-webster.com/word-of-the-day)
    Return a dictionary object with word, definition, and attributes
    """
    resp = getUrl('https://www.merriam-webster.com/word-of-the-day')

    if resp != None:
        #dict containing info to be returned

        soup = BeautifulSoup(resp, 'html.parser')
        
        #get word info
        wod = {
                'word': soup.find('div', class_='word-and-pronunciation').h1.get_text(),
                'part-of-speech': soup.find('div', class_='word-attributes').find(class_='main-attr').get_text(),
                'pronunctiation': soup.find('div', class_='word-attributes').find(class_='word-syllables').get_text(),
                'def': []
              }

        #get word definition
        for defn in soup.select('.wod-definition-container > p'):
            wod['def'].append(defn.get_text())

        return wod

    else:
        return None




def getPoemOfDay():
    """
    Get the poem of the day from Poetry Foundation ('https://www.poetryfoundation.org/poems/poem-of-the-day')
    Return the poem's title, author, and content in a dictionary object
    """ 




