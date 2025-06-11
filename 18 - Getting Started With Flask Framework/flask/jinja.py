###building url dynamically
###variable rule
###jinja 2 template engine

### jinja2 temlate engine 
'''
{{ }}expressions to print output in html
{%....%} conditions,for loops
{# #} comments
'''

from flask import Flask, render_template, request,redirect,url_for
'''it creates an instance of the Flask-class
which will be your WSGI(web server gateway interface)application'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>welcome to the flask course</h1></html>"



@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/submit", methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f"hello {name}!"
#     return render_template('form.html')

##variable rule(dynamic routing)
@app.route("/success/<int:score>")
def success(score):
    res="" 
    if score>=50:
        res="passed"
    else:
        res="failed"

    return render_template("result.html",results=res)

##variable rule(dynamic routing)
@app.route("/successres/<int:score>")
def successres(score):
    res="" 
    if score>=50:
        res="passed"
    else:
        res="failed"

    exp={'score':score,'res':res}

    return render_template("result1.html",results=exp)

##if condition
@app.route("/successif/<int:score>")
def successif(score): 

    return render_template("result.html",results=score)

@app.route("/fail/<int:score>")
def fail(score):
    
    
    return render_template("result.html",results=score)

@app.route("/submit",methods=['GET','POST'])
def submit():
    total_score=0
    if request.method == 'POST':
        science=float(request.form['science'])
        math=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])

        total_score=(science+math+c+datascience)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for("successres",score=total_score))

if __name__ == "__main__":
    app.run(debug=True)

 