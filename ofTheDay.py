#!/usr/bin/python

from scrapeContent import *

#TODO: put the web scraping content in the body of the html doc and add headers and metadata

def constructHtml():
    htmlFile = open('index.html', 'w')
    htmlFile.write("<h1>Of The Day</h1?>")
    
    #write word of the day
    wod = getWordOfDay()
    htmlFile.write('<h2>Word of the Day</h2>')
    htmlFile.write(wod['word'])
    htmlFile.write(wod['part-of-speech'] + "<br></br>")
    htmlFile.write(wod['pronunciation'])
    for defn in wod['defn']:
        htmlFile.write(str(defn))

    htmlFile.write('<hr></hr>')

    #write poem of the day
    pod = getPoemOfDay()
    htmlFile.write('<h2>Poem of the Day</h2>')
    htmlFile.write(pod['title'])
    htmlFile.write(pod['author'] + '<br></br>')
    for line in pod['lines']:
        htmlFile.write(str(line))

    htmlFile.write('<hr></hr>')
    
    #write subreddit of the day
    subod = getSubredditOfDay()
    htmlFile.write('<h2>Subreddit of the Day</h2>')
    htmlFile.write(subod['name'])
    htmlFile.write(subod['readersAndAge'])
    for par in subod['description']:
        htmlFile.write(str(par))

    htmlFile.write('<hr></hr>')

    #write quote of day
    qod = getQuoteOfDay()
    htmlFile.write('<h2>Quote of the Day</h2>')
    htmlFile.write(qod['quote'])
    htmlFile.write('<p>\t- ' + qod['author'] + '</p>') 

    htmlFile.write('<hr></hr>')

    #get meditation of day
    mod = getMeditationOfDay()
    htmlFile.write('<h2>Meditation of the Day</h2>')
    htmlFile.write('<h3>' + mod[0] + '</h3>')
    htmlFile.write(mod[1])

    htmlFile.write('<hr></hr>')

    htmlFile.close()

