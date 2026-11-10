import cv2

def otsu_threshold(gray_image):
    if gray_image.ndim != 2:
        raise ValueError("Expected a grayscale image")
    _, mask = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return mask
