from plyer import notification
import requests

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = ".ico", #Add .ico image file with its current location
        timeout = 15

    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    notifyMe("Dear User","You have been attacked!") #Add your message here which is supposed to be popped
   
        