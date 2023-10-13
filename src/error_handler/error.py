from flask import Blueprint, make_response

handle_err = Blueprint('errors', __name__)

@handle_err.app_errorhandler(500)
def application_error(e):
    return make_response('Sorry, there is an application error!', 500)

@handle_err.app_errorhandler(404)
def token_expired_exception(e):
    return make_response('This is not a valid URL, please check for any spelling mistakes!', 404)

@handle_err.app_errorhandler(405)
def token_expired_exception(e):
    return make_response('The method is not allowed for the given URL!', 405)

@handle_err.app_errorhandler(Exception)
def error_handler(e):
    return make_response('An error occurred in the application!', 500)








