string = ""
bar = 1

x = int(input("Masukkan angka :"))
no = 1
# Looping Baris
while bar <= x:
	kol = bar
	# Looping Kolom
	while kol > 0:
		string = string + " " + str(no) + " "
		kol = kol - 1

	string = string + "\n"
	bar = bar + 1
	no = no+1
print (string)
