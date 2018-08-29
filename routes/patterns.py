"""patterns"""

from flask import current_app as app, jsonify, request

from models import Melody, Rhythm, Pattern
from models.utils import Wrapper
from utils.includes import PATTERN_INCLUDES
from utils.rest import expect_json_data, \
                       load_or_404, \
                       login_or_api_key_required

@app.route('/patterns', methods=['POST'])
@login_or_api_key_required
@expect_json_data
def post_pattern():
    melody = Melody.filter_by(intervals=request.json['intervals'])
    if melody.count() == 0:
        melody = Melody(from_dict=request.json)
        Wrapper.check_and_save(melody)
    else:
        melody = melody.first()
    rhythm = Rhythm.filter_by(durations=request.json['durations'])
    if rhythm.count() == 0:
        rhythm = Rhythm(from_dict=request.json)
        Wrapper.check_and_save(rhythm)
    else:
        rhythm = rhythm.first()

    pattern = Pattern.filter_by(melodyId=melody.id, rhythmId=rhythm.id)
    if pattern.count() == 0:
        pattern = Pattern(from_dict=request.json)
    else:
        pattern = pattern.first()

    return jsonify(pattern.asdict(include=PATTERN_INCLUDES)), 201
