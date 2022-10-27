import os

print(os.getcwd()) #returns the current working dir
print(os.getcwdb()) #returns cwd as a byte object

os.chdir('C:\\Users\\Dilshan\\Desktop\\code\\dir_for_chdir_testing') #changes dir
print(os.getcwd())

print(os.listdir()) #lists all files, folders inside cwd

os.mkdir('Test') #creates a new dir
os.rename('Test', 'test') #renames a dir

os.remove('Test.txt') #removes a file
os.rmdir('test') #removes a dir