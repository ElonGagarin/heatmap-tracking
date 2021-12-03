import cv2

def merg():
    first_frame = cv2.imread('frame_back.jpg')
    color_image = cv2.imread('frame_.jpg')

    # ret, mask = cv2.threshold(color_image, 130, color_image, cv2.THRESH_BINARY)

    # mask_inv = cv2.bitwise_not(mask)

    # img1_bg = cv2.bitwise_and(color_image,color_image,mask = mask)

    # img2_fg = cv2.bitwise_and(color_image,color_image,mask = mask_inv)

    result_overlay = cv2.addWeighted(first_frame, 0.7, color_image, 0.7, 0)

    cv2.imwrite('frame_back_fin.jpg', result_overlay)
