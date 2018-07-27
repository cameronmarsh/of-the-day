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
                print("Bad response\n" + resp.text)
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




#################################################
# Get Of-The-Day content
################################################

def getWordOfDay():
    """
    Get the word of the day from Merriam Webster (https://www.merriam-webster.com/word-of-the-day)
    Return a dictionary object with word, definition, and attributes
    """
    soup = getSoup('https://www.merriam-webster.com/dictionary/of-the-day') 
    
    if(soup == None):
        return None

    #get word info
    wod = {
            'word': str(soup.find('div', class_='word-and-pronunciation').h1),
            'part-of-speech': str(soup.find('div', class_='word-attributes').find(class_='main-attr')),
            'pronunctiation': str(soup.find('div', class_='word-attributes').find(class_='word-syllables')),
            'defn': soup.select('.wod-definition-container > p')
        }

    return wod



def getPoemOfDay():
    """
    Get the poem of the day from Poetry Foundation ('https://www.poetryfoundation.org/poems/poem-of-the-day')
    Return the poem's title, author, and content in a dictionary object
    """ 

    soup = getSoup('https://www.poetryfoundation.org/poems/poem-of-the-day')

    if(soup == None):
        return None

    #get poem info
    pod = {
            'title': str(soup.find('h1', class_='c-hdgSans c-hdgSans_2 c-mix-hdgSans_inline')),
            'author': str(soup.select('span > a')[0]),
            'lines': soup.select('.o-poem > div')
          }

    return pod




def getSubredditOfDay():
    """
    Get the Subreddit of the day from 'https://www.reddit.com/r/subredditoftheday/'

    Retrun the post containing the subreddit of the day including the subreddit, number of readers, 
    age of the subreddit, and the subreddit's description
    """

    soup = getSoup('https://www.reddit.com/r/subredditoftheday/')

    if(soup == None):
        return None

    #get subreddit info
    subPost = soup.select('.md')[0]
    subod = {
            'name': subPost.h4.a,
            'readers': subPost.p.find_all('strong')[0],
            'age': subPost.p.find_all('strong')[1],
            'description': subPost.p.find_next_siblings()
            }

    return subod



def getQuoteOfDay():
    """
    Get the quote of the day from Eduro ('https://www.eduro.com/')
    Return the quote and author
    """
    soup = getSoup('https://www.forbes.com/quotes/')

    if(soup == None):
        return None

    #get quote info
    qod = {
            'quote': soup.dailyquote.p
            'author': soup.dailyquote.find(class_='author').get_text().strip()
          }

    return qod


 






