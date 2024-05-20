from forex_python.converter import CurrencyRates

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    currency = select_currency()
    converted = convert_to_dollars(dollars, currency)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = converted * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    new_d = d.replace("$", "")
    return float(new_d)

def percent_to_float(p):
    new_p = p.replace("%", "")
    p_converted = float(new_p) / 100
    return p_converted

def select_currency():
    currencies = {
        'USD': 'US Dollar',
        'EUR': 'Euro',
        'GBP': 'Pound',
    }
    print("What currency would you like to use?")
    for code, name in currencies.items():
        print(f"{code}: {name}")
    while True:
        choice = input("Enter 3 letter currency code: ").upper()
        if choice in currencies:
            return choice
        else:
            print("Currency code not supported. Please try again.")

def convert_to_dollars(amount, currency):
    c = CurrencyRates()
    return c.convert(currency, 'USD', amount)

main()
