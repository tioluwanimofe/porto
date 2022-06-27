from flask_frozen import Freezer
from Server import app


freezer = Freezer(app)


if __name__ == '__main__':
    # Generate the static files using Frozen-Flask
    freezer.freeze()