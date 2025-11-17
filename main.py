
from core import ChatBot

def main():
    chatbot = ChatBot()
    conversation = chatbot.new_conversation()
    t = conversation.next()
    print(t)
    t = conversation.next("an giang")
    print(t)
    t = conversation.next("can tho")
    print(t)

if __name__ == "__main__":
    main()