from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='',  
                              body='I CANT BELIEVE THIS WORKS',      
                              to='+916232883113' 
                          ) 
 
print(message.sid)