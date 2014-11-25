__author__ = 'Nalon'

from flask import Blueprint

bp_teste = Blueprint('bp_teste',__name__)

@bp_teste.route('/teste')
def isWork():
    return 'GPS-BUS ENGINE WORKING!'
