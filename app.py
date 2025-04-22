from flask import Flask, request, jsonify
import openai
from chatbot_config import SYSTEM_PROMPT, MODEL_NAME, initialize_openai

# Initialize API
initialize_openai()

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.6
        )

        answer = response['choices'][0]['message']['content']
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
