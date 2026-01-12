from flask import Flask, render_template
import pandas as pd
import numpy as np
import plotly.graph_objects as go

app = Flask(__name__)

def generate_plot():
    # Dummy data for fc_log_test (first 14 forecasts)
    data_test = {'forecast_start': pd.to_datetime(pd.date_range(start='2023-01-01', periods=14, freq='D')),
                 'rmse': np.random.uniform(10, 30, 14)}
    fc_log_test = pd.DataFrame(data_test)

    # Dummy data for fc_log (remaining forecasts)
    data_log = {'forecast_start': pd.to_datetime(pd.date_range(start='2023-01-15', periods=30, freq='D')),
                'rmse': np.random.uniform(10, 40, 30)}
    fc_log = pd.DataFrame(data_log)

    # Set threshold: mean + 3 standard deviations
    rmse_threshold = fc_log_test["rmse"].mean() + 3 * fc_log_test["rmse"].std()

    # Create rolling window averages for RMSE
    fc_log["rmse_ma_7"] = fc_log["rmse"].rolling(window=7).mean()
    fc_log["rmse_ma_14"] = fc_log["rmse"].rolling(window=14).mean()

    p = go.Figure()

    # Add RMSE line
    p.add_trace(go.Scatter(x=fc_log["forecast_start"], y=fc_log["rmse"],
                            mode='lines',
                            name='RMSE',
                            line=dict(color='royalblue', width=2)))

    # Add the RMSE rolling windows for 7 and 14 days
    p.add_trace(go.Scatter(x=fc_log["forecast_start"], y=fc_log["rmse_ma_7"],
                            mode='lines',
                            name='7 Days MA',
                            line=dict(color='green', width=2)))

    p.add_trace(go.Scatter(x=fc_log["forecast_start"], y=fc_log["rmse_ma_14"],
                            mode='lines',
                            name='14 Days MA',
                            line=dict(color='orange', width=2)))

    p.add_trace(go.Scatter(x=[fc_log["forecast_start"].min(), fc_log["forecast_start"].max()], 
    y=[rmse_threshold, rmse_threshold], 
    name="Threshold",
    line=dict(color="red", width=2, dash="dash")))

    # Add plot titles and show the plot
    p.update_layout(title="Forecast Error Rate Over Time",
                    xaxis_title="Forecast Start",
                    yaxis_title="RMSE", 
                    height=400,
                    title_x=0.5,
                    margin=dict(t=50, b=50, l=50, r=50))
    
    return p

@app.route('/')
def index():
    plot = generate_plot()
    plot_div = plot.to_html(full_html=False)
    return render_template('index.html', plot_div=plot_div)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
