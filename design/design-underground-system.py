class UndergroundSystem:
    def __init__(self):
        self.register = {}
        self.timer = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.register[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.register[id]
        if (start, stationName) not in self.timer:
            self.timer[(start, stationName)] = [0, 0]
        self.timer[(start, stationName)][0] += t - time
        self.timer[(start, stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, people = self.timer[(startStation, endStation)]
        return time/people

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)