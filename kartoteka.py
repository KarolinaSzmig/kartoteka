from flask import Flask, render_template, request

kartoteka = Flask(__name__)


@kartoteka.route("/", methods=["get", "post"])
def clinicalData():
    if request.method == 'GET':
        enable = False
        if request.form['mode'] == "writing":
            enable = True
            return render_template("data.html", enable=enable)
        else:
            return render_template("data.html", enable=enable)


    else:
        return 'yay'


    



