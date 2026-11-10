import cv2

def absolute_difference(image, reference):
    if image.shape != reference.shape:
        raise ValueError("image and reference must have identical dimensions")
    return cv2.absdiff(image, reference)
