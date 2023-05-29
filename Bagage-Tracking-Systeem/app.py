from flask import Flask, render_template, request, Response, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS
import secrets


from models.luggage import luggage as luggageModel
from services.luggageLogic import luggageLogic as luggageLogicModel

luggageLogic = luggageLogicModel()
app = Flask(__name__)


# generate secret key for flask because it is needed for socketio
app.config['SECRET_KEY'] = secrets.token_hex(16)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

@app.route('/addLuggage', methods=['POST'])
def addLuggage():
    id = request.form['id']
    owner = request.form['owner']
    weight = request.form['weight']
    CheckInTime = request.form['CheckInTime']
    CheckInDesk = request.form['CheckInDesk']
    destination = request.form['destination']
    location = request.form['CheckInDesk']

    luggage = luggageModel(id, owner, weight, CheckInTime, CheckInDesk, destination, location)

    luggageLogic.addLuggage(luggage)
    
    return Response(status=200)

@app.route('/moveLuggage', methods=['POST'])
def moveLuggage():
    id = request.form['id']
    location = request.form['location']

    luggageLogic.moveLuggage(id, location)

    return Response(status=200)


@socketio.on('getLuggage')
def getLuggage():
    luggage = luggageLogic.getAllLuggage()
    luggageList = []
    for item in luggage:
        luggageList.append(item.__dict__)
    socketio.emit('allLuggage', luggageList, namespace='/')
    
    gates = luggageLogic.getGates()
    gateList = []
    for item in gates:
        gateList.append(item[1])

    socketio.emit('allGates', gateList, namespace='/')




@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=3000)