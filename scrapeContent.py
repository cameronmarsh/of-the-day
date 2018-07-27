from scrapeTools import *
from random import choice


#################################################
# Get Of-The-Day content
################################################

def getWordOfDay():
    """
    Get the word of the day from Merriam Webster (https://www.merriam-webster.com/word-of-the-day)
    Return a dictionary object with word, definition, and attributes
    """
    soup = getSoup('https://www.merriam-webster.com/word-of-the-day') 
    
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
            'quote': soup.dailyquote.p,
            'author': soup.dailyquote.find(class_='author').get_text().strip()
          }

    return qod



def getMeditationOfDay():
    """
    Get a random meditation from Marcus Aurelius' "Meditations" from the online book ('http://oll.libertyfund.org/titles/antoninus-the-meditations-of-the-emperor-marcus-aurelius-antoninus-2008')

    Return a tuple containing the book number and the meditation
    """

    soup = getSoup('http://oll.libertyfund.org/titles/antoninus-the-meditations-of-the-emperor-marcus-aurelius-antoninus-2008')

    if(soup == None):
        return None
    
    #build meditation data and add book I to the list
    books = [soup.find(id='lfHutcheson_div_016')]
    
    #add remaining books to list
    for div in soup.find(id='lfHutcheson_div_016').find_next_siblings('div'):
        #check if the section is a book
        if div.h2.get_text().split()[0] == "BOOK":
            books.append(div)
    
    
    #list of all meditations to sample
    meditations = []
    for book in books:
        bookTitle = book.h2
        for meditation in book.find_all('p'):
            meditations.append((bookTitle, meditation))

    #pick a random mediation 
    return choice(meditations)







 



