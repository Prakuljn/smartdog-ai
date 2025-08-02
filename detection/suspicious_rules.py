# Very simple rule-based placeholder; expand for your logic

# E.g., suspicious if person + knife or person + baseball bat, or person after 20:00
SUSPICIOUS_COMBINATIONS = [
    ("person", "knife"),
    ("person", "baseball bat")
]

def check_suspicious(detections):
    detected_classes = [d['class'] for d in detections]
    for combo in SUSPICIOUS_COMBINATIONS:
        if all(obj in detected_classes for obj in combo):
            return True, f"Suspicious activity detected: {' & '.join(combo)}"
    return False, ""
