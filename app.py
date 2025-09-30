import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Lista de los nombres de host de los nodos que definimos en docker-compose.yml
NODOS = ["nodo_1", "nodo_2", "nodo_3"]

Status = [False, False, False]
# Ruta principal que muestra la interfaz gráfica
@app.route('/')
def index():
    return render_template('index.html', nodos=NODOS)

# Ruta de API que devuelve el estado de los nodos en formato JSON
@app.route('/status')
def get_status():
    status_nodos = {}
    for inx, nodo in enumerate(NODOS):
        if Status[inx] == True:
            status_nodos[nodo] = "online"
        else:
            status_nodos[nodo] = "offline"
            
    return jsonify(status_nodos)

@app.route('/activate')
def get_activate():
    arg = request.args.get('node')
    status_resp = {'status': False}
    for inx, nodo in enumerate(NODOS):
        if arg == nodo:
            Status[inx] = True
            status_resp['status'] = True
            break
    return jsonify(status_resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)