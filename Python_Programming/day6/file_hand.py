import livejson
std = livejson.File("student.json")
"""
{
"1" : {"name" : "Tushar" , "prn" : "1" , "address" : {"city" : "Pune"}}
"2" : {"name" : "Tushar" , "prn" : 2 , "address" : {"city" : "Pune"}}
}
"""
def add_student():
	temp = {}
	prn = int(input("Enter the PRN :"))
	temp["name"] = input("Enter the Name :")
	temp["address"] = {}
	temp["address"]["city"] = input("Enter the City :")
	std[str(prn)] = temp
def display_student():
	print(std)
def delete_student():
	prn = int(input("Enter the PRN to delete :"))
	for i in std.keys():
		if int(i) == prn:
			del std[str(prn)]
def menu():
	print("[1] Add Student")
	print("[2] Delete Student")
	print("[3] Display Student")
	print("[4] Exit")
while True:
	menu()
	ch = int(input("Enter the choice :"))
	if ch == 1:
		add_student()
	elif ch == 2:
		delete_student()
	elif ch == 3:
		display_student();
	elif ch == 4:
		break;
	else:
		print("Wrong choice")
