
def calculate_price_change(prices):

    if len(prices) <= 1 or prices[0] == 0:
        return None, None
    else:
        start_price = prices[0]
        last_price = prices[-1]
        price_change = last_price - start_price
        price_change_percent = (price_change / start_price) * 100

    return price_change, price_change_percent

def get_price_movement(price_change):

    if price_change is None:
        return "Invalid price change"
    else:
        if price_change > 0:
            return "Up"
        elif price_change < 0:
            return "Down"
        else:
            return "Flat"
