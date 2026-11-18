from flask import Flask, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

# Catálogo básico de automóviles
autos = [
    {
        "id": 1,
        "marca": "Toyota",
        "modelo": "Corolla",
        "anio": 2024,
        "precio": 350000,
        "color": "Blanco"
    },
    {
        "id": 2,
        "marca": "Nissan",
        "modelo": "Sentra",
        "anio": 2023,
        "precio": 320000,
        "color": "Gris"
    },
    {
        "id": 3,
        "marca": "Volkswagen",
        "modelo": "Jetta",
        "anio": 2024,
        "precio": 410000,
        "color": "Negro"
    }
]

# Ruta principal del servicio
@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Microservicio de catalogo de automoviles",
        "estado": "Activo"
    })

# Consultar todos los automoviles
@app.route("/autos", methods=["GET"])
def obtener_autos():
    return jsonify(autos)

# Consultar un automovil por su ID
@app.route("/autos/<int:auto_id>", methods=["GET"])
def obtener_auto(auto_id):
    auto = next(
        (auto for auto in autos if auto["id"] == auto_id),
        None
    )

    if auto is None:
        return jsonify({"error": "Automovil no encontrado"}), 404

    return jsonify(auto)

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)