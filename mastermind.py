import random


class Setup:
    def __init__(self, colour_num, position_num, duplicate='no'):
        self.colour = colour_num
        self.position = position_num
        self.answer = ''
        self.duplicate = duplicate

    def create_answer(self):
        if self.duplicate == 'yes':
            for i in range(self.position):
                random_num = random.randint(1, self.colour)
                self.answer += str(random_num)

        elif self.duplicate == 'no':
            temp = ''
            while len(temp) != self.position:
                for i in range(self.position):
                    random_num = random.randint(1, self.colour)
                    if str(random_num) not in temp:
                        temp += str(random_num)
            self.answer = temp
            return self.answer


class Mastermind:
    def __init__(self, guess):
        self.guess = guess
        self.hint = ''

    def gameplay(self):
        n = 0
        while self.guess != answer:
            self.guess = input('Enter your guess: ')
            print(f'Your guess is {self.guess}')
            self.hint = ''
            for num in range(len(self.guess)):
                if self.guess[num] == answer[num]:
                    self.hint += '*'
                elif self.guess[num] in answer:
                    self.hint += 'o'
            print(self.hint)
            print()
            n += 1
        print(f'You solve it after {n} rounds')
        print('================================')


choice = ''
while choice != 'no':
    color_num = int(input('How many colours: '))
    position_num = int(input('How many positions: '))
    duplicate = input('Allow duplicates? (yes/no): ')

    game_setup = Setup(color_num, position_num, duplicate)
    game_setup.create_answer()
    answer = game_setup.answer

    print(f'Playing Mastermind with {color_num} colours and {position_num} positions')
    print(answer)
    mastermind_game = Mastermind('')
    mastermind_game.gameplay()
    Mastermind('')
    choice = input('Do you want to continue? ')










