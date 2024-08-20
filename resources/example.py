from flask_restful import Resource, marshal_with, abort

from fields import example_fields


class ExampleResource(Resource):
    @marshal_with(example_fields)
    def get(self):
        return {"id": "1", "name": "example"}
