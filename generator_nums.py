import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Using regular expression for searching the numbers in text.
    pattern = r'\b\d+\.\d+\b'
    # This cycle returning iterator with all matches.
    for match in re.finditer(pattern, text):
        # Using yield construction for generator creating.
        yield float(match.group())
# sum_profit function using generator_numbers function to sum all found numbers and calculating total income.
def sum_profit(
        text: str, 
        func: Callable[[str], Generator[float, None, None]]
        ) -> float:
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
