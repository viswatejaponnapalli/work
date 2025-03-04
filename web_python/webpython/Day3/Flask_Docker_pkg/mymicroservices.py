from flask import Flask,jsonify
import random 
app = Flask(__name__)
@app.route("/number",methods=['GET'])
def semd_a_nummber():
    number=random.randint(1,20)
    return jsonify({"number":number})
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=7000)