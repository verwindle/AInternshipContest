from lib.includes import *
from lib import *


def remove_rgb(mask):
    mask = np.sum([mask[:,:,i] for i in range(mask.shape[2])], axis=0)

    return mask


def pred_masks_dices(model, val_img, val_masks):
    masks_pred_score = []

    for img, mask in tqdm(zip(val_img, val_masks)):
        img_arr = np.array(img)
        results = model.detect([img_arr])
        r = results[0]
        pred_mask = r['masks']
        pred_mask = remove_rgb(pred_mask)
        dice = get_dice(pred_mask, mask)
        masks_pred_score.append(dice)
        
    return np.array(masks_pred_score)


def show_test_with_masks(model, test_img):
    for img in tqdm(test_img):
        img_arr = np.array(img)
        results = model.detect([img_arr], verbose=1)
        r = results[0]
        mask = r['masks']
        mask = remove_rgb(mask)
        print('CONFIDENCE_SCORE\t', r['scores'])
        show_img_with_mask(img, mask)    