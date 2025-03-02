from flask import Blueprint, render_template

physics_bp = Blueprint('physics', __name__, url_prefix='/physics')

@physics_bp.route('/thermodynamics')
def thermodynamics():
    return render_template('physics/thermodynamics.html')