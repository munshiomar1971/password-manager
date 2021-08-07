from cryptography.fernet import Fernet

# master password is master

def load_key():
	file = open("key.key", "rb")
	key = file.read()
	file.close()
	return key



master_pwd = input("What is the master password? ")

if master_pwd == "master":

	key = load_key() + master_pwd.encode()
	fer = Fernet(key)



	def veiw():
		with open('passwords.txt', 'r') as f:
			for line in f.readlines():
				data = line.rstrip()
				user, passw = data.split("|")
				print("User:", user, "Password:", fer.decrypt(passw.encode()).decode())


	def add():
		name = input("Account Name: ")
		pwd = input("Password: ")

		with open('passwords.txt', 'a') as f:
			f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")




	while True:

		mode = input("Would you like to add a new password or veiw existing ones? (veiw, add), press q to quit ").lower()

		if mode == "q":
			break 


		if mode == "veiw":
			veiw()

		elif mode == "add":
			add()
		else:
			print("you did something wrong")
			continue

else:
	print("wrong password")