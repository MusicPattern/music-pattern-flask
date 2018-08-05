""" error handlers """
import re
import simplejson as json
from sqlalchemy.exc import IntegrityError
import traceback
from flask import current_app as app, jsonify

from models.api_errors import ApiErrors


@app.errorhandler(ApiErrors)
def restize_api_errors(e):
    print(json.dumps(e.errors))
    return jsonify(e.errors), e.status_code or 400


def something_went_wrong(e):
    print("UNHANDLED ERROR : ")
    traceback.print_exc()
    return "An error happened. This will be investigated the sooner.", 500


@app.errorhandler(ValueError)
def restize_value_error(e):
    if len(e.args)>1 and e.args[1] == 'enum':
        return json.dumps([{e.args[2]: ' must be in this list : '+",".join(map(lambda x : '"'+x+'"', e.args[3]))}]), 400
    else:
        return something_went_wrong(e)


@app.errorhandler(TypeError)
def restize_type_error(e):
    if e.args and len(e.args)>1 and e.args[1] == 'geography':
        return json.dumps([{e.args[2]: 'must be a list of decimals like : [2.22, 3.22]'}]), 400
    elif e.args and len(e.args)>1 and e.args[1] and e.args[1]=='decimal':
        return json.dumps([{e.args[2]: 'must be a decimal number'}]), 400
    elif e.args and len(e.args)>1 and e.args[1] and e.args[1]=='integer':
        return json.dumps([{e.args[2]: 'must be an integer'}]), 400
    else:
        return something_went_wrong(e)


@app.errorhandler(IntegrityError)
def restize_integrity_error(e):
    if hasattr(e, 'orig') and hasattr(e.orig, 'pgcode') and e.orig.pgcode=='23505':
        field = re.search('Key \((.*?)\)=', str(e._message), re.IGNORECASE).group(1)
        return json.dumps([{field: 'this identifier exists already in our database'}]), 400
    elif hasattr(e, 'orig') and hasattr(e.orig, 'pgcode') and e.orig.pgcode=='23503':
        field = re.search('Key \((.*?)\)=', str(e._message), re.IGNORECASE).group(1)
        return json.dumps([{field: 'could not find an object associated with this identifier'}]), 400
    elif hasattr(e, 'orig') and hasattr(e.orig, 'pgcode') and e.orig.pgcode=='23502':
        field = re.search('column "(.*?)"', e.orig.pgerror, re.IGNORECASE).group(1)
        return json.dumps([{field: 'this field is needed'}]), 400
    else:
        return something_went_wrong(e)
