import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

print ("\033[1;32matau silahkan Hubungi 085785650199")

username = 'noelalvaroo'      

password = 'bacot'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mAlhmdllh sudah masuk juga..", 

			sys.exit()



		else:

			print "\033[1;32Salah Cok... [?]\033[00m"

			print "log-in maneh...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
