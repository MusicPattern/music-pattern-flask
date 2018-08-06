""" harmonies routes """
from flask import current_app as app, jsonify
#from flask_login import login_required

from models import Harmony
from utils.includes import HARMONY_INCLUDES

@app.route('/harmonies', methods=['GET'])
#@login_required
def get_harmonies():
    harmonies = Harmony.query.all()
    return jsonify([harmony.asdict(include=HARMONY_INCLUDES)
                    for harmony in harmonies]), 200
