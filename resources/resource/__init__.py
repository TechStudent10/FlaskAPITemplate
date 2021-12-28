from flask import Blueprint, jsonify

resource = Blueprint('resource', __name__)

@resource.route('/')
def index():
    title = "Resource"
    routes = [
        '<li>/: this<li/>',
        '<li>/hi: hello</li>'
    ]
    return "\n".join([f"<h1>{title}</h1>", "<ul>", '\n'.join(routes), "</ul>"])

@resource.route('/hi')
def hi():
    return jsonify(msg="Hi")
