from flask import Flask, render_template

app = Flask("My Web App")

@app.route("/")
def hello_world():
    print("Rendering index.html template")
    return render_template("index.html")

@app.route("/customers")
def customers():
    return "My customer are: ..."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
