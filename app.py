from flask import Flask, jsonify, request
from datastructure import Family

app = Flask(__name__)

jacksonFamily=Family('Jackson')

@app.route("/member",methods=["GET"])
def all_members():
    return jsonify(jacksonFamily.get_all_members()),200

@app.route("/member/add",methods=["POST"])
def add_member():
    if request.json.get("first_name")==None:
        return jsonify({
            'error':'member must have a first name'
        }),400
    elif request.json.get("lucky_numbers")==None:
        return jsonify({
            'error':'member must have lucky numbers'
        }),400
    elif request.json.get("age")==None or request.json.get('age')<0:
        return jsonify({
            'error':'member must have a natural age'
        }),400
    else:
        new_member={
        "first_name":request.json.get('first_name'),
        "age":request.json.get('age'),
        "lucky_numbers":request.json.get('lucky_numbers')
        }
        jacksonFamily.add_member(new_member)
        return jsonify({
            'msg':'member added succesfully'
        }),201
    
@app.route("/member/<int:member_id>",methods=['GET'])
def get_single_member(member_id):
    if not any(member["id"]==member_id for member in jacksonFamily._members):
        return jsonify({
            'error':'no member found'
        }),404
    
    else:
        found = jacksonFamily.get_member(member_id) 
        return jsonify({
        "data":found
        })

@app.route("/member/delete/<int:member_id>",methods=['DELETE'])
def delete_member(member_id):
    if any(member["id"]==member_id for member in jacksonFamily._members)==False:
        return jsonify({
            'error':'no member found'
        }),404
    jacksonFamily.delete_member(member_id)
    return jsonify({
        "msg":"user deleted succesfully"
    })


    

if __name__ == '__main__':
    app.run(host="localhost", port=5000)