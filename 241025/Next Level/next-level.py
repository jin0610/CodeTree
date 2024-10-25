class Nextlevel:
    def __init__(self, userId='codetree', level='10'):
        self.userId = userId
        self.level = level

userId, level = input().split()

object1 = Nextlevel()

object2 = Nextlevel(userId, level)

print(f"user {object1.userId} lv {object1.level}")
print(f"user {object2.userId} lv {object2.level}")