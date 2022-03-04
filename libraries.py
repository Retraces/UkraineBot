import html5lib  # Due to the nature of Telegram and how the formatting, using html5lib is a good idea
import requests
from bs4 import BeautifulSoup

def tgnews():
  URL = "https://t.me/s/ukrainenowenglish"  # Where we're getting information from, REMEMBER TO USE THE "PREVIEW IN BROWSER" link
  r = requests.get(URL)
  
  soup = BeautifulSoup(r.content, 'html5lib')
  messages = soup.find_all("div", class_="tgme_widget_message_text")  # Grab the latest message as "messages"
  if len(messages) < 1024:  # Discord embeds have a limit of 1024 characters, Telegram messages can be quite large, we will simply exempt the message and provide the Telegram link
    lastmessage = messages[len(messages)-1].text
    return lastmessage
  else:
    lastmessage = "Message too large!"


def tgtime():
    URL = "https://t.me/s/ukrainenowenglish"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    time = soup.find_all("time", class_="time")  #  Grabs the message time in UTC
    date = time[len(time)-1].text  # A repeat of above, simply grabs the latest message (-1) and utilizes it
    return date
