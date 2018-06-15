
class User():
    def __init__(self, username):
        self._username = username

    def User(username):
        this = username

    @property
    def username(self):
        return self._username

if __name__ == "__main__":
    u = User('Guido')
    print(u.username)

    value = 50
    if value > 75:
        print("blue")
    elif value > 50:
        print("purple")
    elif value > 25:
        print("orange")
    else:
        print("green")
    
