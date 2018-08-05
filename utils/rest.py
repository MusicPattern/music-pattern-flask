""" rest """
from functools import wraps
from flask_login import current_user
from flask import jsonify, request

from utils.human_ids import dehumanize

def expect_json_data(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if request.json is None:
            return "JSON data expected", 400
        return f(*args, **kwds)
    return wrapper

def handle_rest_get_list(modelClass, query=None,
                         refine=None, order_by=None, flask_request=None,
                         include=None, resolve=None, print_elements=None,
                         paginate=None, page=None):
    if flask_request is None:
        flask_request = request
    if query is None:
        query = modelClass.query
    # DELETED
    if hasattr(modelClass, 'deleted'):
        query = query.filter_by(deleted=False)
    # REFINE
    if refine:
        query = refine(query)
    # ORDER BY
    if order_by:
        try:
            order_by = [order_by] if not isinstance(order_by, list)\
                       else order_by
            query = query.order_by(*order_by)
        except ProgrammingError as e:
            field = re.search('column "?(.*?)"? does not exist', e._message, re.IGNORECASE)
            if field:
                errors = ApiErrors()
                errors.addError('order_by', 'order_by value references an unknown field : '+field.group(1))
                raise errors
            else:
                raise e
    # PAGINATE
    if paginate:
        if page is not None:
            page = int(page)
        query = query.paginate(page, per_page=paginate, error_out=False)\
                     .items
    # DICTIFY
    elements = [o.asdict(include=include, resolve=resolve) for o in query]
    # PRINT
    if print_elements:
        print(elements)
    # RETURN
    return jsonify(elements), 200

def load_or_404(obj_class, human_id):
    return obj_class.query.filter_by(id=dehumanize(human_id))\
                          .first_or_404()

def login_or_api_key_required(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if not current_user.is_authenticated:
            return "API key or login required", 403
        return f(*args, **kwds)
    return wrapper
