fp = open("text8","r")
text = fp.read()
fp.close()
next_predict = {}

prev = None
ctr = 0

for word in text.split():
	ctr += 1
	if ctr%100000 == 0: print("Processed " + str(ctr) + " words")
	if prev not in next_predict.keys():
		next_predict[prev] = {}
	if word in next_predict[prev]:
		next_predict[prev][word] += 1
	else:
		next_predict[prev][word] = 1
	prev = word

print("Done")
try:
	while 1:
		word = raw_input().strip()
		possibilities = next_predict.get(word)
		print (max(possibilities, key = lambda x:possibilities[x]))
except KeyboardInterrupt:
	exit(0)