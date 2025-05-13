from flask import Blueprint, jsonify

# blueprint is a small flask application(Sub-application) with independent functions
api_bp = Blueprint('api', __name__)

@api_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})
