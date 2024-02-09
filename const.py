calorie_per_unit = {
    "arancia": 45,
    "torta_ananas": 130,
    "torta_cioccolato_e_pere": 130,
    "torta_crema": 130,
    "torta_crema_2": 130,
    "torta_salata_-alla_valdostana-": 130,
    "torta_salata_3": 130,  # Assuming similar to above
    "torta_salata_rustica_-zucchine-": 125,
    "torta_salata_spinaci_e_ricotta": 120,
    "banane": 110,
    "pane": 130,
    "yogurt": 102,
    "budino": 60,
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


calories_per_sq_inch = {
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
