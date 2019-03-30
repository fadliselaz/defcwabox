from flask import Flask, render_template, url_for, request

app = Flask(__name__)
userState = ["fadliselaz@gmail.com", "yunipratiwi@gmail.com"]
passState = ["fadliselaz13", "1"]

@app.route("/", methods=["GET","POST"])
def index():
    salah = True
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in userState and password in passState:
            login = True
            return render_template("mainPage.html", login=login, username=username)

        else:
            return render_template("index.html", salah=salah)


    return render_template("index.html")



@app.route("/send", methods=["GET","POST"])
def send():
    sn = ""
    if request.method == "POST":
        #grab from from
        waNumber = request.form.get("waNumber")
        message = request.form.get("message")
        contact = request.form.get("contact")
        urlLink = request.form.get("urlLink")
        UrlImage = request.form.get("UrlImage")
        title = request.form.get("title")

        print(waNumber, message, contact, urlLink, UrlImage, title)
        sn = contact
        return render_template("mainPage.html", sn=sn, login=True)

    return render_template("mainPage.html")



if __name__ == "__main__":
    app.run(debug=True, port=8080)
