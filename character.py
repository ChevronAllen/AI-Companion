import keyboard
import os
import json

class Character:
    name = ""
    startup_history = ""
    name_activation = False
    voice_id=""
    transcriber = None
    voice_service = None
    ai_model = None
