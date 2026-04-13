 
**Path:** `backend/app.py`  
  
```python  
from flask import Flask, render_template, request, jsonify  
from flask_socketio import SocketIO, emit  
from datetime import datetime  
import os  
from dotenv import load_dotenv  
from ai.chatbot import AQuilChatbot  
  
# Load environment variables  
load_dotenv()  
  
# Initialize Flask app  
app = Flask(__name__,   
            template_folder='../frontend',  
            static_folder='../frontend')  
  
# Initialize SocketIO for real-time chat  
socketio = SocketIO(app, cors_allowed_origins="*")  
  
# Initialize Chatbot  
chatbot = AQuilChatbot()  
  
# Store active users  
active_users = {}  
  
@app.route('/')  
def index():  
    """Render main page"""  
    return render_template('index.html')  
  
@app.route('/api/chat', methods=['POST'])  
def chat():  
    """Handle chat requests"""  
    try:  
        data = request.json  
        user_message = data.get('message', '')  
          
        if not user_message:  
            return jsonify({'error': 'Message cannot be empty'}), 400  
          
        # Get response from chatbot  
        response = chatbot.get_response(user_message)  
          
        return jsonify({  
            'status': 'success',  
            'response': response  
        })  
    except Exception as e:  
        return jsonify({  
            'status': 'error',  
            'message': str(e)  
        }), 500  
  
@socketio.on('connect')  
def handle_connect():  
    """Handle user connection"""  
    user_id = request.sid  
    active_users[user_id] = {  
        'connected_at': datetime.now(),  
        'messages': 0  
    }  
    emit('connection_response', {  
        'status': 'connected',  
        'message': 'Welcome to AQuil AI! 👋'  
    })  
    print(f"User {user_id} connected. Active users: {len(active_users)}")  
  
@socketio.on('disconnect')  
def handle_disconnect():  
    """Handle user disconnection"""  
    user_id = request.sid  
    if user_id in active_users:  
        del active_users[user_id]  
    print(f"User {user_id} disconnected. Active users: {len(active_users)}")  
  
@app.route('/api/stats', methods=['GET'])  
def get_stats():  
    """Get chatbot statistics"""  
    return jsonify({  
        'active_users': len(active_users),  
        'total_conversations': sum(u['messages'] for u in active_users.values())  
    })  
  
if __name__ == '__main__':  
    # Run the Flask app with SocketIO  
    socketio.run(app,   
                 host='0.0.0.0',   
                 port=5000,   
                 debug=True)
