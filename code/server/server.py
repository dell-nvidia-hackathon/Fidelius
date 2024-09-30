from flask import Flask, request, jsonify
import os
# from chat import chatopenai, chatlocal
from csvhandler import predictheaders, maskobfcsv

app = Flask(__name__)

@app.route("/getcsvheader", methods=['GET', 'POST'])
def getcsvheader():
    file_path = request.get_json()['filePath']
    
    # Construct the full path correctly
    full_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', file_path)

    try:
        temp = predictheaders(full_path)[0]['generated_text']
        headers = [line.strip() for line in temp.splitlines() if line.strip()]
        print(headers)
        return jsonify({"headers": headers})
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.route("/maskobfcsv", methods=['GET', 'POST'])
def maskcsv():
    input = request.get_json()
    print(input)
    
    # Construct the full path for masking
    full_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', input['filePath'])

    try:
        maskobfcsv(full_path)
        return jsonify({"message": "File masked successfully"})
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
