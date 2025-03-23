from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with Flask backend

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload", methods=["POST"])
def upload_file():
    if "image" not in request.files or "video" not in request.files:
        return jsonify({"error": "Both image and video are required"}), 400

    image = request.files["image"]
    video = request.files["video"]

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)

    image.save(image_path)
    video.save(video_path)

    # 🔧 Processing logic goes here (e.g., AI animation, etc.)

    output_video_url = f"http://127.0.0.1:5000/static/{video.filename}"  # Replace with actual output video

    return jsonify({"video_url": output_video_url})

if __name__ == "__main__":
    app.run(debug=True)
