class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0

        for i in bills:
            match i:
                case 5:
                    fives += 1
                case 10:
                    if fives > 0:
                        tens += 1
                        fives -= 1
                    else:
                        return False
                case 20:
                    if fives > 0 and tens > 0:
                        tens -= 1
                        fives -= 1
                    elif fives > 2:
                        fives -= 3
                    else:
                        return False

        return True