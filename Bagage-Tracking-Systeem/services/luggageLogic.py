import asyncio
from flask_socketio import emit as wsEmit

from services.luggageDB import luggageDB as _luggageDB
from models.luggage import luggage as luggageModel
import os
from dotenv import load_dotenv

load_dotenv()

class luggageLogic:
    def __init__(self) -> None:
        self.luggageDB = _luggageDB(
            os.getenv('DB_USERNAME'),
            os.getenv('DB_PASSWORD'),
            os.getenv('DB_HOST')
        )

    def getAllLuggage(self):
        return self.luggageDB.getAllLuggage()
    
    def getGates(self):
        return self.luggageDB.getGates()


    def addLuggage(self, luggage: luggageModel):
        self.luggageDB.addLuggage(luggage)
        wsEmit('luggageAdded', luggage.__dict__, broadcast=True, namespace='/')

    def moveLuggage(self, id: str, location: str):
        self.luggageDB.moveLuggage(id, location)
        wsEmit('luggageMoved', {'id': id, 'location': location}, broadcast=True, namespace='/')

    def removeLuggage(self, id: str):
        self.luggageDB.removeLuggage(id)
        wsEmit('luggageRemoved', id, broadcast=True, namespace='/')
    
    