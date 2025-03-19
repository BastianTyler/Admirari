from flask import Blueprint, render_template

programming_bp = Blueprint('programming', __name__, url_prefix='/programming')
godot_bp = Blueprint('godot', __name__, url_prefix='/programming/godot')


# Define Links for sidebar
JAVA_SIDEBAR_TABLE_OF_CONTENTS = [
    {"title": "Java Home", "url": "/programming/java/home_java"},
    {"title": "Linked Lists", "url": "/programming/java/linked_list"},
    {"title": "Lambda", "url": "/programming/java/java_lambda"},
]

GODOT_SIDEBAR_TABLE_OF_CONTENTS = [
    {"title": "Godot Home", "url": "/programming/godot/godot_home"},
    {"title": "Notes", "url": "/programming/godot/godot_notes"}
]

@programming_bp.context_processor
def inject_programming_context():
    return {
        'page_type': 'programming',
        'table_of_contents': JAVA_SIDEBAR_TABLE_OF_CONTENTS
    }

@godot_bp.context_processor
def inject_programming_context():
    return {
        'page_type': 'programming',
        'table_of_contents': GODOT_SIDEBAR_TABLE_OF_CONTENTS
    }


@programming_bp.route('/java/home_java')
def home_java():
    return render_template('/programming/java/home_java.html') 


@programming_bp.route('/java/linked_list')
def linked_list():
    return render_template('/programming/java/linked_list.html') 


@programming_bp.route('/java/java_lambda')
def java_lambda():
    return render_template('/programming/java/java_lambda.html')

@godot_bp.route('/godot_home')
def godot_home():
    return render_template('/programming/godot/godot_home.html')

@godot_bp.route('/godot_notes')
def godot_notes():
    return render_template('/programming/godot/godot_notes.html') 





