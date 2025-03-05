from flask import Blueprint, render_template

math_bp = Blueprint('math', __name__, url_prefix='/math')



# Define Links for sidebar
LINEAR_ALGEBRA_TABLE_OF_CONTENTS = [
    {"title": "Linear Algebra", "url": "/math/linear_algebra"},
    {"title": "Matrix Terminology One", "url": "/math/linear_algebra_folder/matrix_terminology_one"},
    {"title": "Matrix Addition", "url": "/math/linear_algebra_folder/matrix_addition"},
    {"title": "Matrix Multiplication", "url": "/math/linear_algebra_folder/matrix_multiplication"},
    {"title": "Basic Row Operations", "url": "/math/linear_algebra_folder/matrix_row_operations"},
    {"title": "Row Echelon Form", "url": "/math/linear_algebra_folder/matrix_row_echelon"},
    {"title": "Gaussian Elimination", "url": "/math/linear_algebra_folder/matrix_gaussian_elemination"},
    {"title": "Inverse of a Matrix", "url": "/math/linear_algebra_folder/matrix_inverse"},
    {"title": "Determinant Overview", "url": "/math/linear_algebra_folder/determinant_overview"},
    {"title": "Cramers Rule", "url": "/math/linear_algebra_folder/matrix_cramers_rule"},
    {"title": "Adjoint", "url": "/math/linear_algebra_folder/matrix_adjoint"},
]

LINEAR_ALGEBRA_RELATED_TOPICS = [
    {"title": "Matrix Addition", "url": "/math/linear_algebra/matrix_addition"},
    {"title": "Matrix Multiplication", "url": "/math/linear_algebra/matrix_multiplication"},
    {"title": "Determinants", "url": "/math/linear_algebra/determinants"},
    {"title": "Eigenvalues", "url": "/math/linear_algebra/eigenvalues"},
]


@math_bp.route('/linear_algebra')
def linear_algebra():
    return render_template('math/linear_algebra.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)
# Latex chart
@math_bp.route('/mathJax_folder/mathJax')
def mathJax():
    return render_template('math/mathJax_folder/mathJax.html')
# Mathjax on matricies
@math_bp.route('/mathJax_folder/mathJax_matrices')
def mathJax_matrices():
    return render_template('math/mathJax_folder/mathJax_matrices.html')
# Matrix Addition
@math_bp.route('/linear_algebra_folder/matrix_addition')
def matrix_addition():
    return render_template('math/linear_algebra_folder/matrix_addition.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)
# Matrix Terminology One
@math_bp.route('/linear_algebra_folder/matrix_terminology_one')
def show_matrix_terminology():
    return render_template('math/linear_algebra_folder/matrix_terminology_one.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)
# Multiplication
@math_bp.route('/linear_algebra_folder/matrix_multiplication')
def matrix_multiplication():
    return render_template('math/linear_algebra_folder/matrix_multiplication.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)
# Row Echelon
@math_bp.route('/linear_algebra_folder/matrix_row_echelon')
def matrix_row_echelon():
    return render_template('math/linear_algebra_folder/matrix_row_echelon.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)
# Row operations
@math_bp.route('/linear_algebra_folder/matrix_row_operations')
def matrix_row_operations():
    return render_template('math/linear_algebra_folder/matrix_row_operations.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)
# Inverse
@math_bp.route('/linear_algebra_folder/matrix_inverse')
def matrix_inverse():
    return render_template('math/linear_algebra_folder/matrix_inverse.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)
# Gaussian Elemination
@math_bp.route('/linear_algebra_folder/matrix_gaussian_elemination')
def matrix_gaussian_elemination():
    return render_template('math/linear_algebra_folder/matrix_gaussian_elemination.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)

# Determinant Overview
@math_bp.route('/linear_algebra_folder/determinant_overview')
def determinant_overview():
    return render_template('math/linear_algebra_folder/determinant_overview.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)

# Cramers Elemination
@math_bp.route('/linear_algebra_folder/matrix_cramers_rule')
def cramers_rule():
    return render_template('math/linear_algebra_folder/matrix_cramers_rule.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)

# Adjoint Elemination
@math_bp.route('/linear_algebra_folder/matrix_adjoint')
def adjoint():
    return render_template('math/linear_algebra_folder/matrix_adjoint.html', 
                           table_of_contents=LINEAR_ALGEBRA_TABLE_OF_CONTENTS,
                           related_topics=LINEAR_ALGEBRA_RELATED_TOPICS)