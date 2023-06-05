import sqlite3

from models.luggage import luggage as luggageModel

class luggageDB:
    def __init__(self) -> None:
        pass

    def addLuggage(self, luggage: luggageModel):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()

            query = "INSERT INTO luggage (id, owner, weight, check_in_time, check_in_location, destination_gate, location, last_moved) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

            cursor.execute(query, 
                           (luggage.id,
                            luggage.owner, 
                            luggage.weight,
                            luggage.CheckInTime,
                            luggage.checkInLocation,
                            luggage.destination,
                            luggage.location,
                            luggage.lastMoved))
            
            conn.commit()

    def moveLuggage(self, id: str, location: str):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()

            query = "UPDATE luggage SET location = ?, last_moved = datetime('now') WHERE id = ?"

            cursor.execute(query, (location, id))

            conn.commit()
        
    def getLuggage(self, id: str):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()

            query = "SELECT * FROM luggage WHERE id = ?"

            cursor.execute(query, (id,))
            luggage = cursor.fetchone()

            # convert to luggage object
            luggage = luggageModel(luggage[0], luggage[1], luggage[2], luggage[3], luggage[4], luggage[5], luggage[6], luggage[7])

            return luggage
        
    def getAllLuggage(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()

            query = "SELECT * FROM luggage"

            cursor.execute(query)
            luggage = cursor.fetchall()
            
            # convert to luggage object
            luggageList = []
            for l in luggage:
                luggageList.append(luggageModel(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]))

            return luggageList
        
    def removeLuggage(self, id: str):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()

            query = "DELETE FROM luggage WHERE id = ?"

            cursor.execute(query, (id,))

            conn.commit()
        
    def getLuggageByLocation(self, location: str):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            
            query = "SELECT * FROM luggage  WHERE location = ? ORDER BY last_moved DESC"

            cursor.execute(query, (location,))
            luggage = cursor.fetchall()
            
            # convert to luggage object
            luggageList = []
            for l in luggage:
                luggageList.append(luggageModel(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]))

            return luggageList
        

    def getGates(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()

            query = "SELECT * FROM gates"

            cursor.execute(query)
            gates = cursor.fetchall()

            return gates
