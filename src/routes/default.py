from flask import Blueprint, redirect;

default_page = Blueprint('default_page', __name__)
@default_page.route('/')
def page_content():
    return "Social Network Analysis Backend"
