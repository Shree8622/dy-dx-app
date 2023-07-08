from flask import Flask,render_template,request,send_file
from api.logic import api_dy
app = Flask(__name__,static_folder='static')
import os
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/diff', methods = ['POST'])  
def diff():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(os.path.dirname(__file__)+'\\static\\data.csv')

        api_dy() #calls the function written in logic to calculate derivative
        
        return render_template("derivative.html", name = f.filename)
    
@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = os.path.dirname(__file__)+'\\static\\dy-result.csv'
    return send_file(path, as_attachment=True)

if __name__ ==  "__main__":
    app.run()

def sample_func():
    print("this function was called")