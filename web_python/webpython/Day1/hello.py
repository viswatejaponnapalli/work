from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/hello',methods=['GET','POST'])
# def welcome(name):
#     return 'welcome %s' %name
def hello_microservice():
    return "Welcome to microservices-a simple message"
    return jsonify(message)
if __name__=="__main__":
    app.run(port=5000)