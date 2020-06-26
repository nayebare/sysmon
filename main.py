from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import psutil, back

app = Flask(__name__)

# rendering the HTML page which has the button
@app.route("/")
def json():
    retndata = back.GetOSUnameData()
    systarry = back.RecognizeSystem()
    return render_template("main.html", retndata=retndata, systarry=systarry)

# background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"

@app.route('/_stuff', methods= ['GET'])
def stuff():
    cpu=str(psutil.cpu_freq(True))
    return jsonify(cpu=cpu)

@app.route("/virtdata", methods=["GET"])
def virtdata():
    retndata = back.GetVirtualMemoryData()
    retnjson = jsonify(virttomr=retndata["Total"],
                       virtavbl=retndata["Available"],
                       virtperc=retndata["Percent"],
                       virtused=retndata["Used"],
                       virtactv=retndata["Active"],
                       virtbufr=retndata["Buffers"],
                       virtcach=retndata["Cached"],
                       virtshrd=retndata["Shared"],
                       virtslab=retndata["Slab"])
    return retnjson

if __name__ == "__main__":
    app.run(port=9696, host="0.0.0.0")