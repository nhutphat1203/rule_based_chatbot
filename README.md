# Rule-based Chatbot

## Giới thiệu

**Rule-based Chatbot** là một ứng dụng chatbot đơn giản được xây dựng bằng Python, phục vụ mục đích **trả lời câu hỏi người dùng dựa trên các quy tắc (rules) định sẵn**. Chatbot này không sử dụng trí tuệ nhân tạo hay machine learning, mà dựa hoàn toàn vào **luật (rules) và tiền xử lý dữ liệu** để phản hồi người dùng.

Project này là một **đồ án ở trường**, giúp sinh viên hiểu cách:

* Xử lý và chuẩn hóa dữ liệu đầu vào của người dùng.
* Tách các chức năng của chatbot thành module rõ ràng.
* Thiết kế luồng xử lý của chatbot

---

## Tính năng chính

1. **Nhận input từ người dùng** qua console.
2. **Normalize dữ liệu**: chuyển chữ hoa thành chữ thường, loại bỏ dấu, xóa ký tự đặc biệt.
3. **Rule-based response**: chatbot phản hồi dựa trên các quy tắc định sẵn.
4. **Module hóa code**: tách riêng các chức năng thành các module (data, normalize, rules).
5. **Entry point `main.py`** để chạy chương trình.

---

## Cách chạy project

1. Cài đặt Python 3.10 trở lên.
2. Tạo môi trường ảo (khuyến nghị):

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Cài đặt các package từ `requirements.txt`:

```bash
pip install -r requirements.txt
```

4. Chạy chương trình:

```bash
python main.py
```

---

## Công nghệ sử dụng

* Ngôn ngữ: Python 3.10+
* Module Python: `json`, `re`, `unicodedata`
* Cấu trúc code: Module hóa + Rule-based logic

---

## Hướng mở rộng

* Thêm **nhiều rules hơn** để phản hồi linh hoạt.
* Thêm **quản lý nhiều loại input** như ngày tháng, tên địa điểm.
* Tích hợp **cơ sở dữ liệu** để lưu lịch sử trò chuyện.
* Nâng cấp sang **chatbot AI** với NLP.
