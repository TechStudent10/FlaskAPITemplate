from flask import Flask
from resources import resource, resource2

app = Flask(__name__)
app.register_blueprint(resource.resource, url_prefix="/resource")
app.register_blueprint(resource2.resource, url_prefix="/resource2")

if __name__ == "__main__":
    app.run(debug=True)
