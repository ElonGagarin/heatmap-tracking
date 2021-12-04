import cv2
import numpy as np


def background(path, max_frame=10):

    c = cv2.VideoCapture(path)
    _,f = c.read()

    avg1 = np.float32(f)
    avg2 = np.float32(f)

    while(1):
        _,f = c.read()

        cv2.accumulateWeighted(f,avg1,0.1)
        cv2.accumulateWeighted(f,avg2,0.01)

        res1 = cv2.convertScaleAbs(avg1)
        res2 = cv2.convertScaleAbs(avg2)

        cv2.imshow('img',f)
        cv2.imshow('avg1',res1)
        cv2.imshow('avg2',res2)
        k = cv2.waitKey(20)

        if k == max_frame:
            break

    cv2.destroyAllWindows()
    c.release()

def background_2(path, max_frame=50):
    import numpy as np
    import cv2
    from skimage import data, filters

    # Open Video
    cap = cv2.VideoCapture(path)

    # Randomly select 25 frames
    frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=max_frame)

    # Store selected frames in an array
    frames = []
    i = 0
    for fid in frameIds:
        i+=1
        print(i)
        cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
        ret, frame = cap.read()
        frames.append(frame)

    # Calculate the median along the time axis
    medianFrame = np.median(np.array(frames), axis=0).astype(dtype=np.uint8)

    # Display median frame
    cv2.imwrite('frame_back.jpg', medianFrame)
    cv2.waitKey(0)



background_2('input.mp4')