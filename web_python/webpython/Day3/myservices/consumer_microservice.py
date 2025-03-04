from flask import Flask,jsonify
import requests
app=Flask(__name__)
mymicroservice_url="http:..127.0.0.1:8001/number"
def call_send_a_number():
    response=requests.get(mymicroservice_url)
    return response.json().get("number")
@app.route("/check",methods=['GET'])
def check_data():
    my_number=call_send_a_number();
    return jsonify({"number_recd" : my_number})
if __name__=="__main__":
    app.run(port=8001)