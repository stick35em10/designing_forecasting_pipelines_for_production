from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the pre-computed plot."""
    print("Rendering template...")
    return render_template('plot.html')

if __name__ == '__main__':
    app.run(debug=True)