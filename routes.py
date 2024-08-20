from resources.example import ExampleResource


def register_routes(api):
    api.add_resource(ExampleResource, "/example")