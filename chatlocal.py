from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english"
)

print "Now initiating session"

while True:
	print chatbot.get_response(raw_input())
