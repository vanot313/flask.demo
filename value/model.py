import torch
import torch.nn as nn


class model(nn.Module):
    def __init__(self):
        super(model, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 20, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(20),
            nn.ReLU()
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(20, 20, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(20),
            nn.ReLU()
        )
        self.maxpool = nn.MaxPool2d(kernel_size=2, stride=1, padding=1)
        self.droput1 = nn.Dropout(0.5)
        self.dense1 = nn.Linear(3120, 3120)
        self.droput2 = nn.Dropout(0.5)
        self.dense2 = nn.Linear(3120 * 2, 5)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.maxpool(out)
        out = torch.flatten(out)
        out1 = self.droput1(out)
        out = self.dense1(out)
        out = torch.cat((out1, out), 0)
        out = self.droput2(out)
        out = self.dense2(out)

        return out
