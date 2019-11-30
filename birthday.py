from datetime import date

today = date.today()

date_of_birth = date(1994, 11, 21)

birthday = date(today.year, date_of_birth.month, date_of_birth.day)
days_until_birthday = (birthday-today).days
days_alive = (today-date_of_birth).days
secounds_alive = days_alive * 86400

print( 'Masz ' + str(days_alive) + ' dni !')
print('A tyle przeżyłeś sekund:' +str(secounds_alive))

if days_until_birthday > 0:
	print( 'Tyle ' + str(days_until_birthday) + ' dni do urodzin')
elif days_until_birthday == 0:
	print( 'Sto lat lamusie!')
else:
	print( 'Musisz czekać na przyszły rok na życzenia!')



