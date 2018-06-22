from bs4 import BeautifulSoup
import csv

write_file = open("en_room.csv","w")
writer = csv.writer(write_file,delimiter=',')

writer.writerow(['URL','Category'])

main_url = "https://www.ikea.com"
with open("en_room_links.csv","r") as read_file :
	data = csv.reader(read_file)
	i = 0
	for _ in data :
		if i == 0 :
			i = i+1
			continue
		soup = BeautifulSoup(_[0],'html.parser')
		
		#print soup.prettify()
		url = main_url + soup.a["href"]
		#category = soup.a.string.encode('utf-8').strip()
		category = soup.h3.string.encode('utf-8').strip()
		writer.writerow([url,category])
		i = i + 1

