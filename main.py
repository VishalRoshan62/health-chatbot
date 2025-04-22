from flask import Flask, request, jsonify
import openai
import os

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

app = Flask(__name__)

# System prompt to keep responses health-focused
SYSTEM_PROMPT = """
You are HealthBot, a helpful and knowledgeable healthcare assistant. 
You provide safe, non-diagnostic advice about symptoms, wellness, healthy habits, and when to see a doctor.
Do not give medical diagnoses or prescriptions.
"""

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
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

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
