from flask import Flask,render_template,request
import math
from Email_Security import *
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def welcome():
    if request.method=="GET":
        return render_template("text.html")
    txt=request.form.get("txt","World")
    key=int(request.form.get("key","00"))
    if request.form.get("action")=="enc":
        encTxt=encrypt(txt,key)
        enc=True
        finalTxt=encTxt
    else:
        txt=txt.split(';')
        x=math.sqrt(len(txt))
        xtxt=[[]]*x
        k=0
        for i in range(x):
            for j in range(x):
                xtxt[i][j]=txt[k]
        decTxt=decrypt(txt,key)
        enc=False
        finalTxt=decTxt
    return render_template("welcome.html",txt=finalTxt,enc=enc)