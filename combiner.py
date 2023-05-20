import pickle

import numpy as np

first = pickle.load(open('data.pickle', 'rb'))
second = pickle.load(open('data2.pickle', 'rb'))

data_f = np.asarray(first['data'])
labels_f = np.asarray(first['labels'])
print(len(data_f))
print(len(labels_f))

data_s = np.asarray(second['data'])
labels_s = np.asarray(second['labels'])

print(len(data_s))
print(len(labels_s))

print(data_s.shape)
print(data_f.shape)
data_m = np.append(data_f,data_s, axis=0)
print(data_m.shape)
#data_m = data_f
#for x in data_s:
#    data_m = np.append(data_m, x)


labels_m = np.append(labels_f,labels_s)
print(data_f)
print(data_s)
print(data_m)
print(len(labels_m))
f = open('merged_data.pickle', 'wb')
pickle.dump({'data': data_m, 'labels': labels_m}, f)
f.close()
