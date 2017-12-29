from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.io import output_notebook, push_notebook, show, output_file
import pandas as pd
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index1.html')
    
@app.route('/', methods=['POST'])
def index():
    #ticker = input('stock ticker:')
    #ticker=request.form('ticker')
    ticker=request.form['tick']
    baseurl='https://www.quandl.com/api/v3/datasets/WIKI/'
    key='api_key=JSGibRx-xpoA_y9Daq9e'

    url=baseurl+ticker+'.csv'+'?rows=60'+'?'+key

    c=pd.read_csv(url)
    df=c
    df['Date']=pd.to_datetime(df['Date'])
    dfs=df.sort_values(by=['Date'])
    TOOLS='pan,wheel_zoom,box_zoom,reset'
    test = figure(x_axis_type='datetime', tools=TOOLS)
    test.line(dfs['Date'],dfs['Close'])
    
    #output_file('play.html')
    show(test)
    
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')