from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
import numpy as np
import torch
import os
from PIL import Image

import glob


def default_loader(path):
    return np.load(path)


train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465),
                         (0.2023, 0.1994, 0.2010)),
])


class Load_CNN_Dataset(Dataset):
    def __init__(self, base_path,
                 transform=None,
                 load=default_loader):
        super(Load_CNN_Dataset, self).__init__()
        self.path = sorted(glob.glob(base_path + '/*.*'))
        print(self.path)
        self.transform = transform
        self.loader = load

    def change_data(self, data):
        train_data = data[:, :data.shape[1] - 1]
        result_data = data[:, data.shape[1] - 1:data.shape[1]]
        return train_data, result_data

    def __getitem__(self, index):
        im_path = self.path[index]
        im_data = self.loader(im_path)
        train_data, result_data = self.change_data(im_data)
        train_data = np.expand_dims(train_data, 0)
        train_data = train_data.astype(np.float32)
        train_data = torch.from_numpy(train_data)
        result_data = result_data.squeeze()
        result_data = result_data.astype(np.float32)
        result_data = torch.from_numpy(result_data)

        return train_data, result_data

    def __len__(self):
        return len(self.path)


def load_data(base_path, batch_size):
    train_dataset = Load_CNN_Dataset(base_path,
                                     transform=train_transform)

    train_loader = DataLoader(dataset=train_dataset,
                              batch_size=batch_size,
                              shuffle=True,
                              num_workers=0)
    return train_loader


if __name__ == '__main__':
    load_data = load_data('./dataset/input_data/', 5)
