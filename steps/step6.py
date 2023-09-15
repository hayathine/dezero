class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None

class Function:
    def __call__(self, input):
        x = input.data
        y = self.foward(x)
        output = Variable(y)
        self.input
