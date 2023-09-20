from flask import Flask, render_template
from src.blueprint import blp_index


def create_app():
    app = Flask(
        __name__,
        template_folder="src/interface/templates",
        static_folder="src/interface/static",
        instance_relative_config=True
    )
    app.config.from_object("config.development")
    app.config.from_pyfile("config.py")
    app.secret_key = "super secret key"
    app.register_blueprint(blp_index)
    
    return app
    

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")
