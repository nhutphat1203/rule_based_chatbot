
from typing import List, Tuple
from model import Trip
from normalize import normalize_input

class Node:
    def __init__(self, data: List[Trip]):
        self.data = data
        self.iteration = 3
        self.ith_iteration = 0
        self.trip_names = [trip.destination for trip in self.data]
        self.choosed_trip = None
    
    def is_next(self):
        return self.ith_iteration < self.iteration
    
    def next(self, message: str="") -> str:
        if not self.is_next():
            return None
        match self.ith_iteration:
            case 0:
                self.ith_iteration += 1
                return "Chào mừng bạn đến An Giang Trip! Xin hãy cho tôi biết địa điểm bạn muốn ghé thăm"
            case 1:
                can_next, trip = self.__check_trip_name(message)
                if can_next:
                    self.choosed_trip = trip
                    return f"Địa điểm bạn muốn đến là {trip.destination}, có giá vé là {trip.cost} vnd và có các chuyển ở các ngày sau: {", ".join(trip.times)}\n Xin hãy chọn ngày bạn định đi!"
                else:
                    return f"Hiện tại chỉ có các chuyến từ An Giang đến các địa điểm sau: {", ".join(self.trip_names)}"
            case 2:
                pass
    def __check_trip_name(self, trip_name: str) -> Tuple[bool, Trip]:
        trip_name = normalize_input(trip_name)
        for trip in self.data:
            if normalize_input(trip.destination) == trip_name:
                return True, trip
        return False, None
        
    