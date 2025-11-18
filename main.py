
from core import ChatBot

def main():
    chatbot = ChatBot()
    conversation = chatbot.new_conversation()
    response = conversation.next()
    print(response)
    while conversation.is_next():
        message = input("Hãy nhập câu trả lời của bạn: ")
        response = conversation.next(message=message)
        print(response)

if __name__ == "__main__":
    main()