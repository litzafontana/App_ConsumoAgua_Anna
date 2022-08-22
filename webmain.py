
    from flask import Flask, Render_template, Response
    from face import VideoCamera
      #main.py
    #import the necessary packges
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')
