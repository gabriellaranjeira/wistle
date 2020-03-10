import os
import argparse
banner = """
	 ____    __    ____  __       _______.___________. __       _______ 
	\   \  /  \  /   / |  |     /       |           ||  |     |   ____|
	 \   \/    \/   /  |  |    |   (----`---|  |----`|  |     |  |__   
	  \            /   |  |     \   \       |  |     |  |     |   __|  
	   \    /\    /    |  | .----)   |      |  |     |  `----.|  |____ 
	    \__/  \__/     |__| |_______/       |__|     |_______||_______|
		                                                                                                                                
"""
def user():
	return os.path.expanduser("~/.bashrc")
def setColor(color):
	if(color == "red"):
		colorb = '\033[31m'
	elif(color == "green"):
		colorb = '\033[32m'
	elif(color == "blue"):
		colorb = '\033[34m'
	elif(color == "cyan"):
		colorb = '\033[36m'
	elif(color == "magenta"):
		colorb = '\033[35m'
	elif(color == "yellow"):
		colorb = '\033[33m'
	elif(color == "black"):
		colorb = '\033[30m'
	elif(color == "yellow"):
		colorb = '\033[33m'
	elif(color == "white"):
		colorb = '\033[37m'
	else:
		print "[X] Color not exists! use wistle -h"
	original = '\033[0;0m'
	
	fData = colorb
	return fData
	
def getBash(dirBash, tipe):
	try:
		arq = open(dirBash, "r")
	except IOError:
		print "Error open bash file"
		os._exit(0)
	finally:
		lines = len(arq.readlines())
		arq.seek(0)
		bashrc = []
		for x in xrange(0, int(lines)):
			bashrc.append(arq.readline())
			if(tipe == "art" and bashrc[x][:4] == "echo"):
				bashrc[x] = ""
		arq.close()
		bashstr = ""
		for x in bashrc:
			bashstr += x
		print "[+] Getting Bash..."
		return bashstr
def getArt(art, co):
	try:
		arq = open(art, "r")
	except IOError:
		print "Error open file "
		os._exit(0)
	finally:
		if(co != ""):		
			color = setColor(co)
		else:
			color = ""
		lines = len(arq.readlines())
		arq.seek(0)
		art = {}
		for x in range(0, int(lines)):
			art[x] = "echo -e '"+color+" "+str(arq.readline().strip("\n"))+"' \n"
		arq.close()
		artstr = ""
		for x in xrange(0, int(lines)):
			artstr += art[x]
		print "[+] Getting your content..."
		return artstr

def alias(command, name):
	print "[+] Adjusting command..."
	final = "alias "+name+"='"+command+"' \n"
	return final
	

def writeBash(dirBash,bash, data, tipe):
	try:
		arq = open(dirBash, "w")
	except IOError:
		print "Error read  your .bashrc"
	finally:
		if(tipe == "art"):
			command = ""
			print "[+] Writing data..."
			final = str(bash)+str(data)
			arq.write(final)
			arq.close()
			print "[+] Sucefull, please close and open new terminal!"
def writeCommand(dirBash,bash,data):
	try:
		arq = open(dirBash, "w")
	except IOError:
		print "Error write .bashrc"
	finally:
			print "[+] Writing data..."
			final = str(bash) + str(data)
			arq.write(final)
			arq.close()
			print "[+] Sucefull, please close and open new terminal!"
def main():
	os.system("command clear")
	print banner
	parse = argparse.ArgumentParser()
	parse.add_argument('-file', action = 'store', dest='file', required = False, help = 'File of the data')
	parse.add_argument('-cmd', action = 'store', dest = 'cmd', required = False, help = 'Command paragraph realize the shortcut')
	parse.add_argument('-name', action = 'store', dest = 'name', required = False, help = 'shortcut of the command')
	parse.add_argument('-color', action = 'store', dest = 'color', required = False, help = 'Color of the art in terminal, \n Colors: red, \ngreen, \nblue, \ncyan, \nmagenta, \nyellow, \nblack, \nwhite \n')
	arg = parse.parse_args()
	if(arg.color == None):
		arg.color = ""
	if(arg.file == None and arg.cmd == None and arg.name == None):
		print "[X]use : wistle -file=exemple.txt -color=blue or\nuse : wistle -name=wistle -cmd=python /opt/wistle.py1"
		os._exit(0)
	elif(arg.cmd != None):
		if(arg.file != None):
			print "[X]use : wistle -file=exemple.txt -color=blue or\nuse : wistle -name=wistle -cmd=python /opt/wistle.py"
			os._exit(0)
		writeCommand(user(),getBash(user(), "alias"),alias(str(arg.cmd),str(arg.name)))
		os._exit(0)
	elif(arg.file != None):
		if(arg.cmd != None):
			print "[X]use : wistle -file=exemple.txt -color=blue or\nuse : wistle -name=wistle -cmd=python /opt/wistle.py"
			os._exit(0)
		writeBash(user(), getBash(user(), "art"), getArt(str(arg.file), str(arg.color)), "art")
		os._exit(0)
			
	
main()
