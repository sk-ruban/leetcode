class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins.pop(id)
        key = (startStation, stationName)
        old_total, old_count = self.routes.get(key, (0, 0))
        self.routes[key] = (old_total + t - startTime, old_count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        duration, count = self.routes[(startStation, endStation)]
        return duration / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
