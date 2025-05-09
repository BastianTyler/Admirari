from flask import Blueprint, render_template

physics_bp = Blueprint('physics', __name__, url_prefix='/physics')


# Define Links for sidebar
THERMODYNAMICS_TABLE_OF_CONTENTS = [
    {"title": "Thermodynamics: Formulas", "url": "/physics/thermodynamics/thermodynamics_main"},
    {"title": "Thermodynamics: Symbols and Units", "url": "/physics/thermodynamics/thermodynamics_symbols"},
    {"title": "Thermodynamics: Engine Lab", "url": "/physics/thermodynamics/thermodynamics_lab_engine"},
    {"title": "Thermodynamics: Intro", "url": "/physics/thermodynamics/thermodynamics_intro_heat_temp"},
    {"title": "Thermodynamics: Temperature Scales", "url": "/physics/thermodynamics/thermodynamics_temperature_scales"},
    {"title": "Thermodynamics: Thermal Expansion", "url": "/physics/thermodynamics/thermodynamics_thermal_expansion"},
    {"title": "Thermodynamics: Heat", "url": "/physics/thermodynamics/thermodynamics_heat"},
    {"title": "Thermodynamics: Conduction", "url": "/physics/thermodynamics/thermodynamics_conduction"},
    {"title": "Thermodynamics: Radiation", "url": "/physics/thermodynamics/thermodynamics_radiation"},
    {"title": "Thermodynamics: Ideal Gas Law", "url": "/physics/thermodynamics/thermodynamics_ideal_gas_law"},
    {"title": "Thermodynamics: Boltzmann Distributions", "url": "/physics/thermodynamics/thermodynamics_boltzmann_distribution"},
    {"title": "Thermodynamics: First Law of Thermodynamics", "url": "/physics/thermodynamics/thermodynamics_first_law_of_thermodynamics"},
    {"title": "Thermodynamics: PV Diagrams", "url": "/physics/thermodynamics/thermodynamics_PV_diagrams"},
    
]


@physics_bp.context_processor
def inject_physics_context():
    return {
        'page_type': 'physics',
        'table_of_contents': THERMODYNAMICS_TABLE_OF_CONTENTS
    }

@physics_bp.route('/thermodynamics/thermodynamics_main')
def thermodynamics_main():
    return render_template('physics/thermodynamics/thermodynamics_main.html')

@physics_bp.route('/thermodynamics/thermodynamics_intro_heat_temp')
def thermodynamics_intro_heat_temp():
    return render_template('physics/thermodynamics/thermodynamics_intro_heat_temp.html')


@physics_bp.route('/thermodynamics/thermodynamics_symbols')
def thermodynamics_symbols():
    return render_template('physics/thermodynamics/thermodynamics_symbols.html')


@physics_bp.route('/thermodynamics/thermodynamics_formulas')
def thermodynamics_formulas():
    return render_template('physics/thermodynamics/thermodynamics_formulas.html')


@physics_bp.route('/thermodynamics/thermodynamics_temperature_scales')
def thermodynamics_temperature_scales():
    return render_template('physics/thermodynamics/thermodynamics_temperature_scales.html')


@physics_bp.route('/thermodynamics/thermodynamics_thermal_expansion')
def thermodynamics_thermal_expansion():
    return render_template('physics/thermodynamics/thermodynamics_thermal_expansion.html')


@physics_bp.route('/thermodynamics/thermodynamics_heat')
def thermodynamics_heat():
    return render_template('physics/thermodynamics/thermodynamics_heat.html')


@physics_bp.route('/thermodynamics/thermodynamics_ideal_gas_law')
def thermodynamics_ideal_gas_law():
    return render_template('physics/thermodynamics/thermodynamics_ideal_gas_law.html')




@physics_bp.route('/thermodynamics/thermodynamics_boltzmann_distribution')
def thermodynamics_boltzmann_distribution():
    return render_template('physics/thermodynamics/thermodynamics_boltzmann_distribution.html')



@physics_bp.route('/thermodynamics/thermodynamics_lab_engine')
def thermodynamics_lab_engine():
    return render_template('physics/thermodynamics/thermodynamics_lab_engine.html')



@physics_bp.route('/thermodynamics/thermodynamics_first_law_of_thermodynamics')
def thermodynamics_first_law_of_thermodynamics():
    return render_template('physics/thermodynamics/thermodynamics_first_law_of_thermodynamics.html')


@physics_bp.route('/thermodynamics/thermodynamics_PV_diagrams')
def thermodynamics_PV_diagrams():
    return render_template('physics/thermodynamics/thermodynamics_PV_diagrams.html')

@physics_bp.route('/thermodynamics/thermodynamics_conduction')
def thermodynamics_conduction():
    return render_template('physics/thermodynamics/thermodynamics_conduction.html')

@physics_bp.route('/thermodynamics/thermodynamics_radiation')
def thermodynamics_radiation():
    return render_template('physics/thermodynamics/thermodynamics_radiation.html')

