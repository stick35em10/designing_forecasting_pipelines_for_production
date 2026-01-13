from flask import Flask, render_template
import plotly
from ex_7_model_drift.ex_9_Identifying_model_drift.script import generate_plot

app = Flask(__name__)

@app.route('/')
def index():
    fig = generate_plot()
    graphJSON = plotly.io.to_json(fig, pretty=True)
    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
