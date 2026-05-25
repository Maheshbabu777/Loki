import google.generativeai as genai
from app.shared.config import settings

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=settings.google_api_key)

        self.agent_model = genai.GenerativeModel("gemini-3.5-flash")

        self.reasoning_model = genai.GenerativeModel("gemini-3.1-pro")

    def test_connection(self):
        try:
            response = self.agent_model.generate_content("Respond with 'OK'")
            return response.text.strip()=="OK"
        except Exception:
            return False
        

gemini_client = GeminiClient()