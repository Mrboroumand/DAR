from flask import Flask , render_template , redirect , request
import playsound 


app = Flask(__name__)

@app.route("/")
def home():
    return "DAR is runing"






if __name__=='__main__':
    app.run(host="0.0.0.0",port=443)