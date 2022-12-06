 #from bs4 import BeautifulSoup 
#import requests 
import time
import logging
#import matplotlib.pyplot as plt 

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#Command Handlers
def start(update, context):
    update.message.reply_text('You have summond the Bogdabot!')


#function to respond to help cmd
def help(update, context):
    update.message.reply_text('I am currently not equipped to help you.')

#function to echo the users message
def btc(update, context):
    update.message.reply_text('Its all going to zero!!!!! AHHHHHHHHH!!!!!')

def list(update, context):
    update.message.reply_text('start, help, btc')  

#Create a function to get the price of a cryptocurrency
def price(btc):
#Get the URL
    url = "https://www.google.com/search?q="+btc+"+price"
    
    #Make a request to the website
    HTML = requests.get(url) 
  
    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser') 
  
    #Find the current price 
    #text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
#Return the text 
    return text

#function to send a gif
#def gif(update, context):
 #   update.message.reply_img = mpimg.imread('bogdabotgif.jpg')
#imgplot = plt.imshow(img)
#plt.show() )

    

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("5264574549:AAGMPi4Uk8Q-WJNhuahtfBf3zhd3WKCACi8", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("btc", btc))
    dp.add_handler(CommandHandler("list", list))
    dp.add_handler(CommandHandler("price", price ))
    #dp.add_handler(CommandHandler("gif", bog))
    #dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()