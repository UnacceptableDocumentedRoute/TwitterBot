import tweepy
from time import sleep
consumer_key = "0lNINtKpjj9lwu4SicEjIlWXN"
consumer_secret = "B3GsaHM72erBdEOhwAMQPdt4ZmVtOMwXYPpHRLYMrmWP945mwA"
access_token = "919645971801292801-G3NBsF9k1kYvylcWBVU3miJD95vBvma"
access_token_secret = "BqLfBGiLU871Brq1GK4e3hNvWsqRwet29XRWkaUMsAWzB"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)

def Search():
    RESTorStream = input("REST or Stream?")
    searchfor = input("Search for: ")
    sleepfor = input("Sleep for: ")

    if RESTorStream == "Stream":
        class MyStreamListener(tweepy.StreamListener):

            def on_status(self, status):
                print("\n" + status.author.name + ":\n" +
                      status.text +
                      "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                if sleepfor != 0: sleep(int(sleepfor))

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        myStream.filter(track=[searchfor], is_async=False)

    if RESTorStream == "REST":
        limit = int(input("Tweet limit: "))
        alreadyread = []
        for tweet in tweepy.Cursor(api.search, q=searchfor, lang="en").items(limit):
            if tweet.text not in alreadyread:
                print("\n" + tweet.author.name + "\n" +
                      tweet.text +
                      "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                alreadyread.append(tweet.text)
                if sleepfor != 0: sleep(int(sleepfor))
            elif tweet.text in alreadyread:
                print("Duplicate, moving on...")

def Tweet():
    tweet = input("Message: ")
    print("Tweeted! " + tweet)
    status = api.update_status(status=tweet)
    sleep(0.5)

action = input("What would you like to do today?(Search, Tweet) ")

if action == "Search":
    Search()

if action == "Tweet":
    Tweet()