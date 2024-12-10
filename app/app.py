from recommendation.similarity_model import Similarity_Model
import config
from flask import Flask, request, jsonify


similarity_model = Similarity_Model()
# svd_model = SVD_Model()

app = Flask(__name__)

@app.route('/pearson/user', methods=['GET'])
def pearson_user():
    user_id = request.args.get('user_id')
    number_of_recommendations = request.args.get('number_of_recommendations') or 5
    
    user_id = int(user_id)
    number_of_recommendations = int(number_of_recommendations)
    
    similarity_model.load_model(config.USER_USER_MATRIX, config.PEARSON_MODEL)
    response = similarity_model.get_top_n_recommendations(user_id, number_of_recommendations)
    
    return jsonify(response)


@app.route('/pearson/movie', methods=['GET'])
def pearson_item():
    item_id = request.args.get('title')
    number_of_recommendations = request.args.get('number_of_recommendations') or 5
    number_of_recommendations = int(number_of_recommendations)
    
    similarity_model.load_model(config.ITEM_ITEM_MATRIX, config.PEARSON_MODEL)
    response = similarity_model.get_top_n_recommendations(item_id, number_of_recommendations)
    
    return jsonify(response)
    

@app.route('/cosine/user', methods=['GET'])
def cosine_user():
    user_id = request.args.get('user_id')
    number_of_recommendations = request.args.get('number_of_recommendations') or 5
    
    user_id = int(user_id)
    number_of_recommendations = int(number_of_recommendations)
    
    similarity_model.load_model(config.USER_USER_MATRIX, config.COSINE_MODEL)
    response = similarity_model.get_top_n_recommendations(user_id, number_of_recommendations)
    
    return jsonify(response)


@app.route('/cosine/movie', methods=['GET'])
def cosine_item():
    item_id = request.args.get('title')
    number_of_recommendations = request.args.get('number_of_recommendations') or 5 
    number_of_recommendations = int(number_of_recommendations)
    
    similarity_model.load_model(config.ITEM_ITEM_MATRIX, config.COSINE_MODEL)
    response = similarity_model.get_top_n_recommendations(item_id, number_of_recommendations)
    
    return jsonify(response)

