import csv

en_category = []
tw_category = []
tw_subCategoryContainer = []
tw_subCategory = []

with open("en_product.csv", newline="\n") as en_ikea :
	rows = csv.reader(en_ikea,delimiter=',')
	for row in rows :
		en_category.append(row[1])
with open("en_room.csv", newline="\n") as en_ikea :
	rows = csv.reader(en_ikea,delimiter=',')
	for row in rows :
		en_category.append(row[1])


with open("tw_nav.csv", newline="\n") as en_ikea :
	rows = csv.reader(en_ikea,delimiter=',')
	for row in rows :
		tw_category.append(row[1])
		tw_subCategory.append(row[3])
		tw_subCategoryContainer.append(row[2])
with open("tw_product.csv", newline="\n") as en_ikea :
	rows = csv.reader(en_ikea,delimiter=',')
	for row in rows :
		tw_category.append(row[1])
		tw_subCategory.append(row[3])
		tw_subCategoryContainer.append(row[2])

print ("============tw_category============")
for en in en_category :
	if en == "":
		continue
	for tw in tw_category :
		if en == tw :
			print (en)
			break
print ("======tw_subCategoryContainer======")
for en in en_category :
	if en == "":
		continue
	for tw in tw_subCategoryContainer :
		if en == tw :
			print (en)
			break
print ("===========tw_subCategory==========")
for en in en_category :
	if en == "":
		continue
	for tw in tw_subCategory :
		if en == tw :
			print (en)
			break
