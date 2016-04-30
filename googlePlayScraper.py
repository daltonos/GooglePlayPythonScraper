#this imports the lib lxml, which is a lib for handling reading html web pages. this make our job 100 times simpler
from lxml import html #here I'm saying I'll be using the html module from lxml
import requests #and here I'm saying I'll be using the requests (for acessing the internet) also from the lxml lib. As you can see, this is a powerful library


#assign all content from the given url to the variable 'page'
page = requests.get('https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms')

#then I transform the html page content to a string
tree = html.fromstring(page.content)


#Google play has put the installs value inside a div tag which has the attribute 'itemprop' set to 'numDownloads', so I use xpath to select that div TAG especifically.
#xpath isn't Python or any programming language. It is a language you can use in most other programming languages to navigate through an HTML document from any source.

installs = tree.xpath("//div[@itemprop='numDownloads']/text()")



#then I just print the result
print installs
