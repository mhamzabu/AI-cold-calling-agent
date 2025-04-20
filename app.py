from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/voice", methods=["POST"])
def voice():
    caller_input = request.form.get("SpeechResult") or "Hello"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": caller_input}]
    )

    reply = response['choices'][0]['message']['content']

    twilio_response = VoiceResponse()
    twilio_response.say(reply, voice='alice')
    return str(twilio_response)

if __name__ == "__main__":
    app.run(debug=True)
