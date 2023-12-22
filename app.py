import io
import os
from flask import Flask,render_template,request,send_file
import json
from Email_Security import *
app=Flask(__name__)

def writeEncText(fname,text):
    encMatrix=dict()
    for i in range(len(text)):
        encMatrix["row"+str(i)]=dict()
        for j in range(len(text[i])):
            encMatrix["row"+str(i)]["col"+str(j)]=text[i][j]
    with open(fname,'w') as fObj:
        json.dump(encMatrix,fObj)

@app.route('/',methods=["GET","POST"])
def welcome():
    if request.method=="GET":
        return render_template("text.html")
    txt=request.form.get("txt","World")
    key=int(request.form.get("key","00"))
    if request.form.get("action")=="enc":
        encTxt=encrypt(txt,key)
        finalTxt=encTxt
        fname=request.form.get("fname")+".json"
        writeEncText(fname,encTxt)
        txt=io.BytesIO()
        with open(fname,'rb') as fObj:
            txt.write(fObj.read())
        txt.seek(0)
        os.remove(fname)
        return send_file(txt,mimetype="application/json",download_name=fname,as_attachment=True)
    else:
        txt=json.loads(request.files.get("txt").read())
        tmparr=[]
        for i in txt.values():
            tmparr.append(list(i.values()))
        for i in range(len(tmparr)):
            for j in range(len(tmparr[i])):
                tmparr[i][j]=int(tmparr[i][j])
        txt=tmparr
        decTxt=decrypt(txt,key)
        finalTxt=decTxt
    return render_template("text.html",txt=finalTxt,enc=True)
if __name__=="__main__":
    app.run()
