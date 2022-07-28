from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hola')
def hello_world():  # put application's code here
    return 'Hello World ... SantiDev!'


@app.route('/test')
def hello_world_test():
    return 'Hello world test!'


@app.route('/saludar')
@app.route('/saludar/<nombre>')
@app.route('/saludar/<nombre>/<lang>')
def saludar(nombre: str = None, lang: str = None):
    if nombre is None and lang is None:
        return 'Hola'
    elif nombre is not None and lang is None:
        return 'Hola... ' + nombre
    else:
        return 'Hola ' + nombre + ' ' + lang


@app.route('/primer_html')
@app.route('/primer_html/<nombre>')
def primer_html(nombre: str = ''):
    return '''
        <html>
            <body>
                <h1>Hola Flask</h1>
                    <p>Hola %s</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
            </body>
        </html>
    ''' % nombre


@app.route('/static_file')
def static_file():
    return "<img src='" + url_for("static", filename="img/flask.png") + "'>"
    # return "<img src='/static/img/flask.png'>"


@app.route('/mi_primer_template')
@app.route('/mi_primer_template/<name>')
def mi_primer_template(name: str = ''):
    return render_template('view.html', vname=name)


if __name__ == '__main__':
    app.run(debug=True)
