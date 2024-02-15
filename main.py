# app.py
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_from_directory,
)
from PIL import Image
from service import detect_objects_on_image

app = Flask(__name__, template_folder="templates")


@app.route("/public/<path:path>")
def send_report(path):
    return send_from_directory("public", path)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def detect():
    results = {"error": "No image provided."}
    calories_sum, fat_sum, protein_sum, carb_sum = 0, 0, 0, 0
    if request.method == "POST":
        image_file = request.files.get("image")
        if image_file:
            img = Image.open(image_file)
            results, calories_sum, fat_sum, protein_sum, carb_sum = (
                detect_objects_on_image(img)
            )
        else:
            results = {"error": "Image file not found in the request."}
    return jsonify(
        {
            "results": results,
            "calories": calories_sum,
            "protein_sum": protein_sum,
            "fat_sum": fat_sum,
            "carb_sum": carb_sum,
        }
    )


if __name__ == "__main__":
    app.run(port=5000)
