from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Product details
product_details = {
    'Stocks': 'Stocks are shares of ownership in a company.',
    'Bonds': 'Bonds are fixed-income investments representing a loan made by an investor to a borrower.',
    'Mutual Funds': 'Mutual funds pool money from many investors to purchase securities.'
}

@app.route('/products/<product_name>', methods=['GET'])
def get_product_details(product_name):
    """Returns details for the specified investment product."""



    return jsonify({
        'operation_id': operation_id,
        'product': product_name,
        'description': product_details[product_name]
    })