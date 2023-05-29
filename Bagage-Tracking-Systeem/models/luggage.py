class luggage:
    def __init__(self, id, owner, weight, CheckInTime, checkInLocation, destination, location="UNKNOWN", lastMoved=None) -> None:
        self.id = id
        self.owner = owner
        self.weight = weight
        self.CheckInTime = CheckInTime
        self.checkInLocation = checkInLocation
        self.destination = destination
        self.location = location
        self.lastMoved = lastMoved
        
    def __str__(self) -> str:
        return f"[{self.id}] {self.owner} {self.weight}kg {self.location}"
