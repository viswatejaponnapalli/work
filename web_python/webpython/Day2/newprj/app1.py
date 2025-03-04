from flask import Flask,redirect,render_template
from flask import url_for,request
app=Flask(__name__)
@app.route('/')
def homePage():
    return redirect(url_for('checkflask'))
@app.route('/check')
def checkflask():
    return 'Flask is running fine'
@app.route('/show/<name>/<int:age>')
def show_string(name,age):
    age=age+5
    return f'hello {name}, {age}'
@app.route('/api/data')
def apiData():
    return 'This is AP Interface'
@app.route('/number',methods=['GET','POST'])
def readNum():
    render_template('../templates/form1.html')
    if request.method=='POST':
        if (request.form['num']==''):
            return "<html><body>Invalid Number</body></html>"
        else:
            return num;

if __name__=='__main__':
    app.run()
