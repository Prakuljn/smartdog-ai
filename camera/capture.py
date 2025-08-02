import cv2

def get_video_stream(source=0):
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video source: {source}")
    return cap

def read_frame(cap):
    ret, frame = cap.read()
    if not ret:
        return None
    return frame

if __name__ == "__main__":
    cap = get_video_stream()
    while True:
        frame = read_frame(cap)
        if frame is None:
            break
        cv2.imshow('Live Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
