from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    knowledge = {

        # Greetings
        "hello": "Hello! I am your Rural AI Assistant. Ask me about farming, weather, crops, pests, soil, irrigation or government schemes.",
        "hi": "Hi! I can help farmers with agriculture advice and government schemes.",
        "how are you": "I am functioning properly and ready to help with farming knowledge.",

        # Crops
        "rice": "Rice grows best in flooded fields with temperatures between 20°C and 35°C.",
        "paddy": "Paddy cultivation requires plenty of water and fertile soil.",
        "wheat": "Wheat grows best in cool temperatures between 10°C and 25°C.",
        "maize": "Maize grows well in warm climates with moderate rainfall.",
        "crop": "Choosing crops suitable for your soil and climate increases productivity.",

        # Soil
        "soil": "Healthy soil contains organic matter and nutrients required for crop growth.",
        "soil test": "Farmers should test soil pH and nutrient levels before planting crops.",
        "ph": "Most crops grow well in soil pH between 6 and 7.",

        # Fertilizers
        "fertilizer": "NPK fertilizers provide Nitrogen, Phosphorus, and Potassium essential for plant growth.",
        "organic fertilizer": "Organic fertilizers include compost, manure, and green manure.",
        "compost": "Compost improves soil fertility and water retention.",

        # Irrigation
        "irrigation": "Drip irrigation saves water and provides efficient watering to crops.",
        "drip": "Drip irrigation delivers water directly to plant roots.",
        "sprinkler": "Sprinkler irrigation distributes water like rainfall over crops.",

        # Weather
        "weather": "Weather conditions affect crop growth, irrigation, and harvesting.",
        "rain": "Heavy rainfall can damage crops and cause flooding.",
        "temperature": "Most crops grow best between 18°C and 30°C.",
        "monsoon": "Monsoon rains are important for agriculture in India.",

        # Pests
        "pest": "Crop pests can damage plants and reduce yield.",
        "pesticide": "Pesticides should be used carefully and according to recommendations.",
        "neem": "Neem oil is a natural pesticide widely used in agriculture.",

        # Farming practices
        "crop rotation": "Crop rotation improves soil health and reduces pests.",
        "harvest": "Harvest crops when they reach maturity to maximize yield.",
        "planting": "Plant crops at the correct season for best results.",

        # Government schemes
        "scheme": "Many government schemes support farmers financially.",
        "pm kisan": "PM-KISAN provides financial support of ₹6000 per year to farmers.",
        "loan": "Farmers can apply for Kisan Credit Card loans through banks.",
        "insurance": "Pradhan Mantri Fasal Bima Yojana provides crop insurance.",
        "subsidy": "Farmers can receive subsidies for seeds, fertilizers, and irrigation systems.",

        # Technology
        "tractor": "Modern tractors improve farming efficiency.",
        "drone": "Agricultural drones can monitor crops and spray fertilizers.",
        "technology": "Modern farming technology increases productivity."
    }

    for keyword in knowledge:
        if keyword in user_message:
            reply = knowledge[keyword]
            break
    else:
        reply = "I can help with crops, soil, irrigation, weather, pests, farming methods, and government schemes."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)