class FizzBuzz:
    """Implements the FizzBuzz programming example
    """
    def __init__(self):
        pass

    def fizzbuzz(self, number: int) -> str:
        """Implements fizzbuzz sequence

        Args:
            number (int): number in the sequence

        Returns:
            str: output of the sequence
        """
        if not isinstance(number, int) or number <= 0:
            raise ValueError(f"Invalid number input: {number}")
        rv = ''
        if number % 3 == 0:
            rv += 'Fizz'

        if number % 5 == 0:
            rv += 'Buzz'

        if len(rv) == 0:
            rv = str(number)
        return rv
