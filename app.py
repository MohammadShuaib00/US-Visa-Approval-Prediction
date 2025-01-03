# Example usage:

from usvisa.exception.exception import usvisaException
import sys
try:
    # Some code that may raise an error
    raise ValueError("An example error")
except Exception as e:
    # Raising the custom exception with a simplified message
    raise usvisaException(str(e))
