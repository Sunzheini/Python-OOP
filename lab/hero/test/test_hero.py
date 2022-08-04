from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    # class Hero:
    # username: str
    # health: float
    # damage: float
    # level: int

    ATTACKER_USERNAME = 'Hero'
    ATTACKER_LEVEL = 10
    ATTACKER_HEALTH = 100
    ATTACKER_DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self):
        self.attacker = Hero(self.ATTACKER_USERNAME, self.ATTACKER_LEVEL,
                             self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

    # def __init__(self, username: str, level: int, health: float, damage: float):
    # self.username = username
    # self.level = level
    # self.health = health
    # self.damage = damage

    def test_init_sets_up_correct_parameters(self):
        self.assertEqual(self.ATTACKER_USERNAME, self.attacker.username)
        self.assertEqual(self.ATTACKER_LEVEL, self.attacker.level)
        self.assertEqual(self.ATTACKER_HEALTH, self.attacker.health)
        self.assertEqual(self.ATTACKER_DAMAGE, self.attacker.damage)

    # ------------------------------------------------------------------

    # def battle(self, enemy_hero):
    # if enemy_hero.username == self.username:
    # raise Exception("You cannot fight yourself")

    def test_battle_equal_names_raise_exception(self):
        enemy_hero = Hero(self.ATTACKER_USERNAME, 5, 20, 30)

        with self.assertRaises(Exception) as ex:
            self.attacker.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    # ------------------------------------------------------------------

    # if self.health <= 0:
    # raise ValueError("Your health is lower than or equal to 0. You need to rest")

    def test_battle_if_self_health_less_zero_raise_exception(self):
        enemy_hero = Hero('Daniel', 5, 20, 30)
        self.attacker.health = 0

        with self.assertRaises(ValueError) as ex:
            self.attacker.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. "
                         "You need to rest", str(ex.exception))

    # ------------------------------------------------------------------

    # if enemy_hero.health <= 0:
    # raise ValueError(f"You cannot fight {enemy_hero.username}. He needs to rest")

    def test_battle_if_enemy_health_less_zero_raise_exception(self):
        enemy_hero = Hero('Daniel', 5, 0, 30)

        with self.assertRaises(ValueError) as ex:
            self.attacker.battle(enemy_hero)

        compare_string = f"You cannot fight {enemy_hero.username}. " \
                         f"He needs to rest"
        self.assertEqual(compare_string, str(ex.exception))

    # ------------------------------------------------------------------

    # player_damage = self.damage * self.level
    # enemy_hero_damage = enemy_hero.damage * enemy_hero.level

    # self.health -= enemy_hero_damage
    # enemy_hero.health -= player_damage

    # ------------------------------------------------------------------

    # if self.health <= 0 and enemy_hero.health <= 0:
    # return "Draw"

    def test_battle_both_heroes_dead(self):
        enemy_hero = Hero('Daniel', self.ATTACKER_LEVEL,
                          self.ATTACKER_HEALTH,
                          self.ATTACKER_DAMAGE)
        result = self.attacker.battle(enemy_hero)
        self.assertEqual("Draw", result)

        expected_health = self.ATTACKER_HEALTH - \
                          (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE)
        self.assertEqual(expected_health, self.attacker.health)
        self.assertEqual(expected_health, enemy_hero.health)

# ------------------------------------------------------------------

    # if enemy_hero.health <= 0:
        # self.level += 1
        # self.health += 5
        # self.damage += 5
        # return "You win"

    def test_battle_assert_enemy_dead_then_level_up(self):
        enemy_level, enemy_health, enemy_damage = 5, 100, 10
        enemy_hero = Hero('Daniel', enemy_level, enemy_health, enemy_damage)

        result = self.attacker.battle(enemy_hero)
        enemy_expected_health = enemy_health - \
                                (self.ATTACKER_LEVEL *
                                 self.ATTACKER_DAMAGE)

        attacker_expected_health = self.ATTACKER_HEALTH - (enemy_level * enemy_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You win", result)
        self.assertEqual(enemy_expected_health, enemy_hero.health)
        self.assertEqual(self.ATTACKER_LEVEL +
                         self.BATTLE_LEVEL_INCREMENT,
                         self.attacker.level)
        self.assertEqual(self.ATTACKER_DAMAGE +
                         self.BATTLE_DAMAGE_INCREMENT,
                         self.attacker.damage)

        self.assertEqual(attacker_expected_health, self.attacker.health)

# ------------------------------------------------------------------

    # enemy_hero.level += 1
    # enemy_hero.health += 5
    # enemy_hero.damage += 5
    # return "You lose"

    def test_battle_assert_hero_dead_then_level_up(self):
        attacker_level, attacker_health, attacker_damage = 5, 100, 10
        attacker = Hero('Attacker', attacker_level, attacker_health, attacker_damage)

        enemy_hero = Hero("Enemy", self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

        result = attacker.battle(enemy_hero)
        attacker_expected_health = attacker_health - \
                                (self.ATTACKER_LEVEL *
                                 self.ATTACKER_DAMAGE)

        enemy_expected_health = self.ATTACKER_HEALTH - (attacker_level * attacker_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You lose", result)
        self.assertEqual(attacker_expected_health, attacker.health)

        self.assertEqual(self.ATTACKER_LEVEL +
                         self.BATTLE_LEVEL_INCREMENT,
                         enemy_hero.level)
        self.assertEqual(self.ATTACKER_DAMAGE +
                         self.BATTLE_DAMAGE_INCREMENT,
                         enemy_hero.damage)
        self.assertEqual(enemy_expected_health,
                         enemy_hero.health)

# ------------------------------------------------------------------

    # def __str__(self):
        # return f"Hero {self.username}: {self.level} lvl\n" \
            # f"Health: {self.health}\n" \
            # f"Damage: {self.damage}\n"

    def test_return_correct_string(self):
        result = f"Hero {self.attacker.username}: " \
                 f"{self.attacker.level} lvl\n" \
            f"Health: {self.attacker.health}\n" \
            f"Damage: {self.attacker.damage}\n"

        self.assertEqual(result, str(self.attacker))


if __name__ == '__main__':
    main()
