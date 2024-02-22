calorie_per_unit = {
    "arancia": 45,
    "torta_ananas": 230,
    "torta_cioccolato_e_pere": 230,
    "torta_crema": 230,
    "torta_crema_2": 230,
    "torta_salata_-alla_valdostana-": 230,
    "torta_salata_3": 230,  # Assuming similar to above
    "torta_salata_rustica_-zucchine-": 125,
    "torta_salata_spinaci_e_ricotta": 120,
    "banane": 88,
    "pane": 130,
    "yogurt": 60,
    "budino": 120,
}
calorie_per_sq_inch = {
    "arrosto": 2.5,  # Example adjustment for a dense meat dish
    "arrosto_di_vitello": 10,  # Slightly higher for veal
    "bruscitt": 8,  # A specific meat dish, assuming higher density
    "carote": 0.4,
    "cavolfiore": 0.3,
    "cibo_bianco_non_identificato": 1.5,  # Arbitrary value
    "cotoletta": 12,  # Fried meat, assuming higher because of frying
    "crema_zucca_e_fagioli": 1.2,  # Cream soup, lighter
    "fagiolini": 0.4,
    "finocchi_gratinati": 0.7,  # Adjusted down for a vegetable dish
    "finocchi_in_umido": 0.7,  # Similarly adjusted
    "focaccia_bianca": 2.0,  # Bread, assuming a bit denser
    "guazzetto_di_calamari": 1.5,  # Seafood, lighter
    "insalata_mista": 0.2,  # Very light, mostly water content
    "lasagna_alla_bolognese": 9,  # Pasta dish, but with layers and meat
    "mandarini": 0.5,
    "medaglioni_di_carne": 8,
    "mele": 0.5,
    "merluzzo_alle_olive": 1.7,  # Fish dish, assuming lighter than meat
    "minestra": 1.0,  # Soup, lighter
    "minestra_lombarda": 1.1,  # Similar to above
    "orecchiette_-ragu-": 3.5,  # Pasta, as per your guideline
    "passato_alla_piemontese": 1.1,
    "pasta_bianco": 3.5,  # Aligning with your pasta calorie density
    "pasta_cozze_e_vongole": 3.5,
    "pasta_e_ceci": 3.5,
    "pasta_e_fagioli": 3.5,
    "pasta_mare_e_monti": 3.5,
    "pasta_pancetta_e_zucchine": 3.5,
    "pasta_pesto_besciamella_e_cornetti": 3.5,
    "pasta_ricotta_e_salsiccia": 3.5,
    "pasta_sugo": 3.5,
    "pasta_sugo_pesce": 3.5,
    "pasta_sugo_vegetariano": 3.5,
    "pasta_tonno": 3.5,
    "pasta_tonno_e_piselli": 3.5,
    "pasta_zafferano_e_piselli": 3.5,
    "patate-pure": 1.3,  # Mashed potatoes, assuming lighter
    "patate-pure_prosciutto": 1.5,
    "patatine_fritte": 2.2,  # Fries, assuming the oil adds calories
    "pere": 0.5,
    "pesce_-filetto-": 1.7,
    "pesce_2_-filetto-": 1.7,
    "piselli": 0.4,
    "pizza": 2.5,  # Assuming a higher density because of toppings
    "pizzoccheri": 3.5,  # Pasta dish
    "polpette_di_carne": 6,
    "riso_bianco": 1.2,  # Rice, assuming it's less dense than pasta
    "riso_sugo": 1.4,
    "roastbeef": 2.5,
    "rosbeef": 2.5,
    "rucola": 0.1,
    "salmone_-da_menu_sembra_spada_in_realta-": 1.8,
    "scaloppine": 2.7,
    "spinaci": 0.3,
    "stinco_di_maiale": 6,
    "strudel": 2.0,
    "zucchine_impanate": 1.8,
    "zucchine_umido": 0.7,
}
food_translation_simplified = {
    "arancia": "orange",
    "arrosto": "roast",
    "arrosto_di_vitello": "veal roast",
    "banane": "bananas",
    "bruscitt": "specific meat dish",
    "budino": "pudding",
    "carote": "carrots",
    "cavolfiore": "cauliflower",
    "cibo_bianco_non_identificato": "unidentified white food",
    "cotoletta": "fried meat",
    "crema_zucca_e_fagioli": "cream soup",
    "fagiolini": "green beans",
    "finocchi_gratinati": "potatoes",
    "finocchi_in_umido": "potatoes",
    "focaccia_bianca": "focaccia",
    "guazzetto_di_calamari": "seafood dish",
    "insalata_mista": "mixed salad",
    "lasagna_alla_bolognese": "lasagna",
    "mandarini": "mandarins",
    "medaglioni_di_carne": "meat dish",
    "mele": "apples",
    "merluzzo_alle_olive": "fish dish",
    "minestra": "soup",
    "minestra_lombarda": "soup",
    "orecchiette_-ragu-": "pasta dish",
    "pane": "bread",
    "passato_alla_piemontese": "soup",
    "pasta_bianco": "pasta",
    "pasta_cozze_e_vongole": "pasta",
    "pasta_e_ceci": "pasta",
    "pasta_e_fagioli": "pasta",
    "pasta_mare_e_monti": "pasta",
    "pasta_pancetta_e_zucchine": "pasta",
    "pasta_pesto_besciamella_e_cornetti": "pasta",
    "pasta_ricotta_e_salsiccia": "pasta",
    "pasta_sugo": "pasta",
    "pasta_sugo_pesce": "pasta",
    "pasta_sugo_vegetariano": "pasta",
    "pasta_tonno": "pasta",
    "pasta_tonno_e_piselli": "pasta",
    "pasta_zafferano_e_piselli": "pasta",
    "patate-pure": "mashed potatoes",
    "patate-pure_prosciutto": "mashed potatoes with ham",
    "patatine_fritte": "fries",
    "pere": "pears",
    "pesce_-filetto-": "fish fillet",
    "pesce_2_-filetto-": "fish fillet",
    "piselli": "peas",
    "pizza": "pizza",
    "pizzoccheri": "pasta dish",
    "polpette_di_carne": "meatballs",
    "riso_bianco": "rice",
    "riso_sugo": "rice dish",
    "roastbeef": "roast beef",
    "rosbeef": "roast beef",
    "rucola": "arugula",
    "salmone_-da_menu_sembra_spada_in_realta-": "fish dish",
    "scaloppine": "meat dish",
    "spinaci": "spinach",
    "stinco_di_maiale": "pork dish",
    "strudel": "pastry",
    "torta_ananas": "cake",
    "torta_cioccolato_e_pere": "cake",
    "torta_crema": "cake",
    "torta_crema_2": "cake",
    "torta_salata_-alla_valdostana-": "meat pie",
    "torta_salata_3": "meat pie",
    "torta_salata_rustica_-zucchine-": "meat pie",
    "torta_salata_spinaci_e_ricotta": "meat pie",
    "yogurt": "yogurt",
    "zucchine_impanate": "zucchini dish",
    "zucchine_umido": "zucchini dish",
}
nutrient_per_unit = {
    "arancia": {
        "protein": 2,
        "carbs": 0,
        "fat": 1,
    },
    "torta_ananas": {
        "protein": 1.7,
        "carbs": 40,
        "fat": 6,
    },
    "torta_cioccolato_e_pere": {
        "protein": 1.7,
        "carbs": 40,
        "fat": 6,
    },
    "torta_crema": {
        "protein": 1.7,
        "carbs": 40,
        "fat": 6,
    },
    "torta_crema_2": {
        "protein": 1.7,
        "carbs": 40,
        "fat": 6,
    },
    "torta_salata_-alla_valdostana-": {
        "protein": 1.7,
        "carbs": 40,
        "fat": 6,
    },
    "torta_salata_3": {
        "protein": 1.7,
        "carbs": 40,
        "fat": 6,
    },  # Assuming similar to above
    "torta_salata_rustica_-zucchine-": {
        "protein": 1.7,
        "carbs": 40,
        "fat": 6,
    },
    "torta_salata_spinaci_e_ricotta": {
        "protein": 1.7,
        "carbs": 40,
        "fat": 6,
    },
    "banane": {
        "protein": 1.1,
        "carbs": 23,
        "fat": 0.3,
    },
    "pane": {
        "protein": 4.5,
        "carbs": 25,
        "fat": 3.2,
    },
    "yogurt": {
        "protein": 10,
        "carbs": 3.6,
        "fat": 0.4,
    },
    "budino": {
        "protein": 3.2,
        "carbs": 20,
        "fat": 3.2,
    },
}
calorie_per_100_grams = {
    "arrosto": {
        "calories": 155,
        "protein": 2,
        "carbs": 0,
        "fat": 1,
    },
    "arrosto_di_vitello": {
        "calories": 155,
        "protein": 2,
        "carbs": 0,
        "fat": 1,
    },
    "bruscitt": {
        "calories": 310,
        "protein": 2,
        "carbs": 0,
        "fat": 1,
    },
    "carote": {
        "calories": 41,
        "protein": 0.9,
        "carbs": 9.6,
        "fat": 0.2,
    },
    "cavolfiore": {
        "calories": 25,
        "protein": 1.9,
        "carbs": 4.9,
        "fat": 0.3,
    },
    "cibo_bianco_non_identificato": {
        "calories": 100,
        "protein": 0,
        "carbs": 25,
        "fat": 0,
    },
    "cotoletta": {
        "calories": 250,
        "protein": 20,
        "carbs": 15,
        "fat": 18,
    },
    "crema_zucca_e_fagioli": {
        "calories": 120,
        "protein": 3,
        "carbs": 18,
        "fat": 4,
    },
    "fagiolini": {
        "calories": 31,
        "protein": 2,
        "carbs": 7,
        "fat": 0.2,
    },
    "finocchi_gratinati": {
        "calories": 120,
        "protein": 3,
        "carbs": 17,
        "fat": 5,
    },
    "finocchi_in_umido": {
        "calories": 20,
        "protein": 1.2,
        "carbs": 3.7,
        "fat": 0.1,
    },
    "focaccia_bianca": {
        "calories": 250,
        "protein": 9,
        "carbs": 46,
        "fat": 3.5,
    },
    "guazzetto_di_calamari": {
        "calories": 150,
        "protein": 15,
        "carbs": 8,
        "fat": 5,
    },
    "insalata_mista": {
        "calories": 15,
        "protein": 1,
        "carbs": 3,
        "fat": 0.2,
    },
    "lasagna_alla_bolognese": {
        "calories": 140,
        "protein": 8,
        "carbs": 15,
        "fat": 6,
    },
    "mandarini": {
        "calories": 53,
        "protein": 0.8,
        "carbs": 13.3,
        "fat": 0.3,
    },
    "medaglioni_di_carne": {
        "calories": 180,
        "protein": 22,
        "carbs": 0,
        "fat": 10,
    },
    "mele": {
        "calories": 52,
        "protein": 0.3,
        "carbs": 14,
        "fat": 0.2,
    },
    "merluzzo_alle_olive": {
        "calories": 115,
        "protein": 17,
        "carbs": 0,
        "fat": 5,
    },
    "minestra": {
        "calories": 50,
        "protein": 2,
        "carbs": 10,
        "fat": 0.5,
    },
    "minestra_lombarda": {
        "calories": 70,
        "protein": 4,
        "carbs": 15,
        "fat": 1,
    },
    "orecchiette_-ragu-": {
        "calories": 180,
        "protein": 9,
        "carbs": 30,
        "fat": 3,
    },
    "passato_alla_piemontese": {
        "calories": 120,
        "protein": 2,
        "carbs": 10,
        "fat": 8,
    },
    "pasta_bianco": {
        "calories": 130,
        "protein": 5,
        "carbs": 25,
        "fat": 1,
    },
    "pasta_cozze_e_vongole": {
        "calories": 180,
        "protein": 8,
        "carbs": 30,
        "fat": 2,
    },
    "pasta_e_ceci": {
        "calories": 120,
        "protein": 5,
        "carbs": 20,
        "fat": 2,
    },
    "pasta_e_fagioli": {
        "calories": 150,
        "protein": 6,
        "carbs": 25,
        "fat": 3,
    },
    "pasta_mare_e_monti": {
        "calories": 160,
        "protein": 10,
        "carbs": 20,
        "fat": 5,
    },
    "pasta_pancetta_e_zucchine": {
        "calories": 200,
        "protein": 8,
        "carbs": 35,
        "fat": 4,
    },
    "pasta_pesto_besciamella_e_cornetti": {
        "calories": 220,
        "protein": 7,
        "carbs": 40,
        "fat": 5,
    },
    "pasta_ricotta_e_salsiccia": {
        "calories": 230,
        "protein": 9,
        "carbs": 35,
        "fat": 6,
    },
    "pasta_sugo": {
        "calories": 160,
        "protein": 8,
        "carbs": 30,
        "fat": 2,
    },
    "pasta_sugo_pesce": {
        "calories": 180,
        "protein": 10,
        "carbs": 25,
        "fat": 5,
    },
    "pasta_sugo_vegetariano": {
        "calories": 150,
        "protein": 5,
        "carbs": 30,
        "fat": 2,
    },
    "pasta_tonno": {
        "calories": 170,
        "protein": 10,
        "carbs": 25,
    },
    "pasta_tonno_e_piselli": {
        "calories": 200,
        "protein": 8,
        "carbs": 30,
        "fat": 4,
    },
    "pasta_zafferano_e_piselli": {
        "calories": 190,
        "protein": 6,
        "carbs": 35,
        "fat": 3,
    },
    "patate-pure": {
        "calories": 83,
        "protein": 1.9,
        "carbs": 19.7,
        "fat": 0.1,
    },
    "patate-pure_prosciutto": {
        "calories": 190,
        "protein": 5,
        "carbs": 12,
        "fat": 12,
    },
    "patatine_fritte": {
        "calories": 312,
        "protein": 3,
        "carbs": 48,
        "fat": 12,
    },
    "pere": {
        "calories": 57,
        "protein": 0.4,
        "carbs": 15,
        "fat": 0.1,
    },
    "pesce_-filetto-": {
        "calories": 100,
        "protein": 22,
        "carbs": 0,
        "fat": 1.5,
    },
    "pesce_2_-filetto-": {
        "calories": 100,
        "protein": 22,
        "carbs": 0,
        "fat": 1.5,
    },
    "piselli": {
        "calories": 81,
        "protein": 5,
        "carbs": 14,
        "fat": 0.4,
    },
    "pizza": {
        "calories": 266,
        "protein": 11,
        "carbs": 31,
        "fat": 10,
    },
    "pizzoccheri": {
        "calories": 335,
        "protein": 11,
        "carbs": 63,
        "fat": 4,
    },
    "polpette_di_carne": {
        "calories": 260,
        "protein": 15,
        "carbs": 9,
        "fat": 19,
    },
    "riso_bianco": {
        "calories": 130,
        "protein": 2.4,
        "carbs": 28.7,
        "fat": 0.3,
    },
    "riso_sugo": {
        "calories": 160,
        "protein": 3,
        "carbs": 27,
        "fat": 4,
    },
    "roastbeef": {
        "calories": 250,
        "protein": 30,
        "carbs": 0,
        "fat": 14,
    },
    "rosbeef": {
        "calories": 250,
        "protein": 30,
        "carbs": 0,
        "fat": 14,
    },
    "rucola": {
        "calories": 25,
        "protein": 2,
        "carbs": 3,
        "fat": 1,
    },
    "scaloppine": {
        "calories": 300,
        "protein": 25,
        "carbs": 5,
        "fat": 18,
    },
    "spinaci": {
        "calories": 23,
        "protein": 2,
        "carbs": 3,
        "fat": 0.4,
    },
    "stinco_di_maiale": {
        "calories": 350,
        "protein": 20,
        "carbs": 10,
        "fat": 25,
    },
    "strudel": {
        "calories": 350,
        "protein": 4,
        "carbs": 40,
        "fat": 20,
    },
    "zucchine_impanate": {
        "calories": 200,
        "protein": 5,
        "carbs": 20,
        "fat": 12,
    },
    "zucchine_umido": {
        "calories": 50,
        "protein": 2,
        "carbs": 5,
        "fat": 1.5,
    },
    "salmone-da_menu_sembra_spada_in_realta-": {
        "calories": 200,
        "protein": 22,
        "carbs": 0,
        "fat": 12,
    },
}


thai_calorie_per_unit = {
    "boiled egg": "40",
    "fried egg": "100",
    "omelet": "250",
}

thai_calorie_per_sq_inch = {
    "khamoo": 2.5,  # Pork leg rice, considering it's a meat dish with rice
    "khaomungai": 2.0,  # Chicken and rice, slightly less due to leaner meat
    "larb": 1.8,  # A salad with minced pork, assuming less due to mixed composition
    "moo daeng": 2.5,  # Red pork, considering the sauce and meat
    "moo kra tiem": 2.7,  # Fried garlic pork, assuming slightly higher due to frying
    "pad cee eew": 1.9,  # Stir-fried noodles, considering oil and ingredients
    "pad thai": 2.0,  # Stir-fried noodle dish, similar reasoning as Pad Cee Eew
    "rad nha": 1.8,  # Noodles with gravy, possibly lighter due to the sauce
    "rice": 1.3,  # Plain rice, considering its basic and staple nature
    "somtam": 0.5,  # Papaya salad, assuming lower due to primarily being vegetables
}

thai_food_translation_simplified = {
    "boiled egg": "ไข่ต้ม",
    "fried egg": "ไข่ดาว",
    "khamoo": "ข้าวขาหมู",
    "khaomungai": "ข้าวมันไก่",
    "larb": "ลาบหมู",
    "moo daeng": "หมูแดง",
    "moo kra tiem": "หมูกะเทียม",
    "omelet": "ไข่เจียว",
    "pad cee eew": "ผัดซีอิ้ว",
    "pad thai": "ผัดไทย",
    "rad nha": "ราดหน้า",
    "rice": "ข้าว",
    "somtam": "ส้มตำ",
}
thai_calorie_per_100_grams = {
    "khamoo": {
        "calories": 150,
        "protein": 20,
        "carbs": 0,
        "fat": 5,
    },  # Pork leg rice, considering it's a meat dish with rice
    "khaomungai": {
        "calories": 164,
        "protein": 22.5,
        "carbs": 0,
        "fat": 4.6,
    },  # Chicken and rice, slightly less due to leaner meat
    "larb": {
        "calories": 65,
        "protein": 11,
        "carbs": 9.4,
        "fat": 2.5,
    },  # A salad with minced pork, assuming less due to mixed composition
    "moo daeng": {
        "calories": 65,
        "protein": 10,
        "carbs": 2.5,
        "fat": 4,
    },  # Red pork, considering the sauce and meat
    "moo kra tiem": {
        "calories": 50,
        "protein": 8,
        "carbs": 0.3,
        "fat": 3,
    },  # Fried garlic pork, assuming slightly higher due to frying
    "pad cee eew": {
        "calories": 200,
        "protein": 13,
        "carbs": 21,
        "fat": 12,
    },  # Stir-fried noodles, considering oil and ingredients
    "pad thai": {
        "calories": 239,
        "protein": 9,
        "carbs": 20,
        "fat": 13,
    },  # Stir-fried noodle dish, similar reasoning as Pad Cee Eew
    "rad nha": {
        "calories": 200,
        "protein": 13.3,
        "carbs": 21,
        "fat": 10,
    },  # Noodles with gravy, possibly lighter due to the sauce
    "rice": {
        "calories": 155,
        "protein": 2.7,
        "carbs": 28,
        "fat": 0.3,
    },  # Plain rice, considering its basic and staple nature
    "somtam": {
        "calories": 60,
        "protein": 0.7,
        "carbs": 15.7,
        "fat": 0.4,
    },  # Papaya salad, assuming lower due to primarily being vegetables
}

thai_nutrient_per_unit = {
    "boiled egg": {
        "protein": 4,
        "carbs": 0.5,
        "fat": 1.6,
    },
    "fried egg": {
        "protein": 6.3,
        "carbs": 0.4,
        "fat": 9.3,
    },
    "omelet": {
        "protein": 8,
        "carbs": 0.5,
        "fat": 10,
    },
}
