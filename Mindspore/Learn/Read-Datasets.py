import mindspore.dataset as ds
data_path = './datasets/MNIST_Data/train/train-images.idx3-ubyte'
minist_ds = ds.MindDataset(data_path)
for data in minist_ds:
    print(data)
    break;
