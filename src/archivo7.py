class Bot:
    def __init__(self, name):
        self.name = name
        self.commands = {}

    def register_command(self, command_name, handler):
        self.commands[command_name] = handler

    def handle_message(self, message):
        command = self.extract_command(message)
        if command in self.commands:
            return self.commands[command]()
        return "Command not found."

    def extract_command(self, message):
        return message.strip().lower().split()[0]

# Example (simulated command)
def help_command():
    return "This is a placeholder help message."

# Instantiate bot (simulated)
my_bot = Bot("SystemiaBot")
my_bot.register_command("help", help_command)

# Internal economy system - placeholder only
# Simulates user balances and transaction logic

class EconomySystem:
    def __init__(self):
        self.balances = {}

    def create_user(self, user_id):
        if user_id not in self.balances:
            self.balances[user_id] = 100  # starting balance

    def transaction(self, sender, receiver, amount):
        if self.balances.get(sender, 0) >= amount:
            self.balances[sender] -= amount
            self.balances[receiver] = self.balances.get(receiver, 0) + amount
            return True
        return False

    def get_balance(self, user_id):
        return self.balances.get(user_id, 0)