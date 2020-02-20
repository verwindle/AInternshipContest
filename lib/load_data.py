from lib.includes import *
from lib import *


def load_train(path):
    img = np.array([cv2.imread(f"{path}{x}") for x in tqdm(os.listdir(path)[:20])])
    img_ids = np.array([int(x.split('.')[0]) for x in tqdm(os.listdir(path)[:20])])
    annotations = json.load(open(f"{path}../coco_annotations.json", "r"))
    masks = np.array([get_mask(img_id, annotations) for img_id in tqdm(img_ids)])
    print("loaded train to img, masks", img.shape)

    return (img, masks, annotations)


def load_val(path):
    val_img = np.array([cv2.imread(f"{path}{x}") for x in tqdm(os.listdir(path))])
    val_img_ids = np.array([int(x.split('.')[0]) for x in tqdm(os.listdir(path))])
    annotations = json.load(open(f"{path}../coco_annotations.json", "r"))
    val_masks = np.array([get_mask(img_id, annotations) for img_id in tqdm(val_img_ids)])
    print("loaded val images to img, masks", val_img.shape)

    return (val_img, val_masks, annotations)


def load_test(path):
    return np.array([cv2.imread(f'{path}{x}') for x in tqdm(os.listdir(path))])