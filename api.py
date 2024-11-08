import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/greet', methods=['GET'])
def greet():
    try:
        # Get the 'name' parameter from the query string, default to 'World' if not provided
        name = request.args.get('name', 'World')
        
        response = {"message": f"Hello, {name}!"}
        
        app.logger.info(f"Request received with name: {name}")
        app.logger.info(f"Sending response: {response}")

        return jsonify(response)
    
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        
        # Return a JSON response with a 500 status code
        return jsonify({"error": "An internal server error occurred"}), 500

# Custom error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    app.logger.warning(f"Page not found: {request.path}")
    return jsonify({"error": "Page not found"}), 404

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Internal server error: {error}")
    return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
