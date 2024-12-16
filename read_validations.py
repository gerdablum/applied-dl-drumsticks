import pandas as pd
from ultralytics import YOLO

run_no = 9
data_path = "config.yaml"
MODEL_PATH = f"runs/pose/train{run_no}/weights/best.pt"

# metrics
model = YOLO(MODEL_PATH)
metrics = model.val(data=data_path,  imgsz=640, max_det=2) 

print(metrics.box.maps)