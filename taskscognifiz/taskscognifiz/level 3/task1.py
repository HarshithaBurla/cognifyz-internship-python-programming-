#Task:Build a web scraper
from bs4 import BeautifulSoup
import requests
def webscrap(url):
    response=requests.get(url).text
    soup=BeautifulSoup(response,'lxml')
    print(soup.prettify())
    container=soup.find('div')
    rework=container.h1.text
    print(rework)
    ultag=container.find('ul')
    litag=ultag.find_all('li')
    for i in litag:
        print(i.text)
    ptag=container.find_all('p')
    for i in ptag:
        print(i.text)
    atag=container.a.text
    print(atag)
    link=container.a['class']
    print(link)
    print(container.a['href'])
    print(container.a['target'])
url="http://coreyms.com"
webscrap(url)
#output

##= RESTART: C:\taskscognifiz\level 3\task1.py
##<!DOCTYPE html>
##<html lang="en">
## <head>
##  <meta charset="utf-8"/>
##  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
##  <title>
##   Corey Schafer - Rework
##  </title>
##  <style>
##   body {
##            font-family: 'Arial', sans-serif;
##            line-height: 1.6;
##            color: #333;
##            max-width: 800px;
##            margin: 0 auto;
##            padding: 20px;
##            background-color: #f4f4f4;
##        }
##        .container {
##            background-color: white;
##            padding: 40px;
##            border-radius: 8px;
##            box-shadow: 0 0 10px rgba(0,0,0,0.1);
##        }
##        h1 {
##            color: #2c3e50;
##            border-bottom: 2px solid #3498db;
##            padding-bottom: 10px;
##        }
##        ul {
##            padding-left: 20px;
##        }
##        .youtube-link {
##            display: inline-block;
##            margin-top: 20px;
##            padding: 10px 20px;
##            background-color: #c4302b;
##            color: white;
##            text-decoration: none;
##            border-radius: 5px;
##            transition: background-color 0.3s;
##        }
##        .youtube-link:hover {
##            background-color: #e74c3c;
##        }
##  </style>
## </head>
## <body>
##  <div class="container">
##   <h1>
##    I'm Currently Reworking the Website!
##   </h1>
##   <p>
##    Hey everyone! My personal website is currently under construction and being reworked from scratch. This site will serve as a hub for all my programming tutorials and resources, complementing my YouTube channel.
##   </p>
##   <h2>
##    What to Expect
##   </h2>
##   <p>
##    Once completed, this website will feature:
##   </p>
##   <ul>
##    <li>
##     A comprehensive index of my programming tutorials
##    </li>
##    <li>
##     Short and Long-form Updates
##    </li>
##    <li>
##     Project showcases demonstrating various programming concepts and frameworks
##    </li>
##    <li>
##     Resources and tools to complement the tutorials
##    </li>
##    <li>
##     Additional Channel Resources
##    </li>
##   </ul>
##   <p>
##    The site will also serve as a platform for me to experiment with and demonstrate new web technologies, which I'll incorporate into future tutorials.
##   </p>
##   <p>
##    While the site is under construction, you can find my tutorials and stay updated through my YouTube channel:
##   </p>
##   <a class="youtube-link" href="https://www.youtube.com/user/schafer5" target="_blank">
##    Visit My YouTube Channel
##   </a>
##   <p>
##    Thank you for your patience and support. I'm looking forward to sharing this new resource with you soon!
##   </p>
##  </div>
## </body>
##</html>
##
##I'm Currently Reworking the Website!
##A comprehensive index of my programming tutorials
##Short and Long-form Updates
##Project showcases demonstrating various programming concepts and frameworks
##Resources and tools to complement the tutorials
##Additional Channel Resources
##Hey everyone! My personal website is currently under construction and being reworked from scratch. This site will serve as a hub for all my programming tutorials and resources, complementing my YouTube channel.
##Once completed, this website will feature:
##The site will also serve as a platform for me to experiment with and demonstrate new web technologies, which I'll incorporate into future tutorials.
##While the site is under construction, you can find my tutorials and stay updated through my YouTube channel:
##Thank you for your patience and support. I'm looking forward to sharing this new resource with you soon!
##Visit My YouTube Channel
##['youtube-link']
##https://www.youtube.com/user/schafer5
##_blank
