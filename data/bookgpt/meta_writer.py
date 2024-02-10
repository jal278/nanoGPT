import numpy as np
import pickle

vocab_size = 23916
out_dict = {'vocab_size':vocab_size}

#a = np.fromfile("val.bin")
#print(a.max())
#print(a.min())

outfile = open("meta.pkl","wb")
pickle.dump(out_dict,outfile)

