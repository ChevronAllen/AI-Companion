
class ElevenLabsVoices():
    def __init__(self):
        pass

    # Convert text to speech, then save it to file. Returns the file path
    def text_to_audio(self, input_text, voice="", save_as_wave=True, subdirectory=""):
        pass

    # Convert text to speech, then play it out loud
    def text_to_audio_played(self, input_text, voice="Doug VO Only"):
        pass

    # Convert text to speech, then stream it out loud (don't need to wait for full speech to finish)
    def text_to_audio_streamed(self, input_text, voice="Doug VO Only"):
        pass