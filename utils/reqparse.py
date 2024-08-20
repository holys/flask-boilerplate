from flask_restful.reqparse import RequestParser as _RequestParser


class RequestParser(_RequestParser):
    def get_argument(self, name, **kwargs):
        self.add_argument(name, **kwargs)
        args = self.parse_args()
        return args.get(name, None)
