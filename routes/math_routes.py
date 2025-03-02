from flask import Blueprint, render_template

math_bp = Blueprint('math', __name__, url_prefix='/math')

@math_bp.route('/linear_algebra')
def linear_algebra():
    return render_template('math/linear_algebra.html')
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
    return render_template('math/linear_algebra_folder/matrix_addition.html')
# Matrix Terminology One
@math_bp.route('/linear_algebra_folder/matrix_terminology_one')
def show_matrix_terminology():
    return render_template('math/linear_algebra_folder/matrix_terminology_one.html')
# Multiplication
@math_bp.route('/linear_algebra_folder/matrix_multiplication')
def matrix_multiplication():
    return render_template('math/linear_algebra_folder/matrix_multiplication.html')
# Row Echelon
@math_bp.route('/linear_algebra_folder/matrix_row_echelon')
def matrix_row_echelon():
    return render_template('math/linear_algebra_folder/matrix_row_echelon.html')
# Row operations
@math_bp.route('/linear_algebra_folder/matrix_row_operations')
def matrix_row_operations():
    return render_template('math/linear_algebra_folder/matrix_row_operations.html')
# Inverse
@math_bp.route('/linear_algebra_folder/matrix_inverse')
def matrix_inverse():
    return render_template('math/linear_algebra_folder/matrix_inverse.html')
# Gaussian Elemination
@math_bp.route('/linear_algebra_folder/matrix_gaussian_elemination')
def matrix_gaussian_elemination():
    return render_template('math/linear_algebra_folder/matrix_gaussian_elemination.html')