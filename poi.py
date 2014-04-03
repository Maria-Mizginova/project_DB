# coding:utf-8

import urllib.request
import re
item_data = []
url = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%A0%%D0%%BE%%D1%%81%%D1%%81%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s'

for offset in range (2008, 2010, 1) :
	data = urllib.request.urlopen ( url % offset).read()
	data = data.decode()
	data = re.sub('&nbsp;',' ', data)
	title = data.split("""<h2><span class="mw-headline" id=".D0.A3.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Участники""")
	table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
	items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
	for i in  items_tr[1:]:

		club, city, stadium, capacity, sponsor = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
		item = {
			'club' : club,
			'city' : city,
			'stadium' : stadium,
			'capacity' : capacity,

            'year' : offset
			}
		item_data.append(item)


italy = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%98%%D1%%82%%D0%%B0%%D0%%BB%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2009, 2012, 1) :
    try:
        data = urllib.request.urlopen ( italy %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.A3.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity,coach = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass


spain = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%98%%D1%%81%%D0%%BF%%D0%%B0%%D0%%BD%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2009, 2012, 1) :
    try:
     data = urllib.request.urlopen ( spain %(offset, offset+1)).read()
     data = data.decode()
     data = re.sub('&nbsp;',' ', data)
     title = data.split("""<h2><span class="mw-headline" id=".D0.9A.D0.BB.D1.83.D0.B1.D1.8B-.D1.83.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Клубы-участники""")
     table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
     items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
     for i in  items_tr[1:]:

            club, city, stadium, capacity = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
             'year' : offset
		      	}
     item_data.append(item)
    except: pass

france = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%A4%%D1%%80%%D0%%B0%%D0%%BD%%D1%%86%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2006, 2012, 1) :
    try:
        data = urllib.request.urlopen ( france %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.9A.D0.BB.D1.83.D0.B1.D1.8B-.D1.83.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Клубы-участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass

cheh = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%A7%%D0%%B5%%D1%%85%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2009, 2012, 1) :
    try:
        data = urllib.request.urlopen ( cheh %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.A3.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass

tur = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%A2%%D1%%83%%D1%%80%%D1%%86%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2007, 2012, 1) :
    try:
        data = urllib.request.urlopen ( tur %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.A3.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity, place = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass


nethe = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%9D%%D0%%B8%%D0%%B4%%D0%%B5%%D1%%80%%D0%%BB%%D0%%B0%%D0%%BD%%D0%%B4%%D0%%BE%%D0%%B2_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2008, 2012, 1) :
    try:
        data = urllib.request.urlopen ( nethe %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.A3.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity, place = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass


belg = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%91%%D0%%B5%%D0%%BB%%D1%%8C%%D0%%B3%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2008, 2012, 1) :
    try:
        data = urllib.request.urlopen ( belg %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.9A.D0.BB.D1.83.D0.B1.D1.8B-.D1.83.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Клубы-участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass


denmark = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%94%%D0%%B0%%D0%%BD%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2010, 2012, 1) :
    try:
        data = urllib.request.urlopen ( denmark %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.9A.D0.BB.D1.83.D0.B1.D1.8B-.D1.83.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Клубы-участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity, place = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass

uk = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%A3%%D0%%BA%%D1%%80%%D0%%B0%%D0%%B8%%D0%%BD%%D1%%8B_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2001, 2012, 1) :
    try:
        data = urllib.request.urlopen ( uk %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.A3.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity, place = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass

swith = 'http://ru.wikipedia.org/wiki/%%D0%%A7%%D0%%B5%%D0%%BC%%D0%%BF%%D0%%B8%%D0%%BE%%D0%%BD%%D0%%B0%%D1%%82_%%D0%%A8%%D0%%B2%%D0%%B5%%D0%%B9%%D1%%86%%D0%%B0%%D1%%80%%D0%%B8%%D0%%B8_%%D0%%BF%%D0%%BE_%%D1%%84%%D1%%83%%D1%%82%%D0%%B1%%D0%%BE%%D0%%BB%%D1%%83_%s/%s'
for offset in range (2011, 2012, 1) :
    try:
        data = urllib.request.urlopen ( swith %(offset, offset+1)).read()
        data = data.decode()
        data = re.sub('&nbsp;',' ', data)
        title = data.split("""<h2><span class="mw-headline" id=".D0.9A.D0.BB.D1.83.D0.B1.D1.8B-.D1.83.D1.87.D0.B0.D1.81.D1.82.D0.BD.D0.B8.D0.BA.D0.B8">Клубы-участники""")
        table = re.findall('<table.*?>(.*?)<\/table>', title[1], re.DOTALL)
        items_tr = re.findall(r"<tr.*?>\s*(.*?)\s*</tr.*?>", table[0], re.DOTALL)
        for i in  items_tr[1:]:

            club, city, stadium, capacity = re.findall(r'<td.*?>(.*?)<\/td>', i , re.DOTALL)
            item = {
			 'club' : club,
			 'city' : city,
			 'stadium' : stadium,
			 'capacity' : capacity,
                'year' : offset
			 }

        item_data.append(item)
    except: pass


print (item_data[0]['club'])
print (item_data[-1]['stadium'])

print (item_data[-1]['club'])
