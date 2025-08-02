from camera.capture import get_video_stream, read_frame
from detection.yolo_detector import YoloDetector
from detection.suspicious_rules import check_suspicious
from nlp_gemini.report_generator import generate_text_report, generate_json_report
from dashboard.app import draw_detections
import cv2
import json

def main():
    cap = get_video_stream()
    det = YoloDetector()
    while True:
        frame = read_frame(cap)
        if frame is None:
            break
        detections = det.detect(frame)
        suspicious_flag, suspicious_reason = check_suspicious(detections)
        text_report = generate_text_report(detections, suspicious_flag, suspicious_reason)
        json_report = generate_json_report(detections, suspicious_flag, suspicious_reason)
        print(text_report)
        # Save alert JSON if suspicious
        if suspicious_flag:
            with open("data/output/alert_latest.json", "w") as f:
                json.dump(json_report, f, indent=2)
        # Show with overlays
        frame_disp = draw_detections(frame, detections, suspicious_flag, suspicious_reason)
        cv2.imshow('SmartWatchdog AI', frame_disp)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
