import pyshorteners

#Jav Code
X = "\033[0;37;40m"
DG = "\033[1;30;40m"
R = "\033[1;31;40m"
G = "\033[1;32;40m"
Y = "\033[1;33;40m"
B = "\033[1;34;40m"
M = "\033[1;35;40m"
C = "\033[1;36;40m"
W = "\033[1;37;40m"
shortme = pyshorteners.Shortener()

print(W+"    ["+R+"+"+W+"]     URL Shortener    ["+R+"+"+W+"]")
print(W+"    ["+R+"+"+W+"] Subscribe "+Y+"Mbah beluk"+W+" ["+R+"+"+W+"]\n")
url = input("Your URL "+R+"> "+W)
fake = input("Fake URL "+R+"> "+W)
print("Contoh "+R+":"+W+" how-to-get-free-coin")
rantai = input("Rantai url "+R+"> "+W)
hasil = shortme.tinyurl.short(url)
tanpahttp = hasil[7:]
print("Your link "+R+": "+Y+fake+"-"+rantai+"@"+tanpahttp+X)
