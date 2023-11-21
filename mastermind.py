import random


class Setup:
    def __init__(self, colour_num, position_num, duplicate='no'):
        self.colour = colour_num
        self.position = position_num
        self.__answer = ''
        self.duplicate = duplicate

    def create_answer(self):
        temp = ''
        if self.duplicate == 'yes':
            for i in range(self.position):
                random_num = random.randint(1, self.colour)
                temp += str(random_num)

        elif self.duplicate == 'no':
            while len(temp) != self.position:
                for i in range(self.position):
                    random_num = random.randint(1, self.colour)
                    if str(random_num) not in temp:
                        temp += str(random_num)
            return temp

    @property
    def answer(self):
        return self.__answer


class Mastermind:
    def __init__(self, guess):
        self.guess = guess
        self.__hint = ''

    def gameplay(self, answer):
        n = 0
        while self.guess != answer:
            self.guess = input('Enter your guess: ')
            # elif self.guess == '9999':
            #     print(answer)
            print(f'Your guess is {self.guess}')
            self.__hint = ''
            for num in range(len(self.guess)):
                if self.guess[num] == answer[num]:
                    self.__hint += '*'
            for num in range(len(self.guess)):
                if self.guess[num] in answer and self.guess[num] != answer[num]:
                    self.__hint += 'o'

            print(self.hint)
            print()
            n += 1
        print(f'You solve it after {n} rounds')
        print('================================')

    @property
    def hint(self):
        return self.__hint


choice = ''
Mastermind('')
while choice != 'no':
    color_num = int(input('How many colours: '))
    positions = int(input('How many positions: '))
    dup = input('Allow duplicates? (yes/no): ')

    game_setup = Setup(color_num, positions, dup)
    game_setup.create_answer()
    ans = game_setup.answer

    print(f'Playing Mastermind with {color_num} colours and {positions} positions')
    mastermind_game = Mastermind('')
    mastermind_game.gameplay(ans)
    Mastermind('')
    choice = input('Do you want to continue? ')
