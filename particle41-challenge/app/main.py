from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    # Get client IP (works behind proxies)
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    
    return jsonify({
        "ip": ip.split(',')[0],  # Handle multiple IPs in X-Forwarded-For
        "timestamp": datetime.utcnow().isoformat() + "Z"   
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))