from flask import Flask, render_template
import pandas as pd
import json
from pytrends.request import TrendReq
import datetime, pytz
import plotly
import plotly.express as px
app = Flask(__name__)
@app.route('/')
def notdash():
    
    pytrends = TrendReq()
    cat = '0'
    timeframe = ['now 1-H' , 'now 4-H']
    contry = 'IR'
    kw_list = ['/g/122fjxp1']

    pytrends.build_payload(kw_list,timeframe=timeframe[0] ,cat=cat,geo=contry)
    result =pytrends.interest_over_time()
    index = result.index
    cet = pytz.timezone('Asia/Tehran')
    b = result.tz_localize(pytz.utc).tz_convert(cet)
    fig = px.line(b, x=b.index,y=['/g/122fjxp1'])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)
