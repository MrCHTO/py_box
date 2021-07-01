import mindspore.dataset as mds
data_path = "C:\\GitBox\\py_box\\Mindspore\\Learn\\datasets\\MNIST_Data\\train"
minist_ds = mds.MindDataset(data_path)
for a in minist_ds:
    print(a, end=" ")
    break
