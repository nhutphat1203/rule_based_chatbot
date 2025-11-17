
from data import load_data
from core import Node

data = load_data("data/trip.json")

class ChatBot:
    
    def __init__(self):
        pass
    
    def new_conversation(self) -> Node:
        return Node(data=data)
    