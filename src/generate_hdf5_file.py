
import os
import glob
import h5py
import numpy as np
import cv2
from random import shuffle


def _get_images_address(subdir_path):
    """

    :param subdir_path:
    :return:
    """

    # TODO: sanity check for White list formats : {'png', 'jpg', 'jpeg', 'bmp'}

    path_format = subdir_path + '/*.jpg'
    return glob.glob(path_format)


def image_to_array(img_path, target_size):
    """

    :param img_path:
    :param target_size:
    :return:
    """

    img = cv2.imread(img_path)
    img = cv2.resize(img, target_size, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


def directory_iterator(data_path):
    """

    :param data_path:
    :return:
    """

    classes = []
    nb_samples = 0
    addresses = []
    count = 0
    for subdir in sorted(os.listdir(data_path)):
        subdir_path = os.path.join(data_path, subdir)

        if os.path.isdir(subdir_path):

            addrs = _get_images_address(subdir_path)
            nb_samples += len(addrs)
            addresses.append((addrs,count))
            count +=1
            classes.append(subdir)
    # nb_class = len(classes)
    # class_indices = dict(zip(classes, range(len(classes))))

    return addresses, classes, nb_samples


def _get_data_points(addresses, target_size):
    """

    :param addresses:
    :param target_size:
    :return:
    """

    data_points =[]
    for i in range(len(addresses)):
        img_addrs = addresses[i][0]
        img_label = addresses[i][1]
        for j in range(len(img_addrs)):
            img_path = img_addrs[j]
            img_array = image_to_array(img_path, target_size)
            data_points.append((img_array, img_label))
    shuffle(data_points)

    return data_points


def generate_hdf5_file(data_path, output_file_name, target_size=(225, 225)):
    """

    :param data_path:
    :param output_file_name:
    :param target_size:
    :return:
    """

    image_shape = target_size + (3,)
    hdf5_file = h5py.File(output_file_name + ".h5", 'w')
    addresses, classes, nb_samples = directory_iterator(data_path)

    X = np.zeros((nb_samples,) + image_shape)
    Y = np.zeros((1, nb_samples))

    data_points = _get_data_points(addresses, target_size)

    for k in range(len(data_points)):
        X[k] = data_points[k][0]
        Y[0][k] = data_points[k][1]

    hdf5_file["X"] = X
    hdf5_file["Y"] = Y
    hdf5_file["classes"] = classes


    hdf5_file.close()

if __name__=="__main__":
    generate_hdf5_file("/home/pallavi/Documents/personal/learning/ml/kaggle/cnn_experiment/data/train", "catvsdog_train")
