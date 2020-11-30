import tweepy
import json
import boto3
import os


# 4 cadenas para la autenticacion
consumer_key = "Wcol0aOJbVkYOqsYkA57pqO64"
consumer_secret = "DZ43ZrpdV8VS6GdO0LSaoacfOFciIrRg92Bl6QpktaQE4nd5qN"
access_token = "161715257-t2hUBSkhtbkoFNARy4jtaETzAOHQ60Xx1VxJW0eS"
access_token_secret = "lAaKqYJUNDkVAVlbbZgVgkC3T89LcH9lnmV8F22e6sT0j"


clientes3 = boto3.cliente('s3', aws_access_key_id="AKIAIRC3YFKTECX6J7KQ",
                      aws_secret_access_key="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")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

#Obtener informacion de un usario
data = api.me()
print(json.dumps(data._json, indent=4))

#carpeta = 'C:/Users/DELL/proyectoIN/proyecto'
#archivo = "tweet.json"

#with open(os.path.join(carpeta, archivo), 'w') as file:
#   json.dump(data,file)

#data_json = data._json
#print(data_json)

#Obtener informacion de otros usarios
#data = api.get_user("nike")
#print(json.dumps(data._json, indent=4))

#Obtener followers seguidores
#data = api.followers(screen_name="nike")
#print(len(data))
# Explicar cursor
for user in tweepy.Cursor(api.followers, screen_name="nike").items(10):
   print(json.dumps(user._json, indent=4))

#archivo1 = "tweet.json"

#with open(os.path.join(carpeta, archivo1), 'w') as file:
#   json.dump(user, file)

#Obtener followees
#for user in tweepy.Cursor(api.friends, screen_name="nike").items(2):
 #   print(json.dumps(user._json, indent=4))


#Obtener un timeline tweets de nike
#for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweet_mode="extended").items(100):
#    print(json.dumps(tweet._json,  indent=4))

#Buscar Tweets
for tweet in tweepy.Cursor(api.search, q="maradona", tweet_mode="extended").items(10):
   print(json.dumps(tweet._json, indent=4));


#archivo2 = "tweet.json"

#with open(os.path.join(carpeta, archivo2), 'w') as file:
#   json.dump(tweet, file)


#clientes3.put_object(
#    ACL='authenticated-read',
 #   Body=carpeta+archivo2,
   # Bucket='uniquindioia',
   # Key= "/proyecto" + archivo2,
#)

clientes3.put_object(
        Body=str(json.dumps(tweet, user, data)),
        Bucket='uniquindioia',
        Key='proyecto/' + 'archivos.json'
    )


