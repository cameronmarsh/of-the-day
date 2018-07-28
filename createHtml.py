#!/usr/bin/python

from scrapeContent import *

def constructHtml():
    htmlFile = open('index.html', 'w')
    
    ###write html header and metadata
    htmlFile.write('<!DOCTYPE html>')
    htmlFile.write('<html>')
    htmlFile.write('<head>')
    htmlFile.write('<meta charset="utf-8" />')
    htmlFile.write('<title>Of the Day</title>')
    htmlFile.write('<link rel="stylesheet" href="style.css">')
    htmlFile.write('</head>')
    htmlFile.write('<body>')
    
    ###write html body
    htmlFile.write("<h1>Of The Day</h1>")
    htmlFile.write('<hr/>')

    #write word of the day
    wod = getWordOfDay()
    htmlFile.write('<h2>Word of the Day</h2>')
    htmlFile.write('<div class="word-info">')
    htmlFile.write(wod['word'])
    htmlFile.write(wod['part-of-speech'] + "<br></br>")
    htmlFile.write(wod['pronunciation'])
    htmlFile.write('</div>')
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

    ###closing tags
    htmlFile.write('</body>')
    htmlFile.write('</html>')

    htmlFile.close()



#TODO: delete this
constructHtml()
