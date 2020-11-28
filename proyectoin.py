import tweepy
import json

# 4 cadenas para la autenticacion
consumer_key = "Wcol0aOJbVkYOqsYkA57pqO64"
consumer_secret = "DZ43ZrpdV8VS6GdO0LSaoacfOFciIrRg92Bl6QpktaQE4nd5qN"
access_token = "161715257-t2hUBSkhtbkoFNARy4jtaETzAOHQ60Xx1VxJW0eS"
access_token_secret = "lAaKqYJUNDkVAVlbbZgVgkC3T89LcH9lnmV8F22e6sT0j"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

#Obtener informacion de un usario
data = api.me()
print(json.dumps(data._json, indent=4))

#data_json = data._json
#print(data_json)

#Obtener informacion de otros usarios
#data = api.get_user("nike")
#print(json.dumps(data._json, indent=4))

#Obtener followers seguidores
#data = api.followers(screen_name="nike")
#print(len(data))
# Explicar cursor
for user in tweepy.Cursor(api.followers, screen_name="nike").items(15):
   print(json.dumps(user._json, indent=4))

#Obtener followees
#for user in tweepy.Cursor(api.friends, screen_name="nike").items(2):
 #   print(json.dumps(user._json, indent=4))


#Obtener un timeline tweets de nike
#for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweet_mode="extended").items(100):
#    print(json.dumps(tweet._json,  indent=4))

#Buscar Tweets
for tweet in tweepy.Cursor(api.search, q="maradona", tweet_mode="extended").items(10):
   print(json.dumps(tweet._json, indent=4));






