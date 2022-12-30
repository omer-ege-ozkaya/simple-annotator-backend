from flask import Flask, request, jsonify
import mongodb_handler, json, uuid
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/annotations/list', methods=['GET'])
def list_annotations():
    list_of_annotations = mongodb_handler.get_list_of_annotations()
    json_list_of_annotations = json.dumps(list_of_annotations)
    return json_list_of_annotations


@app.route('/annotations', methods=['GET'])
def get_annotation():
    annotation_id = request.args.get("id")
    annotation_id = "http://localhost:8081/annotations?id=" + annotation_id
    annotation = mongodb_handler.get_annotation(annotation_id)
    return jsonify(annotation), 200


@app.route('/annotations', methods=['POST'])
def set_annotation():
    annotation = dict(request.json)
    if "id" not in annotation or annotation["id"] is None:
        annotation["id"] = "http://localhost:8081/annotations?id=" + uuid.uuid4().hex
    mongodb_handler.upsert_annotation(annotation["id"], annotation)
    annotation = mongodb_handler.get_annotation(annotation["_id"])
    return jsonify(annotation), 200


@app.route('/annotations', methods=['DELETE'])
def delete_annotation():
    pass


if __name__ == '__main__':
    app.run("0.0.0.0", 8081)
