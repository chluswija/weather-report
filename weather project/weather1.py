import tkinter as tk
from bs4 import BeautifulSoup as bs
import requests

root = tk.Tk()
root.geometry('300x400')
root.title('City Weather Forecast')

def forecast():
	city = e.get()
	url = 'https://www.weather-forecast.com/locations/'+str(city)+'/forecasts/latest'
	r = requests.get(url)
	html_code = bs(r.content)
	day = html_code.find('div',attrs={'class':'b-forecast__table-days-name'}).get_text()
	date = html_code.find('div',attrs={'class':'b-forecast__table-days-date'}).get_text()
	t = html_code.find_all('span',attrs={'class':'b-forecast__table-value'})
	time = [i.get_text() for i in t[0:3]]
	w = html_code.find('tr',attrs={'class':'b-forecast__table-summary js-summary'})
	w1 = w.find_all('div',attrs={'class':'b-forecast__text-limit'})
	weather = [i.get_text() for i in w1[0:3]]
	t = html_code.find_all('span',attrs={'class':'temp b-forecast__table-value'})
	temprature = [i.get_text() for i in t[0:3]]
	mt = html_code.find('tr',attrs={'class':'b-forecast__table-min-temperature js-min-temp'})
	mt1 = mt.find_all('span',attrs={'class':'temp b-forecast__table-value'})
	min_temprature = [i.get_text() for i in mt1[0:3]]
	
	day_label = tk.Label(root,text=str(day)+str(date))
	day_label.pack()

	frame1 = tk.Frame(root)
	frame1.pack()

	l2 = tk.Label(frame1,text='High')
	l2.grid(row=1,column=0)
	l3 = tk.Label(frame1,text='Low')
	l3.grid(row=2,column=0)
	l4 = tk.Label(frame1,text='Weather')
	l4.grid(row=3,column=0)

	for i in range(len(time)):
		time_label = tk.Label(frame1,text=time[i])
		time_label.grid(row=0,column=i+1)

		temprature_label = tk.Label(frame1,text=temprature[i])
		temprature_label.grid(row=1,column=i+1)

		min_temprature_label = tk.Label(frame1,text=min_temprature[i])
		min_temprature_label.grid(row=2,column=i+1)

		weather_label = tk.Label(frame1,text=weather[i])
		weather_label.grid(row=3,column=i+1)

	def reset():
		day_label.config(text='')
		frame1.destroy()
		btn1.destroy()
		e.delete(0,'end')
	btn1 = tk.Button(root,text='Delete',command=reset)
	btn1.pack()		
l = tk.Label(root,text='City Weather Forecast')
l.pack(pady=10)

l1 = tk.Label(root,text='Enter City Name')
l1.pack()

frame = tk.Frame(root)
frame.pack()

e = tk.Entry(frame,width=20,font=('20'))
e.grid(row=0,column=0)

btn = tk.Button(frame,text='Search',padx=10,command=forecast)
btn.grid(row=0,column=1)





root.mainloop()