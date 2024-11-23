from flask import request
from nexosphere.sentiment.tickerListService.tickerService import *

def tickerRoutes(bp):
    
    @bp.route("/user/getTickers", methods=['GET'])
    def getTickers():
        userId = request.args.get('userId')
        result = getTickerChoices(int(userId))
        
        if result == {}:
            return {"message": "user not found"}, 404
        
        return result, 200


    @bp.route("/user/createTicker", methods=['POST'])
    def createTicker():
        user_id = request.args.get('user_id')
        ticker = request.args.get('ticker')
        
        result = addTickerChoice(int(user_id), ticker)
        
        if result != {}:
            return getTickerChoices(int(user_id)), 201
        
        return {"message": "user already exist"}, 403
    

    @bp.route("/user/updateTicker", methods=['PUT'])
    def updateTicker():
        user_id = request.args.get('user_id')
        ticker = request.args.get('ticker')
        
        result = updateTickerChoice(int(user_id), ticker)

        if result == {}:
            return {"message": "user not found"}, 404
        
        return getTickerChoices(int(user_id)), 200
    
    
    @bp.route("/user/deleteTicker", methods=['DELETE'])
    def deleteTicker():
        user_id = request.args.get('user_id')
        ticker = request.args.get('ticker')
        
        result = deleteTickerChoice(int(user_id), ticker)

        if result == {}:
            return {"message": "user not found"}, 404
        
        return getTickerChoices(int(user_id)), 200