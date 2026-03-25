from ultralytics import YOLO



model = YOLO("yolo26n.pt")

results = model.train(data="dataset/dataset.yaml", epochs=3)
