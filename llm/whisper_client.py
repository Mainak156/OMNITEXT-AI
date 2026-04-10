import whisper

# Load once (IMPORTANT for performance)
model = whisper.load_model("base")  # you can change to small/medium

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]