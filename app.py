
from flask import Flask, request
from flask_restful import Api

from src.get_audio_connector import get_audio
from src.node_status_connector import new_status
from src.return_audio_results_connector import return_audio
from src.node_init_connector import node_init

app = Flask(__name__)
api = Api(app)

@app.route("/get_audio", methods=["GET"])
def get_audio_connector():
    return get_audio(request.json)

@app.route("/update_status", methods=["GET"])
def update_status():
    return new_status(request.json)

@app.route("/return_audio", methods=["GET"])
def return_audio_results():
    return return_audio(request.json)

@app.route("/node_init", methods=["GET"])
def initialize_node():
    return node_init(request.json)

if __name__ == "__main__":
    app.run(debug = True, threaded = True)