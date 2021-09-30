# Assignment B
# We want to show prices as ending in either .50, .95, or .00. We always round up to the nearest of these.
# As an example, 99.01 becomes 99.50, and 5.50 becomes 5.50, 99.51 becomes 99.95, and 99.96 becomes 100.00.
# Frederik Juhl Andreasen
# 2021-09-30
import decimal

def show_pretty_price(value: decimal) -> decimal:
    # Extract the fractional part of the value.
    fraction = value % 1
    
    # Edge case if value is a whole number already.
    if fraction == 0.00:
        return value
    # We check in order from smallest->largest to prioritise rounding up.
    elif fraction <= 0.50:
        return value - fraction + 0.50
    elif fraction <= 0.95:
        return value - fraction + 0.95
    else:
        return value - fraction + 1

print(show_pretty_price(99.01))
# 99.50
print(show_pretty_price(5.50))
# 5.50
print(show_pretty_price(99.51))
# 99.95
print(show_pretty_price(99.96))
# 100.00
