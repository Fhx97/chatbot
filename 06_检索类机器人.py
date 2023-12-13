# 目前chatterbot只适配Python3.7
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# import spacy
# spacy.load('en_core_web_sm')
# spacy.load('en')


# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('I would like to book a flight.')

print(response)