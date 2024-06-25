from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/repaso'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app = Flask(__name__)

productos = [
    {"nombre": "Producto 1", "categoria": "Categoría A", "precio": 10.0},
    {"nombre": "Producto 2", "categoria": "Categoría B", "precio": 20.0},
    {"nombre": "Producto 3", "categoria": "Categoría A", "precio": 15.0},
    {"nombre": "Producto 4", "categoria": "Categoría C", "precio": 30.0}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/productos')
def mostrar_productos():
    return render_template('productos.html', productos=productos)

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        # aca obtiene los datos ddel formulario
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = float(request.form['precio'])
        # creo el nuevo producto
        nuevo_producto = {"nombre": nombre, "categoria": categoria, "precio": precio}
        # y aca lo agrego
        productos.append(nuevo_producto)

        return redirect(url_for('mostrar_productos'))   
    
    return render_template('agregar_producto.html') 

if __name__ == '__main__':
    app.run(debug=True)
