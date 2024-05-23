import nltk
from nltk.chat.util import Chat, reflections


Coversations = [
    (r'Hii|Hello', ['Hello!', 'Hey there!', 'Hi!']),
    (r'How are you', ['I\'m good, thank you!', 'I\'m doing well, Thanks for asking!']),
    (r'who are you|what is your name', ['I\'m a ChatBot, I don\'t have a name.', 'I\'m just a ChatBot.']),
    (r'(.*) your name(.*)', ['My name is ChatBot.', 'You can call me ChatBot.']),
    (r'(.*) help(.*)', ['I can help you in many topics. just ask!']),
    (r'(.*) (Location|City) ?(.*)', ['I am an AI and I don\'t have a physical location.']),
    (r'Bye|Goodbye', ['Goodbye!', 'Take care!', 'See you later!']),
    (r'(.*)',['I\'m not Designed for this yet!']) # We can Generate more Responsis like This - 
]


ChatBot = Chat(Coversations, reflections)


print("Hello! I'm a simple ChatBot. You can start chatting with me or type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("ChatBot: Goodbye!")
        break
    else:
        response = ChatBot.respond(user_input)
        print("ChatBot:", response)

