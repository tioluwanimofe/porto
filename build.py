from flask_frozen import Freezer
from Server import app


app = create_app()

freezer = Freezer(app)


if __name__ == '__main__':
    
    freezer.freeze()
