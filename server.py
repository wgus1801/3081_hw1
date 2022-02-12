from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

value = 0
calculations = []

@app.route('/calc/getValue',methods = ['GET'])
def getValue():
   return jsonify({"value":value});

@app.route('/calc/getComputations',methods = ['GET'])
def getComputations():
   return jsonify(calculations);

@app.route('/calc/add',methods = ['POST'])
def add():
   global value
   calculation = request.get_json()
   calculation["type"] = "add"
   calculation["time"] = datetime.now()
   value = value + calculation["amount"]
   calculations.append(calculation)
   return jsonify({"value":value});

@app.route('/calc/subtract',methods = ['POST'])
def subtract():
   global value
   calculation = request.get_json()
   calculation["type"] = "subtract"
   calculation["time"] = datetime.now()
   value = value - calculation["amount"]
   calculations.append(calculation)
   return jsonify({"value":value});

@app.route('/calc/multiply',methods = ['POST'])
def multiply():
   global value
   calculation = request.get_json()
   calculation["type"] = "multiply"
   calculation["time"] = datetime.now()
   value = value * calculation["amount"]
   calculations.append(calculation)
   return jsonify({"value":value});

@app.route('/calc/divide',methods = ['POST'])
def divide():
   global value
   calculation = request.get_json()
   calculation["type"] = "divide"
   calculation["time"] = datetime.now()
   value = value / calculation["amount"]
   calculations.append(calculation)
   return jsonify({"value":value});


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8081, debug = True)
