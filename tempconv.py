"""Temperature conversions. Practice code for the Gitar dry run."""


def c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def c_to_k(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return celsius + 273.15
