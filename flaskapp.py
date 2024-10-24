from flask import Flask, request, abort
from flask_cors import CORS
from langchain.load.dump import dumps

from flaskapp.scripts.far_dei_chat import FarDeiChat

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
print("Flask app started")

@app.post("/api/v1/fardeichat")
def deptbot_fardei_ask():
    """
    This function is responsible for chatting with the AI about FAR DEI activity.
    :return: void
    """
    question = request.form.get('question')
    thread_id = request.form.get('thread_id')
    if thread_id == 'null':
        thread_id = ''

    chat = FarDeiChat()
    try:
        answer = chat.far_dei_ask(question, thread_id)
        return dumps(answer)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        abort(500, description=f"An error occurred: {str(e)}")

@app.get("/api/v1/health")
def health():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True, port=9001)
