from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City
from models.sight import Sight
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

sight_blueprint = Blueprint("sights", __name__)

@sight_blueprint.route('/')
def index():
    return render_template('index.html')

@sight_blueprint.route('/countries/cities/sights', methods=['GET'])
def all_sights():
    all_sights = sight_repository.select_all()
    return render_template('sights/index.html', all_sights=all_sights)