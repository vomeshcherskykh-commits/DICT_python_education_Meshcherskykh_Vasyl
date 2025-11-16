class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = 'main'

    def print_state(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def enough(self, w, m, b):
        if self.water < w: print('Sorry, not enough water!'); return False
        if self.milk < m: print('Sorry, not enough milk!'); return False
        if self.beans < b: print('Sorry, not enough coffee beans!'); return False
        if self.cups < 1: print('Sorry, not enough cups!'); return False
        return True

    def action(self, command):
        if command == 'remaining':
            self.print_state()
        elif command == 'exit':
            exit()
        elif command == 'take':
            print(f'I gave you {self.money}')
            self.money = 0
        elif command == 'fill':
            self.water += int(input('Write how many ml of water do you want to add:\n'))
            self.milk += int(input('Write how many ml of milk do you want to add:\n'))
            self.beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
            self.cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
        elif command == 'buy':
            choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
            if choice == 'back': return
            if choice == '1' and self.enough(250, 0, 16):
                print('I have enough resources, making you a coffee!')
                self.water -= 250; self.beans -= 16; self.cups -= 1; self.money += 4
            elif choice == '2' and self.enough(350, 75, 20):
                print('I have enough resources, making you a coffee!')
                self.water -= 350; self.milk -= 75; self.beans -= 20; self.cups -= 1; self.money += 7
            elif choice == '3' and self.enough(200, 100, 12):
                print('I have enough resources, making you a coffee!')
                self.water -= 200; self.milk -= 100; self.beans -= 12; self.cups -= 1; self.money += 6


machine = CoffeeMachine()
while True:
    command = input('Write action (buy, fill, take, remaining, exit):\n')
    machine.action(command)
