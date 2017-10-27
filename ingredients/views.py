from django.shortcuts import render
import psycopg2
# Create your views here.

def home(request):
	if(request.method == 'GET'):
		conn = psycopg2.connect("host='localhost' dbname='cookMeUp' user='postgres' password='thara96'")
		cursor = conn.cursor()
		cursor.execute('select * from min_ingredient');
		records = cursor.fetchall()
		cursor.execute('select * from major_ingredient');
		recor = cursor.fetchall()
		cursor.close()
		return render(request, 'ingredients.html',{'maj':recor,'min':records})

def req(request):
	if(request.method == 'GET'):
		return render(request, 'ingredients.html')
	data = request.data
	fop = data['fop']
	sop = data['sop']
	conn = psycopg2.connect("host='localhost' dbname='cookMeUp' user='postgres' password='thara96'")
