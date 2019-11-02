# Do customizowania blednych stron (zabias brzydkiego Page not found)

from flask import Blueprint, render_template

#kupa = Blueprint('error_pages', __name__)
error_pages = Blueprint('error_pages', __name__)


#@kupa.app_errorhandler(404) #dekorator do blednych stron
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404

@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 403