from collections import Counter, defaultdict
from sys import exit, argv
import pickle

def train():
	fp = open("text8","r")
	next_predict = defaultdict(Counter)

	prev = None
	ctr = 0
	for word in fp.read().split():
		ctr += 1
		if ctr%100000 == 0: print ("Processed {} words".format(ctr))
		next_predict[prev][word] += 1
		prev = word

	fp.close()
	print("Saving")
	output = open('out.pkl', 'wb')
	pickle.dump(next_predict,output)
	output.close()
	return next_predict

if len(argv) > 1:
	print("Loading")
	output = open(argv[1],"rb")
	next_predict = pickle.load(output)
	output.close()
else:
	print("Training")
	next_predict = train()


print("Done")
try:
	while 1:
		word = raw_input().strip()
		print (next_predict[word].most_common(5))
except KeyboardInterrupt:
	exit(0)