def read_pickle(pickle_path):
    import pickle
    with open(pickle_path, 'rb') as f:
        return pickle.load(f)


def save_pickle(data, pickle_path):
    import pickle
    with open(pickle_path, 'wb') as f:
        return pickle.dump(data, f)


def show_img(img):
    import matplotlib.pyplot as plt
    plt.imshow(img)
    plt.show()


def show_img_file(img_path):
    import matplotlib.pyplot as plt
    from PIL import Image
    import numpy as np

    img = np.array(Image.open(img_path))
    plt.imshow(img)
    plt.show()



def read_pc_from_ply(ply_path):
    from plyfile import PlyData
    import numpy as np

    ply = PlyData.read(ply_path)
    data = ply.elements[0].data
    x = data['x']
    y = data['y']
    z = data['z']
    return np.stack([x, y, z], axis=-1)

