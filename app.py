from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

T1 = 0
list_of_events = []


@app.route("/")
def home():
    return jsonify({"message": "Bienvenue sur l'API calendrier !"})

# --- 1. Créer un événement ---
@app.route("/create_event", methods=["POST"])
def create_event():
    data = request.get_json()
    t = data.get("time")
    n = data.get("name")

    if t is None or n is None:
        return jsonify({"error": "Paramètres 'time' et 'name' requis"}), 400

    date = (T1, int(t), n)
    list_of_events.append(date)
    return jsonify({"message": "Événement ajouté", "event": date})


# --- 2. Lister tous les événements ---
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify({"events": list_of_events})


# --- 3. Trier les événements ---
@app.route("/events/sorted", methods=["GET"])
def get_sorted_events():
    sorted_events = sorted(list_of_events, key=lambda x: x[1])
    return jsonify({"sorted_events": sorted_events})


# --- 4. Premier événement ---
@app.route("/events/first", methods=["GET"])
def get_first_event():
    if not list_of_events:
        return jsonify({"error": "Aucun événement"}), 404
    return jsonify({"first_event": list_of_events[0]})


# --- 5. Prochain événement ---
@app.route("/events/next", methods=["GET"])
def get_next_event():
    if not list_of_events:
        return jsonify({"error": "Aucun événement"}), 404

    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day, 0, 0, 0)
    seconds_since_midnight = int((now - start_of_day).total_seconds())

    sorted_events = sorted(list_of_events, key=lambda x: x[1])
    for event in sorted_events:
        if int(event[1]) > seconds_since_midnight:
            return jsonify({"next_event": event})
    return jsonify({"message": "Aucun événement à venir aujourd'hui"})


if __name__ == "__main__":
    app.run(debug=True)
