import time

from flask import Flask, request, g
from pyinstrument import Profiler

from models import db
from resources import api
from routes import register_routes
from config import CONFIG, is_develop_env
from flask_cors import CORS


def print_app_config(app):
    if not is_develop_env():
        return
    print("Flask App Configuration:")
    for key in app.config:
        print(f"{key} = {app.config[key]}")


app = Flask(__name__)


def init_app():
    app.config.from_object(CONFIG)
    # 开发环境下允许跨域
    if is_develop_env():
        CORS(app, supports_credentials=True)

    db.init_app(app)
    register_routes(api)
    api.init_app(app)

    with app.app_context():
        db.create_all()

    print_app_config(app)


@app.before_request
def before_request():
    request.start_time = time.time()
    if is_develop_env() and "profile" in request.args:
        g.profiler = Profiler()
        g.profiler.start()


@app.after_request
def after_request(response):
    end_time = time.time()
    elapsed_time = end_time - request.start_time
    app.logger.info(
        f"{request.remote_addr} - - "
        f'"{request.method} {request.path} {request.environ["SERVER_PROTOCOL"]}" '
        f"{response.status_code} - "
        f"{elapsed_time * 1000:.6f}ms"
    )

    if not hasattr(g, "profiler"):
        return response
    g.profiler.stop()
    g.profiler.open_in_browser()

    return response


# 适配 gunicorn 方式部署，因为 gunicorn 不会调用 main
init_app()


def main(port=None):
    if port is None:
        port = 6000

    app.run(host="0.0.0.0", port=port, debug=CONFIG.DEBUG)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        main(int(sys.argv[1]))
    else:
        main()
