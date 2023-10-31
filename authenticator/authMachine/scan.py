import sys

prefix = './logs/'
badUsers = ["john","fred", "j678"]
count = int(open('./count.txt', 'r').readlines()[0])

def setCount(number):
	counter = open('./count.txt', 'w')
	counter.write(str(number))
	
def usersLogged(userFile):
	file = open(prefix+userFile, 'r')
	lines = file.readlines()
	for line in lines:
		uname = line.split()[0]
		if uname in badUsers:
			if count >= 12:
				setCount(0)
				return True
			else:
				setCount(count + 1)
				return False
	setCount(0)
	return False
	
def timeCheck(file1, file2):
	time1 = int(file1.split("-")[1])
	time2 = int(file2.split("-")[1])
	if (time2 - time1) > 360:
		return True
	else:
		return False
	
expire = False
badUser = False
list = sys.argv[1].split('\n')
badUser = usersLogged(list[len(list)-1])
if len(list) >= 2:
	expire = timeCheck(list[len(list)-2], list[len(list)-1])
	
if expire or badUser:
	print('t')

