from flask import Response, request
from app import app
import json


@app.route("/customers", methods=["POST"])
def create_customer():
    customer = {
        "id": 2,
        "firstName": "John",
        "lastName": "Smith",
        "city": "Los Angeles",
        "country": "USA",
        "email": "sample@email.com",
        "apiKey": "7E6C353555C640FD80643925FB54E046",
    }

    json_response = json.dumps(customer)
    return Response(json_response, mimetype="application/json")


@app.route("/customers/<customer_id>", methods=["DELETE", "GET", "PATCH"])
def handle_customer_request_with_id(customer_id):
    if request.method == "DELETE":
        return __delete_customer(customer_id)
    elif request.method == "GET":
        return __get_customer(customer_id)
    else:
        return __update_customer(customer_id)


def __delete_customer(customer_id):
    return Response(mimetype="application/json", status=204)


def __get_customer(customer_id):
    customer = {
        "id": customer_id,
        "firstName": "John",
        "lastName": "Smith",
        "city": "Los Angeles",
        "country": "USA",
        "email": "sample@email.com",
        "apiKey": "7E6C353555C640FD80643925FB54E046",
    }

    json_response = json.dumps(customer)
    return Response(json_response, mimetype="application/json")


def __update_customer(customer_id):
    customer = {
        "id": customer_id,
        "firstName": "John",
        "lastName": "Smith",
        "city": "Los Angeles",
        "country": "USA",
        "email": "sample@email.com",
        "apiKey": "7E6C353555C640FD80643925FB54E046",
    }

    json_response = json.dumps(customer)
    return Response(json_response, mimetype="application/json")
