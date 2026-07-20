const chatInput = document.getElementById("chat_input");
const button = document.getElementById("btn");
const chatBox = document.getElementById("chat_box");
const chatForm = document.getElementById("chat_form");

const apiUrl = "http://127.0.0.1:8000/api/chatbot/";

function updateButtonState() {
  button.disabled = chatInput.value.trim().length === 0;
}

chatInput.addEventListener("input", updateButtonState);

chatForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const userMessage = chatInput.value.trim();
  if (!userMessage) {
    return;
  }

  appendMessage(userMessage, "user");
  chatInput.value = "";
  updateButtonState();

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error || "Unable to fetch chatbot response");
    }

    appendMessage(data.reply || "No reply provided", "bot");
  } catch (error) {
    console.error("Error:", error);
    appendMessage("Sorry, something went wrong. Please try again.", "error");
  }
});

function appendMessage(text, sender) {
  const msgDiv = document.createElement("div");
  msgDiv.className = `message ${sender}`;
  msgDiv.textContent = text;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
