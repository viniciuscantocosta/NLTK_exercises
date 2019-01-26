text = input('Enter your text: ')

def hedge(text):
	textlist = text.split()
	crawler = 2
	for k in range(len(textlist)//2):
		textlist.insert(crawler, 'like')
		crawler += 3
	return ' '.join(textlist)

print(hedge(text))