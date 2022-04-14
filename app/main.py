from distutils.log import debug
from flask import Flask, render_template, request

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

def query_string():
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "ok"

def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    
@app.route('/base')
def base():
    return render_template('base.html')


if __name__=='__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000, host= "0.0.0.0")