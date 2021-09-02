import json

class User:
    def __init__(self, user):
        self.name = user.get('name')
        self.owes = user.get('owes')
        self.owed_by = user.get('owed_by')
        self.balance = user.get('balance')

    def get_as_dict(self):
        user = {'name' : self.name, 
                'owes' : self.owes,
                'owed_by' : self.owed_by,
                'balance' : self.balance,}
        return user

    def lend(self, name, amount):
        if name in self.owes:
            self.owes[name] -= amount
            if self.owes.get(name) < 0:
                self.owed_by[name] = -self.owes.get(name)
                self.owes.pop(name)
            elif self.owes.get(name) == 0:
                self.owes.pop(name)
        else:
            self.owed_by[name] = self.owed_by.setdefault(name, 0.0) + amount
        self.balance += amount

    def borrow(self, name, amount):
        if name in self.owed_by:
            self.owed_by[name] -= amount
            if self.owed_by.get(name) < 0:
                self.owes[name] = -self.owed_by.get(name)
                self.owed_by.pop(name)
            elif self.owed_by.get(name) == 0:
                self.owed_by.pop(name)
        else:
            self.owes[name] = self.owes.setdefault(name, 0.0) + amount
        self.balance -= amount

    def __lt__(self, other):
        return self.name < other.name

class RestAPI:
    def __init__(self, database={}):
        users = [User(user) for user in database.get('users')]
        self.database = {'users' : users}
        self.database['users'].sort()

    def get_users(self, payload=None):
        response = {'users' : [user.get_as_dict() for user in self.database.get('users')]}
        if payload:
            payload = json.loads(payload).get('users')
            response = {'users' : [user for user in response.get('users') if user.get('name') in payload]}
        return json.dumps(response)

    def add_user(self, payload):
        user = {'name' : json.loads(payload).get('user'), 
                'owes' : {},
                'owed_by' : {},
                'balance' : 0.0,}

        self.database.setdefault('users', []).append(User(user))
        self.database['users'].sort()

        return json.dumps(user)

    def make_deal(self, payload):
        payload = json.loads(payload)
        lender, borrower, amount = payload.get('lender'), payload.get('borrower'), payload.get('amount')

        lender_index, borrower_index = 0, 0
        for i, user in enumerate(self.database.get('users')):
            if user.name == lender:
                lender_index = i
            elif user.name == borrower:
                borrower_index = i

        self.database['users'][lender_index].lend(borrower, amount)
        self.database['users'][borrower_index].borrow(lender, amount)

        return self.get_users(payload=json.dumps({'users' : [lender, borrower]}))


    def get(self, url, payload=None):
        if url == '/users':
            return self.get_users(payload)
                
    def post(self, url, payload=None):
        if url == '/add':
            return self.add_user(payload)
        elif url == '/iou':
            return self.make_deal(payload)
