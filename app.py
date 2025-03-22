from flask import Flask, render_template # import flask and render template

# Run and then go to http://127.0.0.1:5000/ to see homepage

app = Flask(__name__) # This creates a flask application

# Import and register blueprints
from routes.main_routes import main_bp
from routes.math_routes import math_bp
from routes.physics_routes import physics_bp
from routes.text_venture_routes import tv_bp
from routes.programming_routes import programming_bp
from routes.programming_routes import godot_bp

app.register_blueprint(main_bp)
app.register_blueprint(math_bp)
app.register_blueprint(physics_bp)
app.register_blueprint(tv_bp)
app.register_blueprint(programming_bp)
app.register_blueprint(godot_bp)

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
