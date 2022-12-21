from flask import Flask, Response, request, jsonify
from flask import render_template
from datetime import datetime
import json
from studentcontact_resources import StudentContactResource

# from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/api/students/<uni>", methods=["GET"])
def get_studentcontact_by_uni(uni):
    result = StudentContactResource.get_by_key(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/students/addcontact", methods=["GET", "POST"])
def add_studentcontact():
    json_data = request.get_json()
    uni = json_data["uni"]
    contact_name = json_data["contact_name"]
    email = json_data["email"]
    tele = json_data["tele"]
    print(uni, contact_name, email, tele)

    result = StudentContactResource.add_user(uni, contact_name, email, tele)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(debug=True)