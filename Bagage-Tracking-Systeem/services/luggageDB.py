import mysql.connector

from models.luggage import luggage as luggageModel

class luggageDB:
    def __init__(self, user, password, host) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.database = 'bagage_tracking_systeem'

    def addLuggage(self, luggage: luggageModel):
        with mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database) as conn:
            cursor = conn.cursor()

            query = "INSERT INTO luggage (id, owner, weight, check_in_time, check_in_location, destination_gate, location, last_moved) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

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
        with mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database) as conn:
            cursor = conn.cursor()

            query = "UPDATE luggage SET location = %s, last_moved = NOW() WHERE id = %s"

            cursor.execute(query, (location, id))

            conn.commit()
        
    def getLuggage(self, id: str):
        with mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database) as conn:
            cursor = conn.cursor()

            query = "SELECT * FROM luggage WHERE id = %s"

            cursor.execute(query, (id,))
            luggage = cursor.fetchone()

            print(luggage)

            # convert to luggage object
            luggage = luggageModel(luggage[0], luggage[1], luggage[2], luggage[3], luggage[4], luggage[5], luggage[6], luggage[7])

            return luggage
        
    def getAllLuggage(self):
        with mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database) as conn:
            cursor = conn.cursor()

            query = "SELECT * FROM luggage"

            cursor.execute(query)
            luggage = cursor.fetchall()
            
            # convert to luggage object
            luggageList = []
            for l in luggage:
                luggageList.append(luggageModel(l[0], l[1], l[2], l[3].strftime("%Y-%m-%d %H:%M:%S"), l[4], l[5], l[6], l[7]))

            return luggageList
        
    def removeLuggage(self, id: str):
        with mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database) as conn:
            cursor = conn.cursor()

            query = "DELETE FROM luggage WHERE id = %s"

            cursor.execute(query, (id,))

            conn.commit()
        
    def getLuggageByLocation(self, location: str):
        with mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database) as conn:
            cursor = conn.cursor()
            
            query = "SELECT * FROM luggage  WHERE location = %s ORDER BY last_moved DESC"

            cursor.execute(query, (location,))
            luggage = cursor.fetchall()
            
            # convert to luggage object
            luggageList = []
            for l in luggage:
                luggageList.append(luggageModel(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]))
                
            return luggageList
        

    def getGates(self):
        with mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database) as conn:
            cursor = conn.cursor()

            query = "SELECT * FROM gates"

            cursor.execute(query)
            gates = cursor.fetchall()

            return gates