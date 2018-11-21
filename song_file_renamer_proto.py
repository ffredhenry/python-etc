#First portion: find the targeted directory and change to it
#also would like to have autocomplete for directory names

bannedString = ")(*&^$%#@!"
protoString = "This* i^s a prototy)pe str@ing!"


for i in range(0, len(protoString)):
	print("Hello, World!")
	for j in range(0, len(bannedString)):
		if(protoString[i]  == bannedString[j]):
			print("found a <{}> at <{}>!".format(bannedString[j],i))

#protoString.find()