import numpy as np
from skimage.measure import compare_mse

def getMSE(alpha_val, gt_img):
    gt_img = np.double(gt_img)
    gt_img = gt_img[:, :, 0]
    mse_val = compare_mse(alpha_val, gt_img)
    return mse_val
