from flask import Flask, render_template # import flask and render template

# Run and then go to http://127.0.0.1:5000/ to see homepage

app = Flask(__name__) # This creates a flask application

@app.route('/') # This defines routes to different pages. This is the default home page
def home():
    return render_template('home.html') # Return a render template as a response

@app.route('/about') # 
def about():
    return render_template('about.html') # Return a render template as a response

@app.route('/fun_with_sine_waves_and_shapes') # 
def fun_with_sine_waves_and_shapes():
    return render_template('fun_with_sine_waves_and_shapes.html') # Return a render template as a response

@app.route('/wave_front') # 
def wave_front():
    return render_template('wave_front.html') # Return a render template as a response

@app.route('/wave_front_line') # 
def wave_front_line():
    return render_template('wave_front_line.html') # Return a render template as a response

if __name__ == "__main__":
    app.run(debug = True) # Run the app in debug mode
