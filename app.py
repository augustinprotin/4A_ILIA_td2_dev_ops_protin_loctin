from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple de route simple
@app.route("/")
def home():
    return "<p>TG baptise!</p>"

# Exemple de route qui utilise une fonction
@app.route("/add")
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = a + b
    return jsonify({"result": result})



if __name__ == "__main__":
    app.run(debug=True)