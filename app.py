from flask import Flask
from flask import render_template , request, redirect, session
from database import get_all_cats, get_cat_by_id,create_cat, add_vote

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_page(id):
	cats = get_cat_by_id(id)
	return render_template("cat.html", cat=cats)

@app.route('/vote_cat/<int:id>', methods=['POST'])
def vote(id):
	add_vote(id)
	return redirect("/")

@app.route('/add_cat', methods=["GET","POST"])
def create_cats():
	if request.method == 'GET':
		return render_template("add_cat.html")
	else:
		name = request.form["name"]
		create_cat(name)
		return redirect("/")

if __name__ == '__main__':
   app.run(debug = True)
