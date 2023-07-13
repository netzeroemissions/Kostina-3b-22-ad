class Bank:
    def __init__(self):
        self.clients = []
        self.accounts_id = [0]
        self.client_account = {}
        self.transactions = []
        self.balances = {}

    def client_create(self, name):
        self.clients.append(name)

    def account_create(self, name, balance):
        self.balance = 0
        self.client_account[name] = self.accounts_id[len(self.accounts_id) - 1] + 1
        self.accounts_id.append(self.accounts_id[len(self.accounts_id) - 1] + 1)
        self.balances[self.client_account[name]] = balance

    def transaction(self, sender, receiver, amount):
        sender_account = self.client_account[sender]
        receiver_account = self.client_account[receiver]
        if self.balances[sender_account] >= amount:
            self.balances[sender_account] -= amount
            self.balances[receiver_account] += amount
            self.transactions.append((sender_account, receiver_account, amount))
        else:
            print('На счету отправителя недостаточно средств')

bank = Bank()
bank.client_create('Иванов')
bank.account_create('Иванов', 2000)

bank.client_create('Сидоров')
bank.account_create('Сидоров', 3000)

bank.transaction('Иванов', 'Сидоров', 1000)
print('Клиенты', bank.clients)
print('Счета клиентов', bank.client_account)
print('Номера счетов', bank.accounts_id)
print('Транзакции', bank.transactions)
print('Балансы', bank.balances)