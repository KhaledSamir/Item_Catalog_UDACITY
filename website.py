
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, ToyShop, ToyItem

app = Flask(__name__)

engine = create_engine('sqlite:///toyshop.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/index/')
def index():
	toyshops = session.query(ToyShop).all()
	return render_template("main.html",toyshops = toyshops)


@app.route('/login/')
def login():

    return render_template('login.html')


@app.route('/new/', methods=['GET', 'POST'])
def new():
	if request.method == 'GET':
		return render_template('newshop.html')
	else:
		newshop = ToyShop(name=request.form['name'],description = request.form['description'])
		session.add(newshop)
		#flash('New Toy Shop %s Successfully Created' % newshop.name)
		session.commit()
		return redirect(url_for('index'))
		


@app.route('/help/')
def help():
	return render_template("help.html")

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
