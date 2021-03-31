from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "It's working"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) # specify port=8080
