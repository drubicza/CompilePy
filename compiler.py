import os
import time
import marshal

banner="""\033[1;36m
     _  _
   _| || |_    \033[1;32m[+] Compiler Python [+]\033[1;36m
  |_  ..  _|
  |_      _| \033[1;31mContact : https://t.me/nndaid\033[1;36m
    |_||_|   \033[1;31mGithub  : https://github.com/nnda-id
"""

def py():
	try:
		os.system('clear')
		print(banner)
		a=input("\033[1;37mMasukan Nama File => \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("hasil_"+a,'w')
		d.write('import marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mFile Berhasil Tercompile: \033[1;36mhasil_"+a)
		print()
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: Pastikan File Yang Mau Di Compile Berada Di Folder Yang Sama, Dan Pastikan Anda Menginput File Dengan Benar")
		exit()

def py2():
	try:
		os.system('clear')
		print(banner)
		a=raw_input("\033[1;37mMasukan Nama File => \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("hasil_"+a,'w')
		d.write('import marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mFile Berhasil Tercompile: \033[1;36mhasil_"+a)
		print
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: Pastikan File Yang Mau Di Compile Berada Di Folder Yang Sama, Dan Pastikan Anda Menginput File Dengan Benar")
		exit()

os.system('clear')
print(banner + "\n\033[1;32m[1] Python3\n[2] Python2")
ask = input("\033[1;37m[?] Mau Compile Python Berapa => \033[1;32m")
if ask == '1':
	py()
elif ask == '2':
	py2()
else:
	print("\n\033[1;31m[!] Pilihanmu Salah")
