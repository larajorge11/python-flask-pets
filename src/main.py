from app import create_app
from app import db
from models import PetSchema
from models import Pet
from flask import request, jsonify

app = create_app()
pet_schema = PetSchema()
pets_schema = PetSchema(many=True)


@app.route("/pets", methods=["POST"])
def create_pet():
    pet_name = request.json["pet_name"]
    age = request.json["age"]
    gender = request.json["gender"]

    pet = Pet(pet_name, age, gender)
    db.session.flush()
    db.session.add(pet)
    db.session.commit()

    return pet_schema.jsonify(pet)


@app.route("/pets", methods=["GET"])
def get_pets_details():
    all_pets = Pet.query.all()
    result = pets_schema.dump(all_pets)
    return jsonify(result)


@app.route("/pets/<id>", methods=["GET"])
def get_pet_details(id):
    pet = Pet.query.get(id)
    return pet_schema.jsonify(pet)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
