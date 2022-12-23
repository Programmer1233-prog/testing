from flask_restful import Resource, Api, reqparse
from flask import request

api = Api()
parser = reqparse.RequestParser()
parser.add_argument('images')


class FaceDetection(Resource):
    def get(self):
        return {'hello':'testing'}


    def post(self):
        element = parser.parse_args()
        print(element)
        return element, 200

api.add_resource(FaceDetection, '/')