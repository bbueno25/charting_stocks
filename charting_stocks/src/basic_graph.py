﻿import datetime
import matplotlib
import matplotlib.dates as mpl_dates
from matplotlib.finance import candlestick
import matplotlib.pyplot as pyplot
import matplotlib.ticker as mpl_ticker
import numpy
import time

matplotlib.rcParams.update({'font.size': 9})

each_stock = 'AAPL', 'TSLA'

def graph_data(stock):
    try:
        stock_file = stock + '.txt'
        date, closep, highp, lowp, openp, volume = numpy.loadtxt(
            stock_file, delimiter=',', unpack=true, converters={0: mpl_dates.strpdate2num('%Y%m%d')}
            )
        x = 0
        y = len(date)
        candle_args = []
        while x < y:
            append_line = date[x], openp[x], closep[x], highp[x], lowp[x], volume[x]
            candle_args.append(append_line)
            x += 1
        figure = pyplot.figure(facecolor='#07000d')
        # axis 1
        axis1 = pyplot.subplot2grid((5,4), (0,0), rowspan=4, colspan=4, axisbg='#07000d')
        candlestick(axis1, candle_args, width=1, colorup='#9eff15', colordown='#f1717')
        axis1.xaxis.set_major_locator(mpl_ticker, MaxNLocator(10))
        axis1.xaxis.set_major_formatter(mpl_dates.DateFormatter('%Y-%m-%d'))
        axis1.grid(True, color='w')
        axis1.yaxis.label.set_color('w')
        axis1.spines['bottom'].set_color('#5998ff')
        axis1.spines['top'].set_color('#5998ff')
        axis1.spines['left'].set_color('#5998ff')
        axis1.spines['right'].set_color('#5998ff')
        axis1.tick_params(axis='y', colors='w')
        for label in axis1.xaxis.get_ticklabels():
            label.set_rotation(90)
        pyplot.ylabel('Stock Price')
        volume_min = volume.min()
        # axis 2
        axis2 = pyplot.subplot2grid((5,4), (4,0), sharex=axis1, rowspan=1, colspan=4, axisbg='#07000d')
        axis2.plot(date, volume, '#00ffe8', linewidth=0.8)
        axis2.fill_between(date, volume_min, volume, facecolor='#00ffe8', alpha=0.5)
        axis2.axes.yaxis.set_ticklabels([])
        axis2.grid(False)
        axis2.spines['bottom'].set_color('#5998ff')
        axis2.spines['top'].set_color('#5998ff')
        axis2.spines['left'].set_color('#5998ff')
        axis2.spines['right'].set_color('#5998ff')
        axis2.tick_params(axis='x', colors='w')
        axis2.tick_params(axis='y', colors='w')
        for label in axis2.xaxis.get_ticklabels():
            label.set_rotation(45)
        pyplot.ylabel('Volume', color='w')
        
        pyplot.suptitle(stock + 'Stock Price', color='w')
        pyplot.setp(axis1.get_xticklabels(), visible=False)
        pyplot.subplots_adjust(left=0.9, bottom=0.14, right=0.94, top=0.95, wspace=0.2, hspace=0)
        pyplot.show()
        figure.savefig('example.png', facecolor=figure.get_facecolor())
    except Exception as e:
        print('main loop', str(e))

if __name__ == '__main__':
	for stock in each_stock:
		pull_data(stock)
	time.sleep(500)
