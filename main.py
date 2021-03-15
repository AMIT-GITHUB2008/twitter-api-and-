import tweepy
from textblob import TextBlob



# Authenticate to Twitter
auth = tweepy.OAuthHandler("MEiz2Q82sjwRxbmyYmiPwJv2K", "JghSoKQ8XSLYANShKleqka5klLwnGXXVtsOz0FaBYEBWAv13P5")
auth.set_access_token("2938403336-ITv9zkdjO7bvdL9X52xivYyLBWFQAoseHxeR2Ep", "Pe1CgZ6JyhFHy0XK5ROyBTe11LnzawnQp52k8YfiPKDDQ")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
         if('RT @' not in status.text):
           blop=TextBlob(status.text)
           blopx=blop.sentiment
           polarity=blopx.polarity
           subjectivity=blopx.subjectivity
           la={
               "name":status.id_str,
               "name 2":status.text,
               "p":polarity,
               "s":subjectivity
           }
           print(la)
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['corona','vaccine'])
