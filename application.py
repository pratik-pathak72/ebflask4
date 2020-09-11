from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return "Hello Pratik!"



if __name__ == '__main__':
    application.debug = True
    application.run()
