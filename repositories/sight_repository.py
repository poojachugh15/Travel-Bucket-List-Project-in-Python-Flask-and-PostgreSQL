from db.run_sql import run_sql

from models.country import Country
from models.city import City
from models.sight import Sight

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository


def save(sight):
    sql = "INSERT INTO sights (name, city_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [sight.name, sight.city.id, sight.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight


def select_all():
    sights = []
    
    sql = "SELECT * FROM sights"
    results = run_sql(sql)
    
    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row["name"], city,  row["visited"], row["id"])
        sights.append(sight)
    return sights


def select(id):
    sights = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        sights = Sight(result['name'], result['id'])
    return sights


def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)