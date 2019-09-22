from os import system as o
from time import sleep as s
from marshal import dumps as d
from sys import version_info as v

x = raw_input if (v[0] == 2) else input
t = """\033[1;36m
     _  _
   _| || |_    \033[1;32m[+] Compiler Python [+]\033[1;36m
  |_  ..  _|
  |_      _| \033[1;31mContact : https://t.me/nndaid\033[1;36m
    |_||_|   \033[1;31mGithub  : https://github.com/nnda-id
"""

try:
    o('clear')
    print(t)
    a = x("\033[1;37mMasukan Nama File => \033[1;32m")
    with open(a,"r") as f:
        b = f.read()
    with open("hasil_" + a, "w") as f:
        f.write("import marshal\nexec(marshal.loads(" + repr(d(compile(b,'','exec'))) + "))")
    s(1.5)
    print("\033[1;32mFile Berhasil Tercompile: \033[1;36mhasil_" + a + "\n")

except KeyboardInterrupt:
    print("\n\033[1;31m[!] ERROR: Pastikan File Yang Mau Dikompilasi Berada Di Folder Yang Sama, Dan Pastikan Anda Menginput File Dengan Benar")
