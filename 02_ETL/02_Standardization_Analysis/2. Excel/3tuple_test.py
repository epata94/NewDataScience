from datetime import date
my_date = (2013, 1, 1, 0, 0, 0)

print(my_date)

print(my_date[0:3])
print(*my_date[0:3])
date_cell = date(*my_date[0:3]).strftime \
					('%m/%d/%Y')
print(date_cell)
print("End")
#new_data = *my_date[0:3] <- Error 남