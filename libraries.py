import html5lib
import requests
from bs4 import BeautifulSoup

def tgnews():
  URL = "https://t.me/s/ukrainenowenglish"
  r = requests.get(URL)
  
  soup = BeautifulSoup(r.content, 'html5lib')
  messages = soup.find_all("div", class_="tgme_widget_message_text")
  if len(messages) < 1024:
    lastmessage = messages[len(messages)-1].text
    return lastmessage
  else:
    lastmessage = "Message too large!"


def tgtime():
    URL = "https://t.me/s/ukrainenowenglish"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    time = soup.find_all("time", class_="time")
    date = time[len(time)-1].text
    return date