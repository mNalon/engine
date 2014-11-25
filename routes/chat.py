__author__ = 'Nalon'
from flask import render_template, Blueprint,request,Response

bp_chat =  Blueprint('bp_chat',__name__)

@bp_chat.route('/chat/message', methods=['POST'])
def templateSubscription():
    try:
        request_json = request.json
        print "message received: %s" %request_json["message"]
        return Response(status=200)
    except:
        return Response(status=500)