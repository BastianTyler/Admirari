from flask import Blueprint, render_template

tv_bp = Blueprint('text_venture', __name__, url_prefix='/text_venture')

@tv_bp.route('/tv_home')
def tv_home():
    return render_template('text_venture/tv_home.html')

@tv_bp.route('/tv_about')
def tv_about():
    return render_template('text_venture/tv_about.html')

@tv_bp.route('/tv_day_one')
def tv_day_one():
    return render_template('text_venture/tv_day_one.html')

@tv_bp.route('/tv_day_two')
def tv_day_two():
    return render_template('text_venture/tv_day_two.html')

@tv_bp.route('/tv_day_three')
def tv_day_three():
    return render_template('text_venture/tv_day_three.html')

@tv_bp.route('/tv_day_four')
def tv_day_four():
    return render_template('text_venture/tv_day_four.html')

@tv_bp.route('/tv_day_five')
def tv_day_five():
    return render_template('text_venture/tv_day_five.html')

@tv_bp.route('/tv_day_six')
def tv_day_six():
    return render_template('text_venture/tv_day_six.html')


@tv_bp.route('/github_workshop')
def github_workshop():
    return render_template('text_venture/github_workshop.html')
