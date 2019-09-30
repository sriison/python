

with open("srini.txt",mode='w') as f:
	f.write('\n testing')

with open("srini.txt", mode = 'r') as f:
    print(f.read())