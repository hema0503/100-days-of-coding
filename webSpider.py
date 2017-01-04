
import urllib.request
from html.parser import HTMLParser
from urllib import parse


class LinkParser(HTMLParser):
    def handle_starttag(self, tags, attrs):
        if tags== 'a':
            for(key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    print(newUrl)
                    self.links = self.links + [newURL]


    def getLinks(self, url):
        self.links = [ ]
        self.baseUrl = url
        response = urllib.request.urlopen(url)
        print(response.read( ))
        if response.getheader('Content-Type') == 'text/javascript':
            htmlBytes = response.read( )
            htmlResponse = htmlByte.decode("utf-8")
            print(htmlResponse)
            self.feed(htmlResponse)
            return htmlResponse, self.links
        else:
            return "", [ ]

def spider(url, word, maxPageLimit):
        pagesToVisit = [url]
        numPagesVisited = 0
        wordFound = False
        while numPagesVisited < maxPageLimit and pagesToVisit != [ ] and wordFound == False:
            numPagesVisited = numPagesVisited + 1
            url = pagesToVisit[0]
            pagesToVisit = pagesToVisit[1:]
            try:
                print(numPagesVisited, "Visiting", url)
                parser = LinkParser( )
                data, links = parser.getLinks(url)
                if data.find(word)>-1:
                    wordFound = True
                pagesToVisit = pagesToVisit + links
                print("Success")
            except:
                print("Failed")
        if wordFound == True:
            print("The word was found in the page", url)
        else:
            print("The word was never found")




