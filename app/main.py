from distutils.log import debug
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')

def index():
    datos=['33 Años', 'Masculino', 'Avda Cabo Gata 121 1 3', 'ing.cefa@gmail.com']
    cliente = {
        'Titulo':'Index',
        'Bienvenida':'Saludos',
        'Nombre':'Carlos Efren Fernandez Abad',
        'Datos':datos,
        'numDatos':len(datos)

    }
    return render_template('index.html', data=cliente)

@app.route('/producto/<sku>/<int:modelo>')
def producto(sku, modelo):
    producto={
        'sku':sku,
        'nombre':'SmartPhone',
        'marca':'Azus',
        'modelo':modelo
    }
    return render_template('producto.html', data=producto)


if __name__=='__main__':
    app.run(debug=True, port=5000, host= "0.0.0.0")