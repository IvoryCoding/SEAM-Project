from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servers')
def servers():
    return render_template('serverdata.html')

@app.route('/post_json', methods=['POST'])
def process_json():
    contentType = request.headers.get('Content-Type')
    if contentType == 'application/json':
        json = request.get_json()
        print(json)

        ip = json['server']
        status = json['status']
        network = json['network']
        process = json['process']

        return '\n\t\tServer: {}\n\t\t{}\n\t\t{}\n\t\t{}'.format(ip, status, network, process) #json['age'] will return just the age value
    else:
        return 'Content-Type is not supported!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')