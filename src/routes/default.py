from flask import Blueprint, redirect
from flask_cors import cross_origin

default_page = Blueprint('default_page', __name__)
@default_page.route('/')
@cross_origin()
def page_content():
    return "Social Network Analysis Backend"
