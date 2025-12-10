from . import MhwGameOptions
from .xorshift128 import XorShift128Generator


# This follows the implementation of the MHW Randomizer
low_rank_monsters = [0, 1, 7, 9, 12, 14, 21, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35]
into_bowels_vale_monsters  = [0, 1, 7, 9, 12, 14, 21, 24, 27, 28, 30, 31, 32, 33, 34]
# "Best quest ever" has fewer monsters available
best_monsters_ever = [0, 1, 7, 12, 14, 21, 24, 27, 28, 29, 30, 31, 32, 34, 35]

class MonsterRandomizer:
    monster_chances = {}
    monsters_to_add_chances = set()

    def __init__(self, randomizer: XorShift128Generator):
        self.randomizer = randomizer

    def get_random_monster(self, possible_monsters: list[int]):
        total_weight = sum(self.monster_chances[monsterId] for monsterId in possible_monsters)
        selected_chance = self.randomizer.next(total_weight) + 1

        added_chance = 0
        for monster_id in possible_monsters:
            added_chance += self.monster_chances[monster_id]
            if added_chance >= selected_chance:
                return monster_id
        return -1

    def increment_monster_chances(self):
        ids_to_remove = []
        for monster_id in self.monsters_to_add_chances:
            self.monster_chances[monster_id] += 1
            if self.monster_chances[monster_id] >= 10:
                ids_to_remove.append(monster_id)

        for monster_id in ids_to_remove:
            self.monsters_to_add_chances.remove(monster_id)

    def set_main_quest_monster(self, monster_id: int):
        self.monster_chances[monster_id] = 0
        self.monsters_to_add_chances.add(monster_id)

    def set_other_quest_monster(self, monster_id: int):
        self.monster_chances[monster_id] -= 5
        if self.monster_chances[monster_id] < 0:
            self.monster_chances[monster_id] = 0
        self.monsters_to_add_chances.add(monster_id)

    def handle_quest(self, possible_monsters: list[int], additional_monster_count: int) -> int:
        main_monster = self.get_random_monster(possible_monsters)

        additional_monsters = set()
        for _ in range(additional_monster_count):
            additional_monster = self.get_random_monster(possible_monsters)
            while additional_monster == main_monster or additional_monster in additional_monsters:
                additional_monster = self.get_random_monster(possible_monsters)
            additional_monsters.add(additional_monster)

        self.increment_monster_chances()
        self.set_main_quest_monster(main_monster)
        for additional_monster in additional_monsters:
            self.set_other_quest_monster(additional_monster)
        return main_monster

    def get_random_monsters_by_quest(self) -> dict[int, int]:
        self.monsters_to_add_chances.clear()
        for i in range(102):
            self.monster_chances[i] = 10

        monster_by_quest = {}
        monster_by_quest[102] = self.handle_quest(low_rank_monsters, 0)

        # 103 is always linked to 102 monster - we use up a double from the randomizer, but we don't change any chances (because the 1st monster would be reset down to 0 anyway)
        self.randomizer.next_double()
        monster_by_quest[103] = monster_by_quest[102]

        monster_by_quest[201] = self.handle_quest(low_rank_monsters, 1)
        monster_by_quest[205] = self.handle_quest(low_rank_monsters, 3)

        # Best kind of quest - handle extra monsters separately
        monster_by_quest[301] = self.get_random_monster(best_monsters_ever)
        # 2nd monster is always a Rathian - we still need to call the randomizer
        self.randomizer.next_double()
        # 3rd monster is random again
        random_third_monster = self.get_random_monster(best_monsters_ever)
        self.increment_monster_chances()
        self.set_main_quest_monster(monster_by_quest[301])
        self.set_other_quest_monster(random_third_monster)
        self.set_other_quest_monster(9)

        monster_by_quest[302] = self.handle_quest(low_rank_monsters, 2)
        monster_by_quest[305] = self.handle_quest(low_rank_monsters, 2)
        monster_by_quest[306] = self.handle_quest(low_rank_monsters, 2)

        # Zorah 1
        monster_by_quest[401] = self.handle_quest(low_rank_monsters, 1)
        monster_by_quest[405] = self.handle_quest(low_rank_monsters, 2)
        monster_by_quest[407] = self.handle_quest(low_rank_monsters, 1)
        monster_by_quest[408] = self.handle_quest(low_rank_monsters, 2)

        monster_by_quest[501] = self.handle_quest(into_bowels_vale_monsters, 2)
        monster_by_quest[502] = self.handle_quest(low_rank_monsters, 2)
        monster_by_quest[503] = self.handle_quest(low_rank_monsters, 2)

        # Zorah 2
        monster_by_quest[504] = self.handle_quest(low_rank_monsters, 1)

        return monster_by_quest
