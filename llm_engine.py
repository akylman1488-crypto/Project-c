import google.generativeai as genai
from config import cfg

class Brain:
    def __init__(self):
        genai.configure(api_key=cfg.GOOGLE_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        self.chat = self.model.start_chat(history=[])

    def think(self, prompt, context=""):
        full_prompt = f"System Context: {context}\nUser: {prompt}"
        try:
            response = self.chat.send_message(full_prompt)
            return response.text
        except Exception as e:
            return f"Brain Error: {e}"
