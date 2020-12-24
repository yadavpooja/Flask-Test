from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/test")
def hello():
    return ("hello")

@app.route("/api")
def hi():
    return jsonify({"name": "ram", "class": "second"})

#this is used to run locally    
app.run(debug=True)
