{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request\
from twilio.twiml.voice_response import VoiceResponse\
import openai\
import os\
\
app = Flask(__name__)\
openai.api_key = os.getenv("OPENAI_API_KEY")\
\
@app.route("/voice", methods=["POST"])\
def voice():\
    caller_input = request.form.get("SpeechResult") or "Hello"\
    \
    response = openai.ChatCompletion.create(\
        model="gpt-3.5-turbo",\
        messages=[\{"role": "user", "content": caller_input\}]\
    )\
\
    reply = response['choices'][0]['message']['content']\
\
    twilio_response = VoiceResponse()\
    twilio_response.say(reply, voice='alice')\
    return str(twilio_response)\
\
if __name__ == "__main__":\
    app.run(debug=True)\
}