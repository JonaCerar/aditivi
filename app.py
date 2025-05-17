from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

def load_additives():
    try:
        df = pd.read_csv('data/additives.csv')
        return df.to_dict('records')
    except Exception as e:
        print(f"Error loading additives: {e}")
        return []

additives = load_additives()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').strip().lower()
    if not query:
        return jsonify([])
    results = []
    for additive in additives:
        if (query in str(additive['E_number']).lower() or 
            query in str(additive['name']).lower()):
            results.append(additive)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True) 