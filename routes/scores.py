""" harmonies routes """
from flask import current_app as app, jsonify
#from flask_login import login_required

from models import Score
from utils.includes import SCORE_INCLUDES

@app.route('/scores', methods=['GET'])
#@login_required
def get_scores():
    scores = Score.query.all()
    return jsonify([score.asdict(include=SCORE_INCLUDES)
                    for score in scores]), 200
