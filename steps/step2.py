class Function:
    def __call__(self, input):
        x = input.data
        y = self.foward(x)
        output = Vareable(y)
        return output

    def foward(self, x):
        raise NotImplomenttedError()

    def Square(Function):
        def foward(self, x):
            return x ** 2

