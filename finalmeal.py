from secret import *
import foursquare

# Construct the client object
# client = foursquare.Foursquare(consumer_key, consumer_secret, redirect_uri='')



client = foursquare.Foursquare(consumer_key, consumer_secret)
df = client.venues('40a55d80f964a52020f31ee3')
print df




print consumer_key
print client