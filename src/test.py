"""test Flask with this"""

from flask import Flask, render_template
app = Flask(__name__)#__name__, para que arranque desde el archivo principal __main__

@app.route('/')#creamos las rutas, con este decorador route("")
def hello():#esto es lo que va dentro del decorador
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":#si el __name__ es donde estamos ejecutando(__main__)
    app.run(debug=True)#ponemos a escuchar nuestra app

