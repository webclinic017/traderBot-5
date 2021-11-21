"""
    Mr.Kataei 11/12/2021
    need risk profile for users - this work just for Aran account
"""

from Account.clients import BitfinexClient


def buy_market(client: BitfinexClient, symbol: str, percent: float):
    amount = client.get_balance_available(symbol=symbol, direction=1)
    amount = amount * percent
    result = client.submit_market_order(symbol=symbol, amount=str(amount))
    return result


def sell_market(client: BitfinexClient, symbol: str, percent: float):
    amount = client.get_balance_available(symbol=symbol, direction=-1)
    amount = amount * percent
    result = client.submit_market_order(symbol=symbol, amount=str(amount))
    return result

