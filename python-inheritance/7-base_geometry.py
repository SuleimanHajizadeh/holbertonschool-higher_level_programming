def integer_validator(self, name, value):
    """Validate that value is a positive integer."""
    if type(value) is not int:  # burada bool da int deyil
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")
