const chatContainer = document.getElementById('chatContainer');  
const messageInput = document.getElementById('messageInput');  
const sendBtn = document.getElementById('sendBtn');  
  
let conversationHistory = [];  
  
sendBtn.addEventListener('click', sendMessage);  
  
messageInput.addEventListener('keypress', (e) => {  
    if (e.key === 'Enter' && !e.shiftKey) {  
        e.preventDefault();  
        sendMessage();  
    }  
});  
  
function sendMessage() {  
    const message = messageInput.value.trim();  
      
    if (!message) return;  
      
    addMessage(message, 'user');  
    messageInput.value = '';  
      
    conversationHistory.push({  
        role: 'user',  
        content: message,  
        timestamp: new Date()  
    });  
      
    showLoadingIndicator();  
    sendToBackend(message);  
}  
  
function addMessage(content, role) {  
    const messageDiv = document.createElement('div');  
    messageDiv.className = `message ${role}`;  
      
    const now = new Date();  
    const timeString = now.toLocaleTimeString('id-ID', {  
        hour: '2-digit',  
        minute: '2-digit'  
    });  
      
    messageDiv.innerHTML = `  
        <div>  
            <div class="message-content">${escapeHtml(content)}</div>  
            <div class="timestamp">${timeString}</div>  
        </div>  
    `;  
      
    chatContainer.appendChild(messageDiv);  
    chatContainer.scrollTop = chatContainer.scrollHeight;  
}  
  
function showLoadingIndicator() {  
    const loadingDiv = document.createElement('div');  
    loadingDiv.className = 'message bot';  
    loadingDiv.innerHTML = `  
        <div class="message-content">  
            <div class="loading">  
                <div class="loading-dot"></div>  
                <div class="loading-dot"></div>  
                <div class="loading-dot"></div>  
            </div>  
        </div>  
    `;  
    loadingDiv.id = 'loadingMessage';  
    chatContainer.appendChild(loadingDiv);  
    chatContainer.scrollTop = chatContainer.scrollHeight;  
}  
  
function removeLoadingIndicator() {  
    const loadingMessage = document.getElementById('loadingMessage');  
    if (loadingMessage) {  
        loadingMessage.remove();  
    }  
}  
  
function sendToBackend(message) {  
    fetch('/api/chat', {  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/json'  
        },  
        body: JSON.stringify({  
            message: message  
        })  
    })  
    .then(response => response.json())  
    .then(data => {  
        removeLoadingIndicator();  
          
        if (data.status === 'success') {  
            const botResponse = data.response;  
            addMessage(botResponse, 'bot');  
              
            conversationHistory.push({  
                role: 'bot',  
                content: botResponse,  
                timestamp: new Date()
