from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servers')
def servers():
    return render_template('serverdata.html')

@app.route('/servers', methods=['POST'])
def parse_request():
    data = request.get_json()
    return f'Recieved! {data}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')