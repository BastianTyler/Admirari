from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/fun_with_sine_waves_and_shapes')
def fun_with_sine_waves_and_shapes():
    return render_template('fun_with_sine_waves_and_shapes.html')

@main_bp.route('/wave_front')
def wave_front():
    return render_template('wave_front.html')

@main_bp.route('/wave_front_line')
def wave_front_line():
    return render_template('wave_front_line.html')

@main_bp.route('/play_box')
def play_box():
    return render_template('play_box.html')