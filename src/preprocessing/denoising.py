import cv2

def denoise(image, method="median", kernel_size=3):
    if kernel_size % 2 == 0:
        raise ValueError("kernel_size must be odd")
    if method == "median":
        return cv2.medianBlur(image, kernel_size)
    if method == "gaussian":
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    raise ValueError("method must be 'median' or 'gaussian'")
