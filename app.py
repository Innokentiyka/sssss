from flask import Flask, send_file

app = Flask(name)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_file('index.html')

if __name__ == 'main':
    app.run(debug=True, port=5000)