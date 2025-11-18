
from datetime import datetime
import os
import json

def append_registration(file_path: str, destination: str, date_str: str):
    # Tạo mã ID = thời gian hiện tại
    now = datetime.now()
    registration_id = now.strftime("%Y%m%d_%H%M%S")   # ví dụ: 20250114_225501

    new_data = {
        "id": registration_id,
        "destination": destination,
        "date": date_str,
        "timestamp": now.isoformat()
    }

    # Nếu file chưa tồn tại → tạo file mới
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([new_data], f, ensure_ascii=False, indent=4)
        return

    # Đọc file cũ
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            data = []  # nếu file rỗng hoặc lỗi format

    # Append
    data.append(new_data)

    # Ghi lại file JSON
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)