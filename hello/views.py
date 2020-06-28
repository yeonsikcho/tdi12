from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from django.http import JsonResponse
import datetime
import requests
from bokeh.plotting import figure
from bokeh.embed import json_item

import json
import requests


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def loadmain(request):
	return render(request, 'tdi12.html')

def keyword_search(request):
	"""Return list of matching stocks based on keyword_search"""
	keyword = request.GET.get('keyword',None)
	#Alpha Vantage Key
	key = 'GKOK7RKCCK0F6C4C'
	url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={key}'
	req = requests.get(url)
	result = [f"{item['1. symbol']}: {item['2. name']}" for item in json.loads(req.content)['bestMatches']]
	return JsonResponse({'items':result})

	
def show_plot(request):
	"""Return json elements of time series line plot"""
	ticker_raw = request.GET.get('ticker',None)
	key = 'GKOK7RKCCK0F6C4C'
	ticker = ticker_raw.split(":")[0]
	url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={key}"
	req = requests.get(url)
	dt = json.loads(req.content)['Time Series (Daily)']
	dates = list(dt.keys())[:30]
	adj_cls = [float(dt[date]['5. adjusted close']) for date in dates]
	dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates]
	p = figure(x_axis_type="datetime", plot_width=800, plot_height=350)
	p.line(dates, adj_cls,legend_label=ticker_raw)
	
	return JsonResponse(json_item(p, "myplot"))
	