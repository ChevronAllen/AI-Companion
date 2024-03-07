from character import Character
from LLMs.open_ai import OpenAIModel
from Transcribers.azureTranscriber import AzureSpeechService

class Sapphire(Character):
    def __init__(self):
        self.name = "Sapphire"
        self.startup_history = "sapphire"
        self.name_activation = True
        self.voice_id="Sapphire"
        self.transcriber = AzureSpeechService
        self.ai_model = OpenAIModel
        self.voice_service = None
