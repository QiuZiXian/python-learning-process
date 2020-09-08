# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/6  23:46
# @abstract    :
import netCDF4
import numpy.ma as ma
import scipy as sp
import scipy.signal as sg
import pandas as pd
import matplotlib.pyplot as plt


station = 'Valkenburg'
data_path = 'D:/d/homework/4/tgtg210-Valkenburg.nc'
data = netCDF4.Dataset(data_path,"r",format="NETCDF3_CLASSIC")
time =data.variables["time"]
start_date = pd.to_datetime(time.units.strip().split()[2],format='%Y-%m-%d')
dy = time[:]
days = pd.to_timedelta(dy, unit='D')
date = start_date+days

# 选择时间序列分析的起始时间
start_year = '1956'
end_year = '2012'
def GetNiceVarName(s):
    words=s.split(None)
    return ' '.join(words[2:min(4,len(words))])
gr = data.variables["fg"]
print(gr)
print(gr[:].max() )# Maximum value
print(gr[:].min()) # 最小值
print(gr[:].mean() )# 均值


# 图一
varname = GetNiceVarName(gr.long_name)
short_varname = gr.name
units = gr.units
gq = ma.masked_values(gr,gr._FillValue)
fg = pd.Series(gq,index=date).dropna()
gs = fg[start_year:end_year]
plt.figure(figsize=(12,3))
plt.gcf().canvas.set_window_title('The sample')
plt.plot(gs)
plt.title(varname+" ["+units+"]"+" at "+station)
plt.savefig(station+"_"+short_varname+"_temporal_variation.png")
plt.show() # 1956 -2012

# 图二
qi = fg.interpolate(method='linear')
date_range = pd.date_range(start=start_year,end=end_year,freq='A')
mean = [qi[date_range+pd.DateOffset(days=i)].mean() for i in range(0,364)]
fg_max = [qi[date_range+pd.DateOffset(days=i)].max() for i in range(0,364)]
fg_min = [qi[date_range+pd.DateOffset(days=i)].min() for i in range(0,364)]
plt.figure(figsize=(12, 4))
plt.gcf().canvas.set_window_title('Mean annual course')
plt.plot(mean, color='red', label='mean')
plt.plot(fg_min, label='fg_min')
plt.plot(fg_max, label='fg_max')
plt.title("Multiannual mean, max and min values of "+varname.lower()+" ["+units+"]"+" at "+station)
plt.xlabel('days of year')
plt.legend(loc='upper left')
plt.savefig(station+"_"+short_varname+"_minimax.png")
plt.show()


# 图三
xr=range(0,720)
r=[qi.autocorr(lag=x) for x in xr ]
plt.figure(figsize=(12, 3))
plt.gcf().canvas.set_window_title('Autocorrelation function')
plt.plot(xr,r)
plt.xlabel('days')
plt.title("Autocorrelation of "+varname.lower()+" at "+station)
plt.savefig(station+"_"+short_varname+"_autocorrelation.png")
plt.show()


# 图四
freq = 1./(3600.*24.)   # sampling frequency in Hz (as we have daily data)
conc_psd, Pxx_den = sp.signal.periodogram(qi,freq,detrend='linear',window='hann')
plt.figure(figsize=(12, 4))
plt.gcf().canvas.set_window_title('Power density')
plt.loglog(conc_psd, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('power density [$\mathrm{W}^2/\mathrm{(m}^2\mathrm{Hz)}$]')
plt.loglog(1./(7*24*3600.),1.E10,'ro',label='1 week')
plt.loglog(1./(183*24*3600.),1.E11,'ro',label='6 months')
plt.loglog(1./(365*24*3600.),5.E12,'ro',label='1 year')
plt.annotate('1 week',xy=(1./(7*24*3600.),1.E10),xycoords='data',xytext=(3E-6,1.E10),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.annotate('6 months',xy=(1./(183*24*3600.),1.E11),xycoords='data',xytext=(1.E-7,1.E11),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.annotate('1 year',xy=(1./(365*3600*24.),5.E12),xycoords='data',xytext=(1.E-8,2.E12),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.grid()
plt.title("Periodogram of "+varname.lower()+" at "+station)
plt.savefig(station+"_"+short_varname+"_periodogram.png")
plt.show()




station = 'Schiphol'
data_path = 'D:/d/homework/4/tgtg240-Schiphol.nc'
data = netCDF4.Dataset(data_path,"r",format="NETCDF3_CLASSIC")
time =data.variables["time"]
start_date = pd.to_datetime(time.units.strip().split()[2],format='%Y-%m-%d')
dy = time[:]
days = pd.to_timedelta(dy, unit='D')
date = start_date+days

# 选择时间序列分析的起始时间
start_year = '1956'
end_year = '2012'
def GetNiceVarName(s):
    words=s.split(None)
    return ' '.join(words[2:min(4,len(words))])
gr = data.variables["tg"]
# gr = data.variables["fg"]
print(gr)
print(gr[:].max() )# Maximum value
print(gr[:].min()) # 最小值
print(gr[:].mean() )# 均值


# 图一
varname = GetNiceVarName(gr.long_name)
short_varname = gr.name
units = gr.units
gq = ma.masked_values(gr,gr._FillValue)
fg = pd.Series(gq,index=date).dropna()
# tg = pd.Series(gq,index=date).dropna()
gs = fg[start_year:end_year]
# gs = tg[start_year:end_year]
plt.figure(figsize=(12,3))
plt.gcf().canvas.set_window_title('The sample')
plt.plot(gs)
plt.title(varname+" ["+units+"]"+" at "+station)
plt.savefig(station+"_"+short_varname+"_temporal_variation.png")
plt.show() # 1956 -2012

# 图二
# qi = fg.interpolate(method='linear')
qi = tg.interpolate(method='linear')
date_range = pd.date_range(start=start_year,end=end_year,freq='A')
mean = [qi[date_range+pd.DateOffset(days=i)].mean() for i in range(0,364)]
fg_max = [qi[date_range+pd.DateOffset(days=i)].max() for i in range(0,364)]
fg_min = [qi[date_range+pd.DateOffset(days=i)].min() for i in range(0,364)]
# tg_max = [qi[date_range+pd.DateOffset(days=i)].max() for i in range(0,364)]
# tg_min = [qi[date_range+pd.DateOffset(days=i)].min() for i in range(0,364)]
plt.figure(figsize=(12, 4))
plt.gcf().canvas.set_window_title('Mean annual course')
plt.plot(mean, color='red', label='mean')
# plt.plot(tg_min, label='tg_min')
# plt.plot(tg_max, label='tg_max')
plt.plot(fg_min, label='fg_min')
plt.plot(fg_max, label='fg_max')
plt.title("Multiannual mean, max and min values of "+varname.lower()+" ["+units+"]"+" at "+station)
plt.xlabel('days of year')
plt.legend(loc='upper left')
plt.savefig(station+"_"+short_varname+"_minimax.png")
plt.show()


# 图三
xr=range(0,720)
r=[qi.autocorr(lag=x) for x in xr ]
plt.figure(figsize=(12, 3))
plt.gcf().canvas.set_window_title('Autocorrelation function')
plt.plot(xr,r)
plt.xlabel('days')
plt.title("Autocorrelation of "+varname.lower()+" at "+station)
plt.savefig(station+"_"+short_varname+"_autocorrelation.png")
plt.show()


# 图四
freq = 1./(3600.*24.)   # sampling frequency in Hz (as we have daily data)
conc_psd, Pxx_den = sp.signal.periodogram(qi,freq,detrend='linear',window='hann')
plt.figure(figsize=(12, 4))
plt.gcf().canvas.set_window_title('Power density')
plt.loglog(conc_psd, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('power density [$\mathrm{W}^2/\mathrm{(m}^2\mathrm{Hz)}$]')
plt.loglog(1./(7*24*3600.),1.E10,'ro',label='1 week')
plt.loglog(1./(183*24*3600.),1.E11,'ro',label='6 months')
plt.loglog(1./(365*24*3600.),5.E12,'ro',label='1 year')
plt.annotate('1 week',xy=(1./(7*24*3600.),1.E10),xycoords='data',xytext=(3E-6,1.E10),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.annotate('6 months',xy=(1./(183*24*3600.),1.E11),xycoords='data',xytext=(1.E-7,1.E11),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.annotate('1 year',xy=(1./(365*3600*24.),5.E12),xycoords='data',xytext=(1.E-8,2.E12),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.grid()
plt.title("Periodogram of "+varname.lower()+" at "+station)
plt.savefig(station+"_"+short_varname+"_periodogram.png")
plt.show()