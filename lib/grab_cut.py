def expected_cropped(img_id, mask):
    # mask = masks[img_id][:,:,np.newaxis]
    mask = mask[:,:,np.newaxis]
    cropped_img = mask * img[img_id]
    return np.where((mask > 0), 255 - cropped_img, cropped_img)


def cropped_cig(img, roi ,mask):
    output = []
    height, width = (512, 512)
    bgdModel = np.zeros((1,65), np.float64)
    fgdModel = np.zeros((1,65), np.float64)
    area = tuple((roi[0][1], roi[0][3], roi[0][0], roi[0][2]))
    # that was unpleasant
    mask = mask.astype('uint8')
    
    cv2.grabCut(img, mask, area, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    cropped_img = img * mask[:,:,np.newaxis]
    output.append(cropped_img)
        
    return np.array(output)[0]
