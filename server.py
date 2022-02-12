from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

balance = 100
transactions = []

@app.route('/atm/getBalance',methods = ['GET'])
def getBalance():
   return jsonify({"balance":balance});

@app.route('/atm/getHistory',methods = ['GET'])
def getHistory():
   return jsonify(transactions);

@app.route('/atm/deposit',methods = ['POST'])
def deposit():
   global balance
   transaction = request.get_json()
   transaction["type"] = "deposit"
   transaction["time"] = datetime.now()
   balance = balance + transaction["amount"]
   transactions.append(transaction)
   return jsonify({"balance":balance});

@app.route('/atm/withdraw',methods = ['POST'])
def withdraw():
   global balance
   transaction = request.get_json()
   transaction["type"] = "withdraw"
   transaction["time"] = datetime.now()
   balance = balance - transaction["amount"]
   transactions.append(transaction)
   return jsonify({"balance":balance});

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8081, debug = True)
