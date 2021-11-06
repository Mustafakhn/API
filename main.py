import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

user_details = [
    {
        "name": "Mustafa",
        "City": "Bhopal"
    },
    {
        "name": "Imran",
        "City": "SG"
    }
]


@app.route('/getdata/all', methods=['GET'])
def get_data():
    return jsonify(user_details), 200


@app.route('/getdata/name/<name>', methods=['GET'])
def get_data_user(name):
    print("User has provided value: {}".format(name))
    for item in user_details:
        print(item)
        if item["name"] == name:
            print(item)
            return jsonify(item), 200


@app.route('/getdata/username', methods=['GET'])
def get_user_param():
    print(request.args)
    return jsonify(request.args), 200

    # print("User has provided value: {}".format(name))


@app.route('/getdata/name/<name>/<city>', methods=['POST'])
def post_data_user(name, city):
    print("User has provided value: {}".format(name, city))
    userinput = {"name": name, "CITY": city}
    user_details.append(userinput)
    return jsonify(user_details), 200


@app.route('/getdata/adduser', methods=['POST'])
def add_user():
    name = request.args.get('name')
    city = request.args.get('city')
    age = request.args.get('age')
    hobby = request.args.get('hobby')
    car = request.args.get('car')

    user_input_dict = {"name": name,
                       "city": city,
                       "age": age,
                       "hobby": hobby,
                       "car": car
                       }

    # print("User has provided value: {}".format(name, city))
    # user_input_dict = {"name": name, "CITY": city}
    user_details.append(user_input_dict)
    return jsonify(user_details), 200


if __name__ == '__main__':
    print("Starting server")
    app.run()
