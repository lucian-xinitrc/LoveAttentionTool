import subprocess
from utils import startTree as st
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/start-tree', methods=['GET', 'POST'])

def start_tree():
    data = request.get_json()

    if data.get("message") == "start":
        try:
            treeSw = st.NewTree(5)
            treeSw.StartTree()
            return jsonify({"status": "Tree activated"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
