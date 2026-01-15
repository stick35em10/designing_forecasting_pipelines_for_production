from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the pre-computed plot."""
    print("Rendering template...")
    with open('templates/plot_div.html', 'r') as f:
        plot_div = f.read()
    return render_template('plot.html', plot_div=plot_div)

if __name__ == '__main__':
    app.run(debug=True)