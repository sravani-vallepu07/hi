from flask import Flask
'''it creates an instance of the Flask-class
which will be your WSGI(web server gateway interface)application'''

app=Flask(__name__)
@app.route("/")
def welcome():
    return "haha haha Welcome to the best Flask course. This should be an amazing course.hi"

@app.route("/index")
def index():
    return " Welcome to the index pageuuuds"
if __name__=="__main__":
    app.run()

    # Make sure to save the file after making changes and restart the Flask server.
    # Flask does not automatically detect changes in the code unless the server is restarted.
    # No additional code is needed at the placeholder. The script is complete and functional as is.
