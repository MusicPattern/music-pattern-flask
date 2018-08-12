""" scores routes """
from flask_login import login_required, current_user
from flask import current_app as app, jsonify

from models import RoleType, Score
from utils.includes import SCORE_INCLUDES
from utils.rest import load_or_404

@app.route('/scores', methods=['GET'])
@login_required
def get_scores():
    query = Score.query
    if RoleType.admin not in [role.type for role in current_user.roles]:
        query = query.filter_by(userId=current_user.id)
    scores = query.all()
    return jsonify([score.asdict(includes=SCORE_INCLUDES)
                    for score in scores]), 200

@app.route('/scores/<id>', methods=['GET'])
@login_required
def get_score(id):
    score = load_or_404(Score, id)
    return jsonify(score.asdict(includes=SCORE_INCLUDES)), 200
