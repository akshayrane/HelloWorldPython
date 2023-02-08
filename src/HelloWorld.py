class HelloWorld:
    def __init__(self, name='World'):
        self.name = name
        self.message = f'Hello {name}!'

    def __str__(self):
        return self.message
