""" staff voices """
from flask import current_app as app, jsonify, request

from models import StaffVoice
from models.utils import Wrapper
from utils.includes import STAFF_VOICE_INCLUDES
from utils.rest import expect_json_data, \
    load_or_404, \
    login_or_api_key_required

@app.route('/staffVoices/<id>', methods=['PATCH'])
@login_or_api_key_required
@expect_json_data
def patch_staff_voice(id):
    staff_voice = load_or_404(StaffVoice, id)
    staff_voice.populateFromDict(request.json)
    Wrapper.check_and_save(staff_voice)
    return jsonify(staff_voice.asdict(includes=STAFF_VOICE_INCLUDES)), 200
