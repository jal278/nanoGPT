import numpy as np
import pickle

vocab_size = 23916
vocab_size = 23913
vocab_size = 23925
vocab_size = 23936 #nearest multiple of 64
out_dict = {'vocab_size':vocab_size}

#a = np.fromfile("val.bin")
#print(a.max())
#print(a.min())

outfile = open("meta.pkl","wb")
pickle.dump(out_dict,outfile)

