from flask import Flask, render_template, request

# Se define la aplicación de Flask una sola vez
app = Flask(__name__)

# Usuarios registrados para el login
USUARIOS = {
    'juan': 'admin',
    'pepe': 'user'
}

# --- RUTAS DE LA APLICACIÓN ---

# Ruta para la página de inicio (index.html)
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta para el Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nombre = str(request.form['nombre'])
            edad = int(request.form['edad'])
            cantidad = int(request.form['cantidad'])

            precio_base = 9000
            total_sin_descuento = cantidad * precio_base
            descuento = 0

            if 18 <= edad <= 30:
                descuento = total_sin_descuento * 0.15
            elif edad > 30:
                descuento = total_sin_descuento * 0.25

            total_con_descuento = total_sin_descuento - descuento

            return render_template('ejercicio1.html',
                                   nombre=nombre,
                                   edad=edad,
                                   cantidad=cantidad,
                                   resultado=total_con_descuento,
                                   descuento=descuento,
                                   total_sin_descuento=total_sin_descuento)
        except (ValueError, KeyError) as e:
            return "Error en los datos del formulario. Asegúrate de que los campos numéricos sean correctos.", 400
    return render_template('ejercicio1.html')

# Ruta para el login
@app.route('/ejercicio2', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre_usuario = request.form['username']
        contrasena = request.form['password']

        if nombre_usuario in USUARIOS and USUARIOS[nombre_usuario] == contrasena:
            if nombre_usuario == 'juan':
                mensaje = "Bienvenido administrador juan"
            else:
                mensaje = "Bienvenido usuario pepe"
            return render_template('ejercicio2.html', mensaje=mensaje)
        else:
            error = "Credenciales incorrectas. Inténtalo de nuevo."
            return render_template('ejercicio2.html', error=error)
    return render_template('ejercicio2.html')


# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True)