# app.py
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_from_directory,
)
from ultralytics import YOLO
import cv2
from const import (
    calorie_per_unit,
    calorie_per_sq_inch,
    food_translation_simplified,
    calorie_per_100_grams,
    nutrient_per_unit,
)

app = Flask(__name__, template_folder="templates")


def get_calorie(class_name, real_food_area):
    if class_name in calorie_per_unit:
        return calorie_per_unit[class_name]
    else:
        return round((calorie_per_sq_inch[class_name] * real_food_area), 2)


def get_nutrient(class_name, real_food_area):
    if class_name in nutrient_per_unit:
        return nutrient_per_unit[class_name]
    else:
        calories = round((calorie_per_sq_inch[class_name] * real_food_area), 2)
        fat = calorie_per_100_grams[class_name]["fat"]
        protein = calorie_per_100_grams[class_name]["protein"]
        carbs = calorie_per_100_grams[class_name]["carbs"]
        calories_per_100_grams = calorie_per_100_grams[class_name]["calories"]
        nutrient = calculate_nutrient(
            calories, calories_per_100_grams, fat, protein, carbs
        )
        return nutrient


def calculate_nutrient(real_calorie, calorie, fat, protein, carbs):
    gram = real_calorie / calorie
    real_fat = round((gram * fat), 2)
    real_protein = round((gram * protein), 2)
    real_carbs = round((gram * carbs), 2)
    return {
        "protein": real_protein,
        "carbs": real_carbs,
        "fat": real_fat,
    }


def translate_food_list(food_list, translation_dict):
    translated_list = []
    for food_group in food_list:
        group_translation = []
        for food_item in food_group:
            translated_item = translation_dict.get(food_item, food_item)
            group_translation.append(translated_item)
        translated_list.append(group_translation)
    return translated_list


def calculate_polygon_area(coords):
    n = len(coords)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    area = abs(area) / 2.0
    return area


@app.route("/public/<path:path>")
def send_report(path):
    return send_from_directory("public", path)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def detect():
    results = {"error": "No image provided."}
    calories_sum = 0
    if request.method == "POST":
        image_file = request.files.get("image")
        if image_file:
            img = cv2.imread(image_file)
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


def detect_objects_on_image(buf):
    model = YOLO("segment.pt")
    results = model(buf)
    masked_plate_pixels = 1401143
    real_plate_area = 113.04  # sq inch
    pixels_per_inch_sq = masked_plate_pixels / real_plate_area

    output = []
    calories_sum = 0
    fat_sum = 0
    protein_sum = 0
    carb_sum = 0
    for i, box in enumerate(results[0].boxes):
        if results[0].masks:
            points_rollers = results[0].masks[i].xy[0].astype(int)
            data_points = [tuple(elem) for elem in points_rollers]
            masked_food_pixels = calculate_polygon_area(data_points)
            class_id = box.cls[0].item()
            class_name = results[0].names[class_id]
            english_class_name = food_translation_simplified[class_name]
            real_food_area = masked_food_pixels / pixels_per_inch_sq
            food_calories = get_calorie(class_name, real_food_area)
            food_nutrients = get_nutrient(class_name, real_food_area)
            calories_sum += food_calories
            fat_sum += food_nutrients["fat"]
            protein_sum += food_nutrients["protein"]
            carb_sum += food_nutrients["carbs"]
            output.append(
                {
                    "name": english_class_name,
                    "calories": food_calories,
                    "protein": food_nutrients["protein"],
                    "carbs": food_nutrients["carbs"],
                    "fat": food_nutrients["fat"],
                }
            )
    return (
        output,
        round(calories_sum, 2),
        round(fat_sum, 2),
        round(protein_sum, 2),
        round(carb_sum, 2),
    )


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
