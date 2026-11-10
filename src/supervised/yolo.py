"""YOLO training/inference entry points will be implemented after dataset conversion."""

def train_yolo(data_yaml, model_name="yolo11n.pt", epochs=50, image_size=640):
    try:
        from ultralytics import YOLO
    except ImportError as exc:
        raise RuntimeError("Install ultralytics to use YOLO: pip install ultralytics") from exc
    model = YOLO(model_name)
    return model.train(data=str(data_yaml), epochs=epochs, imgsz=image_size)

if __name__ == "__main__":
    print("Prepare a YOLO-format dataset YAML, then call train_yolo(...).")
