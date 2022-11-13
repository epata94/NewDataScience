import pickle

f = open("test.bin", "wb")
data = {1: 'python', 2: 'you need'}
pickle.dump(data,f)

f.close()