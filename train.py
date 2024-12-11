from ultralytics import YOLO

data_path = "C:/Users/alina/Master-Projects/applied-dl/applied-dl-drumsticks/config.yaml"
trained_model_path = "C:/Users/alina/Master-Projects/applied-dl/applied-dl-drumsticks/models/best-11-12.pt"

model = YOLO('yolov8n-pose.pt') #load a pretrained model

#model.train(data=data_path, epochs=5, imgsz=640, max_det=2)

# metrics
# mAP: mean average precision with a certain IoU (intersection over unit)
model = YOLO(trained_model_path)
metrics = model.val(data=data_path,  imgsz=640, max_det=2) 

print(metrics.box.maps)