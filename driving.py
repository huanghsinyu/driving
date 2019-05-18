c = input('你是哪國人？')
a = input('你幾歲？')
a = int(a)
if c == '台灣':
	if a >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')
elif c == '美國':
	if a >= 16:
		print('你可以考駕照')
	else:
		print('你不能考駕照')
else:
	print('只能輸入台灣或美國')