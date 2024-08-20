from flask_restful import fields

example_fields = {
    "id": fields.String(attribute="id"),
    "name": fields.String(attribute="name"),
}
