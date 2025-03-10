from flask import Blueprint, render_template

programming_bp = Blueprint('programming', __name__, url_prefix='/programming')


# Define Links for sidebar
SIDEBAR_TABLE_OF_CONTENTS = [
    {"title": "Thermodynamics: Formulas", "url": "/programming/java/linked_list"},
]


@programming_bp.route('/java/home_java')
def home_java():
    return render_template('/programming/java/home_java.html', 
                           table_of_contents=SIDEBAR_TABLE_OF_CONTENTS)

@programming_bp.route('/java/linked_list')
def linked_list():
    return render_template('/programming/java/linked_list.html', 
                           table_of_contents=SIDEBAR_TABLE_OF_CONTENTS)



