import re

date1 = "16/12/2016"
date2 = "16-12-2016"
date3 = "16 Dec 2016"
date4 = "16 December 2016"
date5 = "12/30/2016"

#year
year = re.search('([0-9]{4})$', date1)
print(year)
year1 = re.search('([0-9]{4})$', date2)
print(year1)
year2 = re.search('([0-9]{4})$', date3)
print(year2)
year3 = re.search('([0-9]{4})$', date4)
print(year3)
year4 = re.search('([0-9]{4})$', date5)
print(year4)

#month


#day
