from flask import Flask, request, jsonify, render_template
from core import ChatBot  # ChatBot của bạn

app = Flask(__name__)

chatbot = ChatBot()
conversation = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["GET"])
def start():
    global chatbot, conversation
    chatbot = ChatBot()
    conversation = chatbot.new_conversation()

    try:
        first = conversation.next()
    except Exception as e:
            return jsonify({"bot": f"Lỗi khi khởi tạo cuộc trò chuyện: {e}"}), 500

    return jsonify({"bot": first})


@app.route("/chat", methods=["POST"])
def chat():
    """Nhận message từ client, trả về response của bot."""
    global conversation, chatbot
    data = request.get_json(force=True)
    user_message = data.get("message", "").strip()

    if conversation is None:
        chatbot = ChatBot()
        conversation = chatbot.new_conversation()
        _ = conversation.next()  

    if not user_message:
        return jsonify({"bot": "Bạn chưa nhập nội dung.", "done": not conversation.is_next()})

    try:
        bot_response = conversation.next(message=user_message)
    except Exception as e:
        return jsonify({"bot": f"Lỗi xử lý: {e}", "done": True}), 500

    if bot_response is None:
        return jsonify({
            "bot": (
                "Cuộc hội thoại hiện tại đã kết thúc.\n"
                "Nếu muốn bắt đầu lại, hãy bấm nút 'Mới'."
            ),
            "done": True
        })

    done = not conversation.is_next()
    if done:
        bot_response += "\n\nCuộc hội thoại đã hoàn thành. Cám ơn bạn đã sử dụng An Giang Trip!"

    return jsonify({"bot": bot_response, "done": done})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
