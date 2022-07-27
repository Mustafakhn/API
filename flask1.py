import flask
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

data = [
    {
        'name': 'mustafa',
        'age': '21',
        'area': 'khanugaon'
    },
    {
        'name': 'tayyaba',
        'age': '20',
        'area': 'koh-e-fiza'
    },
    {
        'name': 'ibraheem',
        'age': '16',
        'area': 'koh-e-fiza'
    },
    {
        'name': 'yousuf',
        'age': '11',
        'area': 'mumbai'
    }
]

@app.route('/data/users', methods=['GET'])  # methods go here
def data_user():
    return jsonify(data), 200  # return data and 200 OK code


@app.route('/data/users/<area>', methods=['GET'])  # methods go here
def data_users_area(area):
    for item in data:
        temp_list = []
        if item["area"] == area:
            temp_list.append(item)
            print(request.args)
            return jsonify(temp_list), 200


@app.route('/data/<name>', methods=['GET'])
def get_users_name(name):
    for inp in data:
        if inp['name'] == name:
            print(request.args)
            return jsonify(inp), 200


@app.route('/data/class/<classes>', methods=['POST'])
def post_data(classes):
    input = {"classes": classes}
    data.append(input)
    return jsonify(input), 200

@app.route('/data/class/', methods=['POST'])
def post_data_new():
    new_user = {"name": request.args.get('name'),
                "area": request.args.get('area'),
                "age": request.args.get('age')
                    }
    print("new_user", new_user)
    data.append(new_user)
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(port=5002)  # run our Flask app
