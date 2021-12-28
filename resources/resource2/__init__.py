from flask import Blueprint, jsonify

resource = Blueprint('resource2', __name__)

@resource.route('/')
def index():
    title = "Resource 2"
    routes = [
        '<li>/: this<li/>',
        '<li>/bye: bye</li>'
    ]
    return "\n".join([f"<h1>{title}</h1>", "<ul>", '\n'.join(routes), "</ul>"])

@resource.route('/bye')
def bye():
    return jsonify(msg="bye")
