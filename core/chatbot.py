
from data import load_data
from core import Node

data = load_data("data/trip.json")

class ChatBot:
    
    def __init__(self):
        self.registration_data_path = 'registration.json'
    
    def new_conversation(self) -> Node:
        return Node(data=data, registration_data_path=self.registration_data_path)
    