import time
import keyboard
import asyncio
import os
from dotenv import load_dotenv
from voiceTranscription import VoiceTranscriptionService 
from aimodel import AIModel
from Profiles.sapphire import Sapphire

load_dotenv()

DEFAULT_CHARACTER="Sapphire"
character = Sapphire()
transcriber_manager = character.transcriber()
ai_manager = character.ai_model()

