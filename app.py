from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import plotly
app = Flask(__name__)

# Load and clean data
df = pd.read_csv('911.csv')
df['zip'] = df['zip'].fillna(df['zip'].mode()[0])
df['twp'] = df['twp'].fillna('Unknown')
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['hour'] = df['timeStamp'].dt.hour
df['day_of_week'] = df['timeStamp'].dt.day_name()
df['month'] = df['timeStamp'].dt.month_name()
df['reason'] = df['title'].apply(lambda x: x.split(':')[0].strip())
df = df.drop_duplicates()

def generate_plots(filtered_df):
    # Reason Distribution
    reason_counts = filtered_df['reason'].value_counts()
    reason_plot = px.bar(x=reason_counts.index, y=reason_counts.values, labels={'x': 'Reason', 'y': 'Number of Calls'},
                         title='Distribution of 911 Calls by Reason', color=reason_counts.index)

    # Monthly Trends
    monthly_calls = filtered_df.groupby('month').size().reindex(
        ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    )
    monthly_plot = px.line(x=monthly_calls.index, y=monthly_calls.values, labels={'x': 'Month', 'y': 'Number of Calls'},
                           title='911 Call Volume by Month', markers=True)

    # Day-Hour Heatmap
    day_hour = filtered_df.groupby(['day_of_week', 'hour']).size().unstack()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_hour = day_hour.reindex(day_order)
    heatmap_plot = go.Figure(data=go.Heatmap(
        z=day_hour.values, x=day_hour.columns, y=day_hour.index, colorscale='YlOrRd',
        hoverongaps=False))
    heatmap_plot.update_layout(title='911 Calls by Day of Week and Hour', xaxis_title='Hour of Day', yaxis_title='Day of Week')

    # Geographic Map
    map_plot = px.scatter_mapbox(filtered_df, lat='lat', lon='lng', color='reason', size_max=15,
                                 zoom=10, mapbox_style='open-street-map',
                                 title='Geographic Distribution of 911 Calls',
                                 hover_data={'lat': False, 'lng': False, 'reason': True, 'twp': True})

    # Top Townships
    top_townships = filtered_df['twp'].value_counts().head(10)
    township_plot = px.bar(x=top_townships.values, y=top_townships.index, labels={'x': 'Number of Calls', 'y': 'Township'},
                           title='Top 10 Townships by 911 Call Volume', orientation='h', color=top_townships.index)

    return {
        'reason_plot': json.dumps(reason_plot, cls=plotly.utils.PlotlyJSONEncoder),
        'monthly_plot': json.dumps(monthly_plot, cls=plotly.utils.PlotlyJSONEncoder),
        'heatmap_plot': json.dumps(heatmap_plot, cls=plotly.utils.PlotlyJSONEncoder),
        'map_plot': json.dumps(map_plot, cls=plotly.utils.PlotlyJSONEncoder),
        'township_plot': json.dumps(township_plot, cls=plotly.utils.PlotlyJSONEncoder)
    }

@app.route('/')
def dashboard():
    plots = generate_plots(df)
    return render_template('index.html', **plots)

@app.route('/filter', methods=['POST'])
def filter_data():
    reason = request.form.get('reason', 'all')
    filtered_df = df if reason == 'all' else df[df['reason'] == reason]
    plots = generate_plots(filtered_df)
    return jsonify(plots)

if __name__ == '__main__':
    app.run(debug=True)