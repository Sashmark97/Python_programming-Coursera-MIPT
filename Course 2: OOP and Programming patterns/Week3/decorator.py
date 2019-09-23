from abc import ABC, abstractmethod
# from deco import *

'''
class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()
'''


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        super().__init__(base)

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Berserk"]

    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["MP"] += 0
        stats["SP"] += 0
        stats["Strength"] += 7
        stats["Perception"] -= 3
        stats["Endurance"] += 7
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        stats["Agility"] += 7
        stats["Luck"] += 7
        return stats.copy()


class Blessing(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]

    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 0
        stats["MP"] += 0
        stats["SP"] += 0
        stats["Strength"] += 2
        stats["Perception"] += 2
        stats["Endurance"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        return stats.copy()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Curse(AbstractNegative):
    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]

    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 0
        stats["MP"] += 0
        stats["SP"] += 0
        stats["Strength"] -= 2
        stats["Perception"] -= 2
        stats["Endurance"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        return stats.copy()


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]

    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 0
        stats["MP"] += 0
        stats["SP"] += 0
        stats["Strength"] -= 0
        stats["Perception"] -= 0
        stats["Endurance"] -= 0
        stats["Charisma"] -= 0
        stats["Intelligence"] -= 0
        stats["Agility"] -= 0
        stats["Luck"] -= 10
        return stats.copy()


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]

    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 0
        stats["MP"] += 0
        stats["SP"] += 0
        stats["Strength"] -= 4
        stats["Perception"] -= 0
        stats["Endurance"] -= 4
        stats["Charisma"] -= 0
        stats["Intelligence"] -= 0
        stats["Agility"] -= 4
        stats["Luck"] -= 0
        return stats.copy()


'''
def get_info(hero):
    print(hero.get_stats())
    print(hero.get_negative_effects())
    print(hero.get_positive_effects())
    print()

if __name__ == "__main__":
    hero = Hero()
    get_info(hero)

    bers1 = Berserk(hero)
    get_info(bers1)

    bers2 = Berserk(bers1)
    get_info(bers2)

    cur1 = Curse(bers2)
    get_info(cur1)

    cur1.base = bers1
    get_info(cur1)
'''
