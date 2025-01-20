class FizzBuzz:
    def __init__(self):
        pass
    
    def fizzbuzz(self, number: int) -> str:
        rv = ''
        if number % 3 == 0:
            rv += 'Fizz'
        
        if number % 5 == 0:
            rv += 'Buzz'
        
        if len(rv) == 0:
            rv = str(number)
        return rv