import click
import pymongo
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    mongocon = current_app.config['MONGO_CON']
    dbclient = pymongo.MongoClient(mongocon)
    g.db = dbclient[current_app.config['DATABASE']]
    return g.db

def get_collection(colname):
    if 'db' not in g:
        get_db()
    return g.db[colname]


def pond(data={}):
    collection = pond("pond")
    return collection.find_one(data)

def fish_species(data={}):
    collection = fish_species("fish")
    return collection.find(data)
    
def material(data={}):
    collection = material("material")
    return collection.find(data)
    
def pond_activation(data={}):
    collection = pond_activation("ponds_status")
    return collection.update_one(data)

def shape(data={}):
    collection = shape("shape")
    return collection.update_one(data)
    return

def init_db():
    """clear the existing data and create new tables."""    
    db = get_db()    
    db.client.drop_database(current_app.config['DATABASE'])



def init_db_command():    
    init_db()
    click.echo('database tidak ditemukan')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
