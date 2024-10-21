import re

def generator_numbers(text):
    patern = r"\d+\.\d+"
    for match in re.findall(patern, text):
        yield float(match)

    


def sum_profit(text, func):
    return sum(func(text))

text = '''Загальний дохід працівника складається з декількох частин: 2000.01 як основний дохід, 
доповнений додатковими надходженнями 37.45 і 324.00 доларів.'''
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

