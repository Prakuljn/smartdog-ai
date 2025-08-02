from ultralytics import YOLO
import cv2

class YoloDetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)
        self.class_names = self.model.names

    def detect(self, frame):
        results = self.model(frame)
        detections = []
        for r in results[0].boxes:
            det = {
                "class": self.class_names[int(r.cls)],
                "confidence": float(r.conf),
                "bounding_box": [int(x) for x in r.xyxy[0].tolist()]
            }
            detections.append(det)
        return detections

if __name__ == "__main__":
    from camera.capture import get_video_stream, read_frame
    det = YoloDetector()
    cap = get_video_stream()
    while True:
        frame = read_frame(cap)
        if frame is None:
            break
        detections = det.detect(frame)
        print(detections)
        cv2.imshow('YOLO Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
