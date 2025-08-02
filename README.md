suspicious-activity-detection/
│
├── camera/
│   ├── capture.py            # Camera/video stream capture logic
│   ├── utils.py              # Helper functions (e.g., frame conversion)
│
├── detection/
│   ├── yolo_detector.py      # YOLO object detection pipeline
│   ├── activity_model.py     # Pretrained activity recognition (CNN/LSTM/transformer)
│   ├── suspicious_rules.py   # Rules/config for flagging suspicious events
│
├── nlp_gemini/
│   ├── gemini_client.py      # Gemini LLM API or SDK wrapper
│   ├── report_generator.py   # Converts detections to NLP summaries and JSON reports
│
├── mcp_server/
│   ├── server.py             # Main MCP server (API endpoints for detection, reporting)
│   ├── session_manager.py    # Handles sessions, user/context management, logging
│
├── dashboard/
│   ├── app.py                # Frontend app (Tkinter, Streamlit, Flask, etc.)
│   ├── live_alerts.py        # Live alert overlay/rendering
│   ├── static/               # Static assets (CSS, icons)
│
├── config/
│   ├── yolo.yaml             # YOLO model configuration
│   ├── model.cfg             # Suspicious model/class settings
│   ├── system.env            # Environment variables (API keys, ports)
│
├── data/
│   ├── samples/              # Test images/videos
│   ├── output/               # Saved reports, alert frames
│
├── requirements.txt          # Python dependencies
├── README.md
│
└── main.py                   # Orchestrates full pipeline: camera -> detection -> NLP -> MCP -> dashboard
