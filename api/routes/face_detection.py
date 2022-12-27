from flask_restful import Resource, Api, reqparse
from flask import request
import cv2



api = Api()
parser = reqparse.RequestParser()
parser.add_argument('images')


class FaceDetection(Resource):
    def get(self):
        return {'hello':'testing'}


    def post(self):
        element = parser.parse_args()
        path = r'{}'.format(element['images'])
        print(path)
        img = cv2.imread(path)
        filename = 'savedImage.jpg'
        cv2.imwrite(filename, img)
        return element, 200

api.add_resource(FaceDetection, '/')