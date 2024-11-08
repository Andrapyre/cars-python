from flask import Response, request
from app import app
import json
from uuid import uuid4


@app.route("/customers/<customer_id>/cars", methods=["POST"])
def create_car(customer_id):
    car = {
        "id": str(uuid4()),
        "customerId": customer_id,
        "model": "Jetta",
        "make": "VW",
        "producedIn": 2018,
    }

    json_response = json.dumps(car)
    return Response(json_response, mimetype="application/json")


@app.route("/customers/<customer_id>/cars/<car_id>", methods=["DELETE", "GET", "PATCH"])
def handle_car_request_with_id(customer_id, car_id):
    if request.method == "DELETE":
        return __delete_car(customer_id, car_id)
    elif request.method == "GET":
        return __get_car(customer_id, car_id)
    else:
        return __update_car(customer_id, car_id)


def __delete_car(customer_id, car_id):
    return Response(mimetype="application/json", status=204)


def __get_car(customer_id, car_id):
    car = {
        "id": car_id,
        "customerId": customer_id,
        "model": "Jetta",
        "make": "VW",
        "producedIn": 2018,
    }

    json_response = json.dumps(car)
    return Response(json_response, mimetype="application/json")


def __update_car(customer_id, car_id):
    car = {
        "id": car_id,
        "customerId": customer_id,
        "model": "Jetta",
        "make": "VW",
        "producedIn": 2018,
    }

    json_response = json.dumps(car)
    return Response(json_response, mimetype="application/json")
