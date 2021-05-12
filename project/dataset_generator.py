import numpy as np




def read_data(filename):
    out=[]
    with open(filename) as f:
        for line in f.readlines():
            out.append([line.strip()])
    return np.array(out)


if __name__=="__main__":
    DATASET='dataset.txt'
    LABELSET='label.txt'
    description=read_data(DATASET)
    label=read_data(LABELSET)
    filename='test_dataset'
    np.savez(filename,description=description,label=label)


