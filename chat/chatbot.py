from fbchat import Client, log, Message
import time
import random
import json
import requests

# email = "benjiw93@hotmail.fr"
# mdp = "iamjarvis"
# uid = 1554146637

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"

class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		time.sleep(random.randrange(5, 10, 1) / 10)
		self.markAsRead(thread_id)
		if author_id == self.uid:
			return
		time.sleep(random.randrange(5, 10, 1) / 10)
		if message_object.text.find("exit") is not -1:
			self.send(Message(text='Je vais dormir !'), thread_id=thread_id, thread_type=thread_type)
			client.listening = False
			return
		if str.upper(message_object.text).find(str.upper("jarvis")) >= 0:
			self.send(Message(text='JARVIS !'), thread_id=thread_id, thread_type=thread_type)
		else:
			self.send(Message(text='Je ne comprends pas :('), thread_id=thread_id, thread_type=thread_type)

client = EchoBot("benjiw93@hotmail.fr", "iamjarvis", user_agent=user_agent)
client.listen()
print("<JARVIS> Je vais me déconnecter.")
client.logout()
print("<JARVIS> Je suis déconnecté. Bonne nuit, Benjamin.")
