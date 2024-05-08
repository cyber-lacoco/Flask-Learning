from flask import Flask, render_template
app = Flask(__name__)

JOBS = [
    {
        "id":"1",
        "Title":"Data Analyst",
        "location":"Ikeja, Lagos",
        "salary":"200k",
    },
    {
        "id":"2",
        "Title":"Data Engineer",
        "location":"Ikeja, Lagos",
        "salary":"300k",
    }
]

@app.route("/")
def home():
    return render_template("index.html", jobs=JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
