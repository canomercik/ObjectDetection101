from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8n.pt') # nano medium large
rsults = model('Images/Image3.jpg', show=True)
cv2.waitKey(0)
