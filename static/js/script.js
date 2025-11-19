  const chatLog = document.getElementById("chat-log");
        const messageInput = document.getElementById("message-input");
        const sendBtn = document.getElementById("send-btn");
        const newBtn = document.getElementById("new-btn");
        const statusText = document.getElementById("status-text");

        function addMessage(sender, text, senderType) {
            const row = document.createElement("div");
            row.classList.add("message-row", senderType);

            const bubble = document.createElement("div");
            bubble.classList.add("bubble", senderType);

            const senderLabel = document.createElement("div");
            senderLabel.classList.add("bubble-sender");
            senderLabel.textContent = sender;

            const content = document.createElement("div");
            content.textContent = text;

            const timeLabel = document.createElement("div");
            timeLabel.classList.add("bubble-time");
            const now = new Date();
            const hh = String(now.getHours()).padStart(2, "0");
            const mm = String(now.getMinutes()).padStart(2, "0");
            timeLabel.textContent = `${hh}:${mm}`;

            bubble.appendChild(senderLabel);
            bubble.appendChild(content);
            bubble.appendChild(timeLabel);

            row.appendChild(bubble);
            chatLog.appendChild(row);
            chatLog.scrollTop = chatLog.scrollHeight;
        }

        async function startConversation() {
            statusText.textContent = "Đang tải...";
            try {
                const res = await fetch("/start");
                const data = await res.json();
                chatLog.innerHTML = "";
                if (data.bot) {
                    addMessage("An Giang Trip Bot", data.bot, "bot");
                }
                statusText.textContent = "Đang trò chuyện";
            } catch (e) {
                console.error(e);
                statusText.textContent = "Lỗi kết nối";
                addMessage("Hệ thống", "Không thể khởi tạo cuộc trò chuyện.", "bot");
            }
        }

        async function sendMessage() {
            const text = messageInput.value.trim();
            if (!text) return;

            addMessage("Bạn", text, "user");
            messageInput.value = "";
            messageInput.focus();
            statusText.textContent = "Đang xử lý...";

            try {
                const res = await fetch("/chat", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message: text })
                });
                const data = await res.json();
                if (data.bot) {
                    addMessage("An Giang Trip Bot", data.bot, "bot");
                }
                statusText.textContent = data.done ? "Hội thoại kết thúc" : "Đang trò chuyện";
            } catch (e) {
                console.error(e);
                addMessage("Hệ thống", "Có lỗi xảy ra khi xử lý. Hãy thử lại.", "bot");
                statusText.textContent = "Lỗi kết nối";
            }
        }

        sendBtn.addEventListener("click", sendMessage);
        newBtn.addEventListener("click", startConversation);

        messageInput.addEventListener("keydown", (e) => {
            if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
        
        startConversation();