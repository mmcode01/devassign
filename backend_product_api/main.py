from flask import Flask, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Product details
""'Stocks': 'Stocks are shares of a company.',
'Bonds': 'Bonds are fixed-income investments, for example a loan made by an investor to a borrower.',
'Mutual Funds': 'Mutual funds pool money from many investors to purchase securities.'""

@app.route('/products/<product_name>', methods=['GET'])
def get_product_details(product_name):
    """TO DO: Returns details for the specified investment product."""



    return jsonify({
        'operation_id': operation_id,
        'product': product_name,
        'description': product_details[product_name]
    })
