from ultralytics import YOLO

data_path = "config.yaml"
trained_model_path = "models/best-11-12.pt"

model = YOLO('yolov8n-pose.pt') #load a pretrained model

model.train(data=data_path, epochs=20, imgsz=640, max_det=2)

# metrics
# mAP: mean average precision with a certain IoU (intersection over unit)
#model = YOLO(trained_model_path)
#metrics = model.val(data=data_path,  imgsz=640, max_det=2) 

#print(metrics.box.maps)