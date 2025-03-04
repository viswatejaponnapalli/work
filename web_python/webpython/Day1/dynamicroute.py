from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/hello/<name>')
# def welcome(name):
#     return 'welcome %s' %name
def hello_dyna_service():
    #return "Welcome to microservices-a simple message"
    return 'Welcome : (name)'
if __name__=="__main__":
    app.run(port=6000)