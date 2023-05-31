from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para obtener datos de usuario por ID
@app.route("/get-user/<user_id>")
def get_user(user_id):
    # Datos de usuario ficticios
    user_data = {
        "user_id": user_id,
        "name" : "John Doe",
        "email" : "John.deo@example.com"
    }

    # Obtener el parámetro 'extra' de la consulta (si existe)
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    # Devolver los datos de usuario en formato JSON
    return jsonify(user_data), 200

# Ruta para crear un nuevo usuario
@app.route("/create-user", methods=['POST'])
def create_user():
    # Obtener los datos del usuario desde el cuerpo de la solicitud en formato JSON
    data = request.get_json()

    # Devolver los datos del usuario creado en formato JSON
    return jsonify(data), 201

# Iniciar la aplicación Flask en modo de depuración
if __name__ == "__main__":
    app.run(debug=True)
