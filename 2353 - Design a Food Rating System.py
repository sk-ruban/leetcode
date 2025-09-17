from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = defaultdict(SortedSet)
        self.cuisines = {}
        self.ratings = {}

        for i in range(len(foods)):
            self.foods[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisines[food]
        r = self.ratings[food]

        self.foods[c].remove((-r, food))
        self.foods[c].add((-newRating, food))

        self.ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.foods[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)