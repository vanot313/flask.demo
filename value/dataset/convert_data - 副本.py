import numpy as np
import glob

x = np.load('./save/1.npy')
y = np.load('./save1/1.npy')

print(x.shape)
print(y.shape)
y = np.expand_dims(y, 1)
save = np.concatenate((x, y), 1)
print(save.shape)
print(save)
print(y)

for i in range(1780):
    x = np.load('./save/' + str(i) + '.npy')
    y = np.load('./save1/' + str(i) + '.npy')
    y = np.expand_dims(y, 1)
    save = np.concatenate((x, y), 1)
    np.save('./input_data/' + str(i) + '.npy', save)
