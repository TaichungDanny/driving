country = input("請輸入國家:")
age = int(input("請輸入年齡:"))
if country == "台灣":
	if age >= 18:
		print("可以考駕照!")
	else:
		print("不能考駕照!")