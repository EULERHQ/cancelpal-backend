from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/generate": {"origins": "*"}})

@app.route('/generate', methods=['POST'])
def generate_letter():
    data = request.json
    company = data.get('company')
    type_ = data.get('type')
    name = data.get('name')
    address = data.get('address')
    reason = data.get('reason', 'No reason provided.')

    letter = f"""To Whom It May Concern at {company},

I am writing to formally request the cancellation of my {type_} subscription. Please consider this as notice of termination as per your cancellation policy.

Subscriber Name: {name}
Address: {address}
Reason: {reason}

Please confirm the cancellation in writing.

Sincerely,
{name}
"""
    return letter

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

