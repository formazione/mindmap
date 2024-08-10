# app.py
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Initial mind map data
mind_map_data = {
    "nodes": [
        {"id": "balance-sheet", "title": "Balance Sheet", "subtitle": "", "x": 40, "y": 10},
        {"id": "purpose", "title": "What is it for?", "subtitle": "To show economic and financial data", "x": 20, "y": 150},
        {"id": "importance", "title": "Importance", "subtitle": "Very important document", "x": 60, "y": 150},
        {"id": "related-docs", "title": "Related Documents", "subtitle": "Stato Patrimoniale, Conto economico", "x": 40, "y": 300}
    ],
    "connections": [
        {"source": "balance-sheet", "target": "purpose"},
        {"source": "balance-sheet", "target": "importance"},
        {"source": "balance-sheet", "target": "related-docs"}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', mind_map_data=json.dumps(mind_map_data))

@app.route('/save', methods=['POST'])
def save():
    global mind_map_data
    mind_map_data = request.json
    return jsonify(mind_map_data)

@app.route('/get_mind_map')
def get_mind_map():
    return jsonify(mind_map_data)

if __name__ == '__main__':
    app.run(debug=True)

