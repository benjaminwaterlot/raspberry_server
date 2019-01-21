# Mail : benjiw93@hotmail.fr
# MDP : iamjarvis

from fbchat import Client, log, Message
import time
import random
import json

# email = "benjiw93@hotmail.fr"
# mdp = "iamjarvis"
# uid = 1554146637

prev_cookies_file = open("chat/cookies.json", "r+")
prev_cookies = prev_cookies_file.read()
if prev_cookies == "":
	prev_cookies = None
else:
	prev_cookies = json.loads(prev_cookies)
print(prev_cookies)
prev_cookies_file.close()

class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		time.sleep(random.randrange(5, 10, 1) / 10)
		self.markAsRead(thread_id)
		log.info(f"{message_object} from {thread_id} in {thread_type.name}")
		if author_id != self.uid:
			time.sleep(random.randrange(5, 10, 1) / 10)
			if str.upper(message_object.text).find(str.upper("jarvis")) >= 0:
				self.send(Message(text='JARVIS !'), thread_id=thread_id, thread_type=thread_type)
			else:
				self.send(Message(text='Je ne comprends pas :('), thread_id=thread_id, thread_type=thread_type)
		if message_object.text.find("exit") is not -1:
			time.sleep(random.randrange(5, 10, 1) / 10)
			client.listening = False
	def onLoggedIn(self, email):
		cookies = open("chat/cookies.json", "w")
		cookies.write(json.dumps(self.getSession()))
		cookies.close()

client = EchoBot("benjiw93@hotmail.fr", "iamjarvis", session_cookies=prev_cookies)
client.listen()
print("<JARVIS> Je vais me déconnecter.")
client.logout()
print("<JARVIS> Je suis déconnecté. Bonne nuit, Benjamin.")
