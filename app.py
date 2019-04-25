import os
from flask import Flask, jsonify, request

app = Flask(__name__)

person2 = {
  "id": 14,
  "name": "John",
  "lastname": "Doe",
  "age": 28,
  "gender": "Male",
  "lucky_numbers": [5, 34, 3, 2, 12]
}

person1 = {
  "id": 5,
  "name": "Jackie",
  "lastname": "Doe",
  "age": 25,
  "gender": "Female",
  "lucky_numbers": [9111, 21, 23, 343, 3]
  }

family = {
  "lastname": "Doe",
  "members": [person1, person2]
    }


@app.route('/', methods=['GET'])
def hello():
  return jsonify(family)

@app.route('/members', methods=['GET'])
def x():
  status_code = 200
  
  abc = family["members"]
  
  lk_nums = []
  for i in abc:
    edf = i["lucky_numbers"]
    for e in edf:
      if lk_nums.count(e) > 1:
        pass
      else:
        lk_nums.append(e)
  
  sum_of_lucky = 0
  for i in abc:
    sum_of_lucky += sum(i["lucky_numbers"])
  
  data = {
    "members": family["members"],
    "family_name": family["lastname"],
    "lucky_numbers": lk_nums,
    "sum_of_lucky": sum_of_lucky
    }
  
  return jsonify(data)


@app.route('/member/<int:id>')
def get_member(id):
  
  y = {"status_code": 200}
  abc = family["members"]
  for i in abc:
    if i["id"]==id:
      return jsonify(y,i)
  x = {
  "status_code": 400,
  "message": "member not found"
  }
  return jsonify(x)
  

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))