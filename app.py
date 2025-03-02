from flask import Flask, render_template # import flask and render template

# Run and then go to http://127.0.0.1:5000/ to see homepage

app = Flask(__name__) # This creates a flask application

@app.route('/') # This defines routes to different pages. This is the default home page
def home():
    return render_template('home.html') # Return a render template as a response

@app.route('/about') # 
def about():
    return render_template('about.html')

@app.route('/math/linear_algebra')
def linear_algebra():
    return render_template('math/linear_algebra.html')

@app.route('/math/mathJax_folder/mathJax')
def mathJax():
    return render_template('math/mathJax_folder/mathJax.html')

@app.route('/math/mathJax_folder/mathJax_matrices')
def mathJax_matricies():
    return render_template('math/mathJax_folder/mathJax_matrices.html')

@app.route('/math/linear_algebra_folder/matrix_addition')
def matrix_addition():
    return render_template('math/linear_algebra_folder/matrix_addition.html')

@app.route('/math/linear_algebra_folder/matrix_terminology_one')
def show_matrix_terminology():
    return render_template('math/linear_algebra_folder/matrix_terminology_one.html')

@app.route('/math/linear_algebra_folder/matrix_multiplication')
def matrix_multiplication():
    return render_template('math/linear_algebra_folder/matrix_multiplication.html')

@app.route('/physics/thermodynamics')
def thermodynamics():
    return render_template('physics/thermodynamics.html')

@app.route('/fun_with_sine_waves_and_shapes') 
def fun_with_sine_waves_and_shapes():
    return render_template('fun_with_sine_waves_and_shapes.html') 

@app.route('/wave_front') # 
def wave_front():
    return render_template('wave_front.html') 

@app.route('/wave_front_line') # 
def wave_front_line():
    return render_template('wave_front_line.html') 

if __name__ == "__main__":
    app.run(debug = True) # Run the app in debug mode
