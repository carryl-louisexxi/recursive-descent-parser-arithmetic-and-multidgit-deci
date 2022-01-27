class Arithmetic:  # recursive-descent parser for arithmetic expression
    def __init__(self):
        self.current = 0
        self.token = ''
        self.err = False
        self.string = ''
        self.digit = ['0', '1', '2', '3']

    def getString(self):
        self.string = input('String:')

    def getChar(self):
        self.token = self.string[self.current]
        self.current += 1

    def match(self):
        self.getChar()

    def error(self):
        self.err = True

    def factor(self):
        if self.token in self.digit:
            self.match()
        elif self.token == '(':
            self.match()
            self.exp()
            if self.token == ')':
                self.match()
            else:
                self.error()
        else:
            self.error()

    def term(self):
        self.factor()
        while self.token == '*' or self.token == '/':
            self.match()
            self.factor()

    def exp(self):
        self.term()
        while self.token == '+' or self.token == '-':
            self.match()
            self.term()

    def valid(self):
        print('Valid Input String!')

    def invalid(self):
        print('Invalid Input String!')

    def isCheckString(self):
        for char in self.string:
            if '$' == char:
                return True
        return False

    def main(self):
        self.getString()
        if self.isCheckString():
            self.getChar()
            self.exp()
            if self.token != '$' or self.err:
                self.invalid()
            else:
                self.valid()
        else:
            self.invalid()


class MultiDeci:  # recursive-descent parser for multi-digit decimal number
    def __init__(self):
        self.current = 0
        self.token = ''
        self.err = False
        self.deci = False
        self.string = ''
        self.digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def getString(self):
        self.string = input('String:')

    def getChar(self):
        self.token = self.string[self.current]
        self.current += 1

    def match(self):
        self.getChar()

    def digits(self):
        if self.token == '.' and not self.deci:
            self.match()
            self.deci = True
        else:
            return

    def num(self):
        while self.token in self.digit:
            self.match()
            self.digits()

    def exp(self):
        if self.token == '+' or self.token == '-':
            self.match()
        self.num()

    def valid(self):
        print('Valid Input String!')

    def invalid(self):
        print('Invalid Input String!')

    def isCheckString(self):
        for char in self.string:
            if '$' == char:
                return True
        return False

    def main(self):
        self.getString()

        if self.isCheckString():
            self.getChar()
            self.exp()
            if self.token == '$':
                self.valid()
            else:
                self.invalid()
        else:
            self.invalid()


def main():
    select = """
             1. Arithmetic Expression.
             2. Multi-digit Decimal Number.
             3. Quit.
             """
    print(select)

    while True:
        try:
            choice = int(input('Choice of Expression:'))
        except:
            print('Value Error')
        else:
            if choice == 1:
                arith = Arithmetic()
                arith.main()
            elif choice == 2:
                multi = MultiDeci()
                multi.main()
            elif choice == 3:
                return
            else:
                print('Input Out of Range')


main()
