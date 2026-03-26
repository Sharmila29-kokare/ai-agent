from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Agent is running!"

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    # Simple summarization logic (safe fallback)
    summary = text[:100] + "..."

    return jsonify({
        "original_text": text,
        "summary": summary
    })

if __name__ == '__main__':
    import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))