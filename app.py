from chain import BlockChain
from flask import Flask, request
from flask.json import jsonify
import json


app = Flask(__name__)

blockchain = BlockChain()

@app.route("/mine", methods=["GET"])
def mine_block():
    message = "Mining Failed"
    if blockchain.mine():
        message = "Blocks added to BlockChain"
    response = {
        "message": message
    }
    return jsonify(response), 200


@app.route("/chain", methods=["GET"])
def display_chain():
    json_string = json.dumps(blockchain.chain, default=obj_dict)
    response = {
        "chain": json_string,
        "length": len(blockchain.chain)
    }
    return jsonify(response), 200


@app.route("/valid", methods=["GET"])
def is_valid():
    validity = blockchain.chain_valid(blockchain.chain)
    message = "Valid" if validity else "Invalid"
    response = {
        "message": message
    }
    return jsonify(response), 200


@app.route("/add", methods=["POST"])
def add_new_transaction():
    request_data = json.loads(request.data)
    transaction_data = request_data.get("data")
    message = "No Transaction data found"
    if transaction_data:
        blockchain.new_transactions.append(transaction_data)
        message = "Added new transaction"
    response = {
        "message": message
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)