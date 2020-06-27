from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/generate-report' ,  methods = ['POST'])
def generate_report():
    req_data = request.get_json()
    print(req_data["sar"])
    
    return req_data;

if __name__ == "__main__":
    app.run(debug=True)