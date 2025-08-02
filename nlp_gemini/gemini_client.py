import requests

GEMINI_API_URL = "https://api.gemini.google.com/v1/generate"
GEMINI_API_KEY = ""

def query_gemini(prompt):
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(GEMINI_API_URL, headers=headers, json=body)
    resp_data = response.json()
    # Parsing may change based on Gemini's API output
    return resp_data.get("text", "")

def detections_to_nlp_prompt(detections, suspicious_flag, reason):
    det_str = ", ".join([d['class'] for d in detections])
    prompt = (
        f"Detected objects: {det_str}. Suspicious: {suspicious_flag}."
        f"Reason: {reason}. Write a security report for this frame."
    )
    return prompt

if __name__ == "__main__":
    # For testing
    dets = [{"class": "person"}, {"class": "knife"}]
    prompt = detections_to_nlp_prompt(dets, True, "person & knife")
    print(query_gemini(prompt))
