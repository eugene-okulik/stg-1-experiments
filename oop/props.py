BASE_URL = 'www.google.com'

class Api:
    BASE_URL = f'{BASE_URL}/api'

    def get_users(self):
        requests.get(f'{self.BASE_URL}/users')

    def get_roles(self):
        requests.get(f'{BASE_URL}/api/roles')

class Grpc:
    BASE_URL = f'{BASE_URL}/grpc'