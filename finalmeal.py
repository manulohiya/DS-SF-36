import foursquare

# Construct the client object
# client = foursquare.Foursquare(client_id='3PCWWGPVXQ5VB1KVS0FM3XEZDZMIJPRV0UONHWZPSLO5LCMO', client_secret='BUH1TEAK2ATYAPXL1C2VDHXZPVZAX4V42IBDSQNJGFVVUG0R', redirect_uri='')

consumer_key = '3PCWWGPVXQ5VB1KVS0FM3XEZDZMIJPRV0UONHWZPSLO5LCMO'
consumer_secret = 'BUH1TEAK2ATYAPXL1C2VDHXZPVZAX4V42IBDSQNJGFVVUG0R'

# access_token = 	'1010066696-zHPbnHrUti3THtEPl3HXRUN4eAuGUyjvnhLjsWg'
# access_token_secret = 'VPB99S6rb6TesCwhMODwUnEBd4sh9kVUIU3j9hy1eatnn'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

client = foursquare.Foursquare(client_id='3PCWWGPVXQ5VB1KVS0FM3XEZDZMIJPRV0UONHWZPSLO5LCMO', client_secret='BUH1TEAK2ATYAPXL1C2VDHXZPVZAX4V42IBDSQNJGFVVUG0R')
df = client.venues('40a55d80f964a52020f31ee3')
print df
# api = tweepy.API(auth)



print "this is working"
