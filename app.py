
from flask import Flask, request
from flask_restful import Api

from src.get_audio_connector import get_audio
from src.node_status_connector import new_status
from src.return_audio_results_connector import return_audio

app = Flask(__name__)
api = Api(app)

@app.route("/get_audio", methods=["GET"])
def get_audio_connector():
    return get_audio(request.json)

@app.route("/update_status", methods=["GET"])
def update_status():
    return new_status(request.json)