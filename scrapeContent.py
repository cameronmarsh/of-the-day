#!/usr/bin/python

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
            'word': str(soup.find('div', class_='word-and-pronunciation').h1.string.wrap(soup.new_tag('h3'))),
            'part-of-speech': str(soup.find('div', class_='word-attributes').find(class_='main-attr')),
            'pronunciation': str(soup.find('div', class_='word-attributes').find(class_='word-syllables')),
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
            'title': str(soup.find('h1', class_='c-hdgSans c-hdgSans_2 c-mix-hdgSans_inline').string.wrap(soup.new_tag('h3'))),
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
    subPost = None
    posts = soup.select('.s1w05phc-0')[0].find_all('div')
    for post in posts:
        if len(post.select('.icon-sticky')) == 0:
            if post.h4 != None:
                subPost = post
                break

    subod = {
            'name': str(subPost.h4.string.wrap(soup.new_tag('h3'))),
            'readersAndAge': str(subPost.p),
            'description': subPost.p.find_next_siblings()
            }

    return subod



def getQuoteOfDay():
    """
    Get the quote of the day from Eduro ('https://www.eduro.com/')
    Return the quote and author
    """
    soup = getSoup('https://www.eduro.com')

    if(soup == None):
        return None

    #get quote info
    #TODO: there has to be a better way to get the author's name, this seems hacky
    author = soup.dailyquote.find(class_='author').get_text().strip().split()
    author = author[1] + ' ' + author[2]
    qod = {
            'quote': str(soup.dailyquote.p),
            'author': author
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
        bookTitle = book.h2.get_text()
        for meditation in book.find_all('p'):
            try:
                for note in meditation.select('a') + meditation.select('span'):
                    note.decompose()
                    meditations.append((bookTitle, meditation.encode('utf-8')))
            except Exception as e:
                meditations.append((bookTitle, meditation.encode('utf-8')))

    #pick a random mediation 
    return choice(meditations)







 



