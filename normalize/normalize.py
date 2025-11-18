
import unicodedata
import re
from datetime import datetime

def normalize_input(text: str) -> str:
    """
    Chuẩn hóa dữ liệu đầu vào:
    - chuyển chữ hoa thành chữ thường
    - loại bỏ dấu tiếng Việt
    - loại bỏ khoảng trắng thừa
    - loại bỏ ký tự đặc biệt (trừ chữ và số)
    """
    # 1. Chuyển chữ hoa thành chữ thường
    text = text.lower()

    # 2. Loại bỏ dấu tiếng Việt
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')

    # 3. Loại bỏ ký tự đặc biệt, giữ chữ và số
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # 4. Xóa khoảng trắng thừa
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def normalize_date(text: str) -> datetime | None:
    cleaned = re.findall(r"\d+", text)   # lấy toàn bộ số trong chuỗi

    if len(cleaned) != 3:
        return None  # không phải dạng ngày hợp lệ
    
    day, month, year = cleaned

    # xử lý năm 2 chữ số (ví dụ 25 → 2025)
    if len(year) == 2:
        year = "20" + year

    date_str = f"{day}/{month}/{year}"

    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except:
        return None
