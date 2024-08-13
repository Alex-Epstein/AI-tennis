from ultralytics import YOLO

model = YOLO('yolov8x') # using v8 not v9

model.predict('input_videos/input_video.mp4', save=True)