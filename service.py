from ultralytics import YOLO
from const import (
    calorie_per_unit,
    calorie_per_sq_inch,
    food_translation_simplified,
    calorie_per_100_grams,
    nutrient_per_unit,
    thai_calorie_per_unit,
    thai_calorie_per_sq_inch,
    thai_food_translation_simplified,
    thai_calorie_per_100_grams,
    thai_nutrient_per_unit,
)


def get_calorie(class_name, real_food_area):
    if class_name in thai_calorie_per_unit:
        return thai_calorie_per_unit[class_name]
    else:
        return round((thai_calorie_per_sq_inch[class_name] * real_food_area), 2)


def get_nutrient(class_name, real_food_area):
    if class_name in thai_nutrient_per_unit:
        return thai_nutrient_per_unit[class_name]
    else:
        calories = round((thai_calorie_per_sq_inch[class_name] * real_food_area), 2)
        fat = thai_calorie_per_100_grams[class_name]["fat"]
        protein = thai_calorie_per_100_grams[class_name]["protein"]
        carbs = thai_calorie_per_100_grams[class_name]["carbs"]
        calories_per_100_grams = thai_calorie_per_100_grams[class_name]["calories"]
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


def estimate_new_masked_plate_pixels(
    original_width, original_height, new_width, new_height, original_masked_plate_pixels
):
    original_total_pixels = original_width * original_height
    original_ratio = original_masked_plate_pixels / original_total_pixels
    new_total_pixels = new_width * new_height
    estimated_masked_plate_pixels = new_total_pixels * original_ratio

    return int(estimated_masked_plate_pixels)


def detect_objects_on_image(buf, w, h):
    model = YOLO("v8xseg.pt")
    results = model(buf)
    original_masked_plate_pixels = 1401143
    real_plate_area = 113.04  # sq inch

    masked_plate_pixels = estimate_new_masked_plate_pixels(
        3264, 2458, w, h, original_masked_plate_pixels
    )
    picture_ratio = 7990272 / (w * h)
    print(picture_ratio)
    ratio_masked_to_total = masked_plate_pixels / (w * h)
    real_plate_area = real_plate_area * ratio_masked_to_total
    pixels_per_inch_sq = ((masked_plate_pixels) / real_plate_area) / picture_ratio

    print(pixels_per_inch_sq)
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
            english_class_name = thai_food_translation_simplified[class_name]
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
