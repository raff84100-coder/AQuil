import re  
from datetime import datetime  
  
class AQuilChatbot:  
    """  
    AQuil AI - Productivity Assistant  
    """  
      
    def __init__(self):  
        """Initialize chatbot"""  
          
        # Knowledge base untuk respons cepat  
        self.knowledge_base = {  
            'hello': 'Halo! 👋 Saya AQuil, asisten produktivitas Anda. Ada yang bisa saya bantu?',  
            'hi': 'Hi there! 😊 Siap membantu Anda mencapai goals hari ini!',  
            'help': 'Saya bisa membantu Anda dengan:\n- Mengatur jadwal kerja\n- Memberikan motivasi\n- Mengoreksi kesalahan Anda\n- Berpikir kritis tentang masalah\n\nApa yang bisa saya bantu?',  
            'siapa kamu': 'Saya AQuil AI - asisten produktivitas yang peduli dengan progress Anda. 🤖',  
            'thanks': 'Sama-sama! Senang bisa membantu. Terus semangat! 💪',  
            'terima kasih': 'Sama-sama! Keep pushing forward! 🚀'  
        }  
          
        # Patterns untuk deteksi intent  
        self.patterns = {  
            'task': r'(task|tugas|pekerjaan|kerja|deadline)',  
            'motivation': r'(motivasi|semangat|capek|lelah|stress)',  
            'error': r'(salah|error|bug|masalah|tidak bisa)',  
            'plan': r'(rencana|planning|jadwal|schedule)',  
            'thinking': r'(pikir|analisis|bagaimana|kenapa|apa alasan)'  
        }  
      
    def detect_intent(self, user_message):  
        """Deteksi intent dari pesan user"""  
        message_lower = user_message.lower()  
          
        for intent, pattern in self.patterns.items():  
            if re.search(pattern, message_lower):  
                return intent  
        return None  
      
    def check_grammar_and_spelling(self, text):  
        """Deteksi kesalahan penulisan"""  
        errors = []  
          
        # Deteksi huruf besar di awal kalimat  
        if text and text[0].islower():  
            errors.append("💡 Tips: Mulai kalimat dengan huruf besar")  
          
        # Deteksi kata-kata umum yang salah tulis  
        common_mistakes = {  
            'gk': 'tidak',  
            'msh': 'masih',  
            'yg': 'yang',  
            'sdh': 'sudah',  
            'krn': 'karena',  
            'blm': 'belum'  
        }  
          
        for mistake, correction in common_mistakes.items():  
            if mistake in text.lower():  
                errors.append(f"💡 '{mistake}' → gunakan '{correction}'")  
          
        return errors  
      
    def respond_to_task(self, user_message):  
        """Respons untuk task/tugas"""  
        return "Bagus! 🎯 Breakdown task Anda menjadi langkah-langkah kecil. Mulai dari yang paling penting dulu. Apa langkah pertama Anda?"  
      
    def respond_to_motivation(self, user_message):  
        """Respons untuk motivasi"""  
        return "Saya mengerti, Anda sedang merasa capek. 💙 Ini normal! Coba ambil break 5-10 menit, minum air, lalu lanjut lagi. Kamu bisa! 💪"  
      
    def respond_to_error(self, user_message):  
        """Respons untuk kesalahan"""  
        return "Tidak masalah membuat kesalahan! 🤔 Itu adalah bagian dari pembelajaran. Ceritakan detailnya, saya siap membantu!"  
      
    def respond_to_plan(self, user_message):  
        """Respons untuk planning"""  
        return "Planning yang baik adalah fondasi kesuksesan! 📋\n\nPastikan:\n✅ Sasaran jelas\n✅ Timeline realistis\n✅ Prioritas\n✅ Fleksibel\n\nMau kita buat plan detailnya?"  
      
    def respond_to_critical_thinking(self, user_message):  
        """Respons untuk berpikir kritis"""  
        return "Pertanyaan yang bagus! 🤔 Mari kita analisis bersama dengan data dan logika. Share lebih detail!"  
      
    def get_response(self, user_message):  
        """Get response dari chatbot"""  
          
        # Check untuk quick responses  
        message_lower = user_message.lower().strip()  
        if message_lower in self.knowledge_base:  
            return self.knowledge_base[message_lower]  
          
        # Check untuk grammar/spelling errors  
        errors = self.check_grammar_and_spelling(user_message)  
          
        # Detect intent  
        intent = self.detect_intent(user_message)  
          
        # Build response  
        response = ""  
          
        # Jika ada error, koreksi dengan halus  
        if errors:  
            response += "Sedikit catatan:\n"  
            for error in errors:  
                response += error + "\n"  
            response += "\n"  
          
        # Generate response berdasarkan intent  
        if intent == 'task':  
            response += self.respond_to_task(user_message)  
        elif intent == 'motivation':  
            response += self.respond_to_motivation(user_message)  
        elif intent == 'error':  
            response += self.respond_to_error(user_message)  
        elif intent == 'plan':  
            response += self.respond_to_plan(user_message)  
        elif intent == 'thinking':  
            response += self.respond_to_critical_thinking(user_message)  
        else:  
            response += f"Menarik! 🤔 Ceritakan lebih detail, dan saya akan coba membantu Anda. Apa yang Anda ingin tahu?"  
          
        return response
