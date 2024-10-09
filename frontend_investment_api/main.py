from flask import Flask, request, jsonify
import requests
import uuid
import logging
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Available products for user to choose from
# investment_products = 'Stocks', 'Bonds', 'Mutual Funds'

@app.route('/investments', methods=['GET'])
def get_investment_options():
      """ TODO: Returns the list of available investment products."""
     

      return jsonify({
        'operation_id': operation_id,
        'products': investment_products
    })


@app.route('/investments/select', methods=['POST'])
def select_investment():
    """TODO: User selects an investment product, Frontend API retrieves details from Backend API."""
    


    # Return product details to user
    product_details = backend_response.json()
    return jsonify({
        'operation_id': operation_id,
        'product': selected_product,
        'details': product_details
    })


