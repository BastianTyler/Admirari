from flask import Blueprint, render_template

physics_bp = Blueprint('physics', __name__, url_prefix='/physics')


# Define Links for sidebar
LINEAR_ALGEBRA_TABLE_OF_CONTENTS = [
    {"title": "Thermodynamics: Boltzmann Distributions", "url": "/physics/thermodynamics/thermodynamics_boltzmann_distribution"},
    {"title": "Thermodynamics: Intro", "url": "/physics/thermodynamics/thermodynamics_intro_heat_temp"},
    {"title": "Thermodynamics: First Law of Thermodynamics", "url": "/physics/thermodynamics/thermodynamics_main"},
    {"title": "Thermodynamics: Ideal Gas Law", "url": "/physics/thermodynamics/thermodynamics_main"},
    {"title": "Thermodynamics: PV Diagrams", "url": "/physics/thermodynamics/thermodynamics_main"},
    {"title": "Thermodynamics: Radiation", "url": "/physics/thermodynamics/thermodynamics_main"},
    {"title": "Thermodynamics: Formulas", "url": "/physics/thermodynamics/thermodynamics_main"},
    {"title": "Thermodynamics: Symbols and Units", "url": "/physics/thermodynamics/thermodynamics_symbols"},
]

@physics_bp.route('/thermodynamics/thermodynamics_main')
def thermodynamics_main():
    return render_template('physics/thermodynamics/thermodynamics_main.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS)

@physics_bp.route('/thermodynamics/thermodynamics_intro_heat_temp')
def thermodynamics_intro_heat_temp():
    return render_template('physics/thermodynamics/thermodynamics_intro_heat_temp.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS)

@physics_bp.route('/thermodynamics/thermodynamics_symbols')
def thermodynamics_symbolsp():
    return render_template('physics/thermodynamics/thermodynamics_symbols.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS)