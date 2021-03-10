import torch
from load_data import load_data
from model import model
import time

device = torch.device("cpu")
epoch_num = 200
lr = 0.001
batch_size = 1

base_path = './dataset/input_data/'

net = model().to(device)
net = torch.load('./save_model/360.pkl')
train_loader = load_data(base_path, batch_size)
# loss
loss_func = torch.nn.L1Loss()
# 优化器
optimizer = torch.optim.SGD(net.parameters(), lr=lr,
                            momentum=0.9, weight_decay=5e-4)

scheduler = torch.optim.lr_scheduler.StepLR(optimizer,
                                            step_size=20,
                                            gamma=0.8)

for epoch in range(1500):
    print(" epoch is ", epoch)
    correct = 0
    loss_mean = 0
    net.train()
    start = time.time()

    for i, data in enumerate(train_loader):
        inputs, labels = data

        p = net(inputs)

        loss = loss_func(p, labels[0])
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss_mean += loss

    scheduler.step()
    print('time =', time.time() - start, 'epoch=', epoch, 'loss=', loss_mean / i)
    if epoch % 20 == 0:
        torch.save(net, './save_model/' + str(epoch) + '.pkl')
