import gradio as gr
from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def text_to_speech(text):
    tts.tts_to_file(text=text, file_path="output.wav")
    return "output.wav"

iface = gr.Interface(
    fn=text_to_speech,
    inputs="text",
    outputs="audio",
    title="Text-to-Speech with Coqui TTS",
    description="Enter text to convert to speech."
)

iface.launch()
