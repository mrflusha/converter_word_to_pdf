import os
import subprocess


path, path_to = input("Enter path:\n"),input("Enter path_to:\n")
print("docto.exe -f \"" + path + "\" -O \"" + path_to + "\" -T wdFormatPDF  -OX .pdf")

def convert(path, path_to):
	a = subprocess.Popen("docto.exe -f \"" + path + "\" -O \"" + path_to + "\" -T wdFormatPDF  -OX .pdf", stdout=subprocess.PIPE, shell=True)
	out = a.stdout.read()
	print(out)
	#print (out.decode('utf-8'))

convert(path, path_to)