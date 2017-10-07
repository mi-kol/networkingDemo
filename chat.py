from chatterbot import ChatBot

chatbot = ChatBot("Training Example")

while True:
	print chatbot.get_response(raw_input())

