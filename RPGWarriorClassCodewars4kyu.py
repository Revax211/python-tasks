class Warrior():
    levels = {num: num // 100 for num in range(100, 10001)}

    def __init__(self):
        self.level = 1
        self.rank = "Pushover"
        self.__experience = 100
        self.__achievements = []

    @property
    def achievements(self):
        return self.__achievements

    def add_experience(self, points):
        def limits():
            if self.__experience < 100:
                self.__experience = 100
            elif self.__experience > 10000:
                self.__experience = 10000
        limits()
        self.__experience += points
        if self.__experience in self.levels:
            self.level = self.levels[self.__experience]
        elif self.__experience > max(self.levels):
            self.level = self.levels[max(self.levels)]
        self.rank = self.get_rank(self.level)[1]
        limits()

    @property
    def experience(self):
        return self.__experience

    def training(self, training_list):
        achtext, expgain, minlvl = training_list
        if expgain < 0:
            expgain = 0
        if self.level >= minlvl:
            self.add_experience(expgain)
            self.achievements.append(achtext)
            return achtext
        else:
            return "Not strong enough"

    def battle(self, enemy_level):
        if not isinstance(enemy_level, int) or enemy_level < 1 or \
                enemy_level > 100:
            return "Invalid level"
        superior = (Warrior.get_rank(enemy_level)[0]) - (
            Warrior.get_rank(self.level)[0])
        diff = enemy_level - self.level
        if diff >= 5 and superior > 0:
            return "You've been defeated"
        if enemy_level < 1 or enemy_level > 100:
            return "Invalid level"
        if diff < -1:
            self.add_experience(0)
            return "Easy fight"
        elif diff == -1:
            self.add_experience(5)
            return "A good fight"
        elif diff == 0:
            self.add_experience(10)
            return "A good fight"
        elif diff == 1:
            self.add_experience(20 * diff * diff)
            return "An intense fight"
        elif diff > 1:
            self.add_experience(20 * diff * diff)
            return "An intense fight"

    @ staticmethod
    def get_rank(lvl):
        ranks = {
            range(1, 10): (1, "Pushover"),
            range(10, 20): (2, "Novice"),
            range(20, 30): (3, "Fighter"),
            range(30, 40): (4, "Warrior"),
            range(40, 50): (5, "Veteran"),
            range(50, 60): (6, "Sage"),
            range(60, 70): (7, "Elite"),
            range(70, 80): (8, "Conqueror"),
            range(80, 90): (9, "Champion"),
            range(90, 100): (10, "Master"),
            range(100, 101): (11, "Greatest")  # исправлено
        }
        for key in ranks:
            if lvl in key:
                return ranks[key]