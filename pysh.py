import os
import pathlib

print('\n'*100)
print('''
  _____             _____   _              _   _
 |  __ \           / ____| | |            | | | |
 | |__) |  _   _  | (___   | |__     ___  | | | |
 |  ___/  | | | |  \___ \  | '_ \   / _ \ | | | |
 | |      | |_| |  ____) | | | | | |  __/ | | | |
 |_|       \__, | |_____/  |_| |_|  \___| |_| |_|   Made by Nika Kereselidze
            __/ |
           |___/
''')
print('\n'*5)
print('Type command \'help\' to get a list of all commands with their functions\n')
print('\n')
def help():
	print('\n'*50)
	print('''\n
'help' === Print this menu\n
------------------------------------------------------------------------------------------\n
'cd' === Change the current directory to the provided directory if exists\n
------------------------------------------------------------------------------------------\n
'list' === Show all the files / folders in the current directory\n
------------------------------------------------------------------------------------------\n
'delete' === Delete files in the current directory if it exists\n
------------------------------------------------------------------------------------------\n
'deletedir' === Delete folders in the current directory if it exists\n
------------------------------------------------------------------------------------------\n
'clr' === Clear the terminal window\n
------------------------------------------------------------------------------------------\n
'cwd' === Print current working directory\n
------------------------------------------------------------------------------------------\n
'create' === Create a file\n
------------------------------------------------------------------------------------------\n
'createdir' === Create a folder\n
------------------------------------------------------------------------------------------\n
'nanotxt' === Open text editor 'nano'\n
''')
	b = input('Help Page ( 1 / 2 ) Do you want to see the next page? ( y | n ) -> ')
	if b == 'y':
		print('\n'*100)
		print('''\n
'read' === Read a file (Same as bash command : 'cat')\n
------------------------------------------------------------------------------------------\n
'quit' === Quit the utility\n
Help Page ( 2 / 2 )
''')
	elif b == 'n':
		pass
	else:
		print('You didn\'t choose a valid option')
def delete():
	b = input('Enter filename -> ')
	try:
		os.remove(b)
		print('File removed!')
	except FileNotFoundError:
		print(f'\'{b}\' file does not exist')
def deletedir():
	b = input('Enter folder name -> ')
	try:
		os.rmdir(b)
		print('Folder removed!')
	except FileNotFoundError:
		print(f'\'{b}\' folder does not exist')
def clr():
	print('\n'*100)
def cd():
	b = input('Enter path / folder -> ')
	try:
		os.chdir(b)
	except FileNotFoundError:
		print(f'\'{b}\' folder does not exist')
def cwd():
	print(os.getcwd())
def list():
	print('\n')
	list_iter = pathlib.Path()
	for iter in list_iter.iterdir():
		print(iter)
	print('\n')
def create():
	list_iter = pathlib.Path()
	for iter2 in list_iter.iterdir():
		iter = iter2
	b = input('Enter file name -> ')
	if b in str(iter):
		print('This file already exists')
	if b not in str(iter):
		open(b, 'a+')
def createdir():
	b = input('Enter folder name -> ')
	try:
		os.mkdir(b)
		print('Folder created!')
	except FileExistsError:
		print(f'\'{b}\' folder exists')
def read():
	b = input('Enter file name -> ')
	try:
		f = open(b, 'r')
		print('\n')
		print(f.read())
	except FileNotFoundError:
		print(f'\'{b}\': File does not exist')
def nanotxt():
	b = input('Enter file name (Only works if you have nano) -> ')
	os.system(f'nano {b}')
def runpy():
	b = input('Enter Python file name (Must have Python installed) -> ')
	try:
		os.system(f'python3 {b}')
	except FileNotFoundError:
		print(f'\'{b}\' File does not exist.')
while True:
	try:
		c = input(f'{os.getcwd()}-> ')
		if c == 'help':
			help()
		elif c == 'delete':
			delete()
		elif c == 'deletedir':
			deletedir()
		elif c == 'clr':
			clr()
		elif c == 'cd':
			cd()
		elif c == 'cwd':
			cwd()
		elif c == '':
			pass
		elif c == 'quit':
			print('Bye')
			break
		elif c == 'exit':
			print('Type \'quit\' to quit the utility')
		elif c == 'list':
			list()
		elif c == 'create':
			create()
		elif c == 'createdir':
			createdir()
		elif c == 'read':
			read()
		elif c == 'nanotxt':
			nanotxt()
		elif c == 'runpy':
			runpy()
		else:
			print(f'{c}: Unknown Command')
	except KeyboardInterrupt:
		print('Type \'quit\' to quit the utility')
		pass
