from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from models.report_model import insert_report

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reports', methods=['GET'])
def get_reports():
    from models.report_model import get_all_reports
    reports = get_all_reports()
    return jsonify(reports)

@app.route('/report', methods=['POST'])
def report():
    print("🔔 /report endpoint hit")

    data = request.get_json()
    print("📨 Received data:", data)

    try:
        new_report = insert_report(data)
        print("✅ Inserted report:", new_report)

        socketio.emit('new_report', new_report)
        return jsonify(new_report), 201
    except Exception as e:
        print("❌ Error inserting report:", e)
        return jsonify({"error": "Failed to insert report"}), 500

if __name__ == '__main__':
    socketio.run(app, debug=True)