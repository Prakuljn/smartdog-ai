def generate_text_report(detections, suspicious_flag, suspicious_reason):
    objects = [d['class'] for d in detections]
    summary = f"Detected: {', '.join(objects)}."
    if suspicious_flag:
        summary += f" ALERT: {suspicious_reason}"
    return summary

def generate_json_report(detections, suspicious_flag, suspicious_reason):
    import datetime
    report = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "objects_detected": [d['class'] for d in detections],
        "suspicious": suspicious_flag,
        "reason": suspicious_reason
    }
    return report
