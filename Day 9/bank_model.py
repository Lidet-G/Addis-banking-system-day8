from collections import deque

# Account Class

class Account:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

# Branch Tree

class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.accounts = []

    def add_child(self, branch):
        self.children.append(branch)

    def add_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        total = 0

        for account in self.accounts:
            total += account.balance

        for child in self.children:
            total += child.total_balance()

        return total



# Build Branch Tree


head_office = Branch("Head Office")

bole = Branch("Bole")
piassa = Branch("Piassa")

head_office.add_child(bole)
head_office.add_child(piassa)

# Child branches

bole_teller = Branch("Bole Teller")
bole_loans = Branch("Bole Loans")

piassa_teller = Branch("Piassa Teller")

bole.add_child(bole_teller)
bole.add_child(bole_loans)
piassa.add_child(piassa_teller)

# Add Accounts


bole.add_account(Account("CBE-1", "Abel", 5000))
bole.add_account(Account("CBE-2", "Sara", 3000))

bole_teller.add_account(Account("CBE-3", "John", 4500))

bole_loans.add_account(Account("CBE-4", "Mahi", 6000))

piassa.add_account(Account("CBE-5", "Almaz", 7000))

piassa_teller.add_account(Account("CBE-6", "Dawit", 2500))


# Total Balance


print("========== BANK ==========")
print("Total Bank Balance:", head_office.total_balance())


# Transfer Graph


transfers = {
    "CBE-1": ["CBE-2", "CBE-3"],
    "CBE-2": ["CBE-4"],
    "CBE-3": ["CBE-4"],
    "CBE-4": ["CBE-5"],
    "CBE-5": ["CBE-6"],
    "CBE-6": []
}


# BFS


def bfs(graph, start):

    visited = set()

    queue = deque([start])

    visited.add(start)

    while queue:

        node = queue.popleft()

        print(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)

    return visited


print("\nAccounts reachable from CBE-1")
reachable = bfs(transfers, "CBE-1")

print("\nReachable Set:")
print(reachable)