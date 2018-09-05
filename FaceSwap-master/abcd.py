import numpy as np, cv

img1 = cv.LoadImage(fn1, 0)
img2 = cv.LoadImage(fn2, 0)

h1, w1 = img1.height,img1.width
h2, w2 = img2.height,img2.width
vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
vis[:h1, :w1] = cv.GetMat(img1)
vis[:h2, w1:w1+w2] = cv.GetMat(img2)
vis2 = cv.CreateMat(vis.shape[0], vis.shape[1], cv.CV_8UC3)
cv.CvtColor(cv.fromarray(vis), vis2, cv.CV_GRAY2BGR)

cv.ShowImage("test", vis2)
cv.WaitKey()