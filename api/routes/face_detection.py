from flask_restful import Resource, Api, reqparse
from flask import request
import werkzeug
from werkzeug.utils import secure_filename
import os




api = Api()
parser = reqparse.RequestParser()
parser.add_argument('images', type=werkzeug.datastructures.FileStorage, location='files')


class FaceDetection(Resource):
    def get(self):
        return {'hello':'testing'}


    def post(self):
        element = parser.parse_args()
        image = element["images"]
        image.save("testing.jpg")
        return 'hi there', 200

api.add_resource(FaceDetection, '/')