# -*- coding: utf-8 -*-

__author__ = 'Nalon'
from flask import render_template, Blueprint,request,Response,jsonify,json
from datetime import datetime
from collections import deque

queue_messages = deque([])

bp_chat =  Blueprint('bp_chat',__name__)

@bp_chat.route('/chat/message', methods=['POST'])
def templateSubscription():
    try:
        json_data = {
                        "message" : "",
                        "time_stamp" : "",
                        "user_id" : ""
                    }
        request_json = request.json

        json_data["message"] = request_json["message"].encode('UTF-8')
        json_data["time_stamp"] = datetime.now().strftime("%d/%m/%y  %H:%M:%S")
        json_data["user_id"] = request_json["user_id"]
        if len(queue_messages) == 20:
            queue_messages.popleft()
        queue_messages.append(json_data)
        print len(queue_messages)
        for data in queue_messages:
            print data
        return Response(status=200)
    except Exception as e:
        print e.message
        return Response(status=500)

@bp_chat.route('/chat/all', methods=['GET'])
def templateViewAll():
    json_messages = {
        "messages":list(queue_messages)
    }

    return jsonify(json_messages)