from . import app
from flask import jsonify

from src.constants.http_status_codes import HTTP_404_NOT_FOUND

# Route imports
from src.routes.default import default_page
from src.routes.ergm import ergm_page
from src.routes.graph_stats import graph_stats_page


# Register Routes
app.register_blueprint(default_page)
app.register_blueprint(ergm_page)
app.register_blueprint(graph_stats_page)


@app.errorhandler(HTTP_404_NOT_FOUND)
def handle_404(e):
    return jsonify({
        'error': 'API Not found'
    }), HTTP_404_NOT_FOUND

# @app.before_request
# def before():
    # Things to be done before pre-processing
