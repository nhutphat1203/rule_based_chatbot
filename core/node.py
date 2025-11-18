
from typing import List, Tuple
from model import Trip
from normalize import normalize_input, normalize_date
from core.registration import append_registration

class Node:
    def __init__(self, data: List[Trip], registration_data_path: str):
        self.data = data
        self.iteration = 3
        self.ith_iteration = 0
        self.trip_names = [trip.destination for trip in self.data]
        self.choosed_trip = None
        self.trip_dates = None
        self.registration_data_path = registration_data_path
    
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
                    self.ith_iteration += 1
                    return f"Địa điểm bạn muốn đến là {trip.destination}, có giá vé là {trip.cost} vnd và có các chuyển ở các ngày sau: {", ".join(trip.times)}\n Xin hãy chọn ngày bạn định đi!"
                else:
                    return f"Hiện tại chỉ có các chuyến từ An Giang đến các địa điểm sau: {", ".join(self.trip_names)}"
            case 2:
                user_date = self.user_date_in_trip(message)
                if user_date is None:
                    return f"Ngày bạn nhập không hợp lệ! Bạn hãy nhập lại đúng các ngày trong các ngày sau: {", ".join(self.choosed_trip.times)}"
                else:
                    self.ith_iteration += 1
                    append_registration(self.registration_data_path, self.choosed_trip.destination, user_date)
                    return f"Chuyến đi tới {self.choosed_trip.destination} vào ngày {user_date} đã được ghi nhận vào hệ thống. Nếu bạn muốn biết nhiều hơn về chuyến đi hãy gọi cho số 099999999. Cám ơn bạn đã chọn dịch vụ của chúng tôi!"
                    
    def __check_trip_name(self, trip_name: str) -> Tuple[bool, Trip]:
        trip_name = normalize_input(trip_name)
        for trip in self.data:
            if normalize_input(trip.destination) == trip_name:
                return True, trip
        return False, None
    
    def user_date_in_trip(self, user_input: str) -> str | None:
        user_date = normalize_date(user_input)
        if user_date is None:
            return None
        for t in self.choosed_trip.times:
            if user_date == normalize_date(t):
                return t
        return None
    