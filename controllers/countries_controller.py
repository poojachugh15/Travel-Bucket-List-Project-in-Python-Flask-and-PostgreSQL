from flask import Flask, render_template, Blueprint, request, redirect, url_for

from models.country import Country
import repositories.country_repository as country_repository

country_blueprint = Blueprint("countries", __name__)

# INDEX
@country_blueprint.route('/')
def index():
    return render_template('index.html')

@country_blueprint.route('/countries', methods=['GET'])
def all_countries():
    all_countries = country_repository.select_all()
    return render_template('/countries/index.html', all_countries=all_countries)

# NEW
@country_blueprint.route('/countries/new', methods=['GET'])
def new_country():
    return render_template('/countries/new.html')

# CREATE
@country_blueprint.route('/countries', methods=['POST'])
def create_country():
    name = request.form["name"]
    visited = request.form["visited"]
    country = Country(name, visited)
    country_repository.save(country)
    return redirect("/countries")

# SHOW
@country_blueprint.route('/countries/<id>/show')
def show_country(id):
    country = country_repository.select(id)
    return render_template('/countries/show.html', country=country)


# EDIT
@country_blueprint.route('/countries/<id>/edit', methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('/countries/edit.html', country=country)

# UPDATE
@country_blueprint.route('/countries/<id>', methods=['POST'])
def update_country(id):
    country = country_repository.select(id)
    country.name = request.form["name"]
    country.visited = request.form["visited"]
    country_repository.update(country)
    return redirect ('/countries')
    
    
# DELETE

@country_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete(id):
    country_repository.delete(id)
    return redirect("/countries")