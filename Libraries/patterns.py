import pandas as pd


def _average(*inputs: float):
    result = 0.0
    for put in inputs:
        result += put
    return result / len(inputs)


def get_ohcl(candles):
    c_high = candles['high']
    c_low = candles['low']
    c_close = candles['close']
    c_open = candles['open']
    return c_open, c_high, c_close, c_low


def hammer(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_low[0] > c_open[1] > c_close[1] > c_low[1] and c_high[1] < c_low[0]:
        return True
    else:
        return False


def hanging_man(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[1] > c_close[1] > c_high[0] > c_low[1]:
        return True
    else:
        return False


def inverted_hammer(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_low[0] > c_high[1] > c_high[2] > c_close[1] > c_close[2] and c_open[2] < c_close[1] and c_high[2] < c_open[1]:
        return True
    else:
        return False


def shooting_star(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_high[1] > c_high[0] > _average(c_open[1], c_close[1]) and c_open[1] > c_close[1] > c_close[0] \
            and c_open[1] > c_high[0]:
        return True
    else:
        return False


def harami_cross_bullish(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and c_open[0] > c_high[1] and c_close[0] < c_low[1]:
        return True
    else:
        return False


def harami_cross_bearish(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] and c_open[0] < c_low[1] and c_close[0] > c_high[1]:
        return True
    else:
        return False


def doji_star_bullish(candles, limit: float):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and abs(c_open[1] - c_close[1]) < limit and c_high[1] >= c_close[0]:
        return True
    else:
        return False


def doji_star_bearish(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] and c_open[1] > c_close[1] and c_close[1] <= c_close[0] < _average(c_open[1], c_close[1]):
        return True
    else:
        return False


def morning_doji_star(candles, limit: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and abs(c_open[1] - c_close[1]) < limit and c_close[1] < c_open[2] < c_close[2] \
            and c_low[2] >= c_close[1]:
        return True
    else:
        return False


def evening_doji_star(candles, limit: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] and abs(c_open[1] - c_close[1]) < limit and c_close[1] > c_open[2] > c_close[2] \
            and c_high[2] <= c_close[1]:
        return True
    else:
        return False


def abandoned_baby_bullish(candles, limit: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] >= c_high[1] and abs(c_open[1] - c_close[1]) < limit and c_open[2] < c_close[2] \
            and c_close[2] > c_close[0] and c_close[2] >= _average(c_open[0], c_close[0]) and c_open[2] > c_close[1]:
        return True
    else:
        return False


def abandoned_baby_bearish(candles, limit: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] < c_close[1] and abs(c_open[1] - c_close[1]) < limit \
            and c_close[1] > c_open[2] > c_close[2] and _average(c_open[0], c_close[0]) >= c_close[2] \
            and c_high[2] <= c_close[1]:
        return True
    else:
        return False


def tri_star_bullish(candles, limit: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[1] < c_close[2] < c_close[0] and abs(c_open[2] - c_close[2]) < limit \
            and abs(c_open[1] - c_close[1]) < limit and abs(c_open[0] - c_close[0]) < limit:
        return True
    else:
        return False


def tri_star_bearish(candles, limit: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[0] < c_close[2] < c_close[1] and abs(c_open[2] - c_close[2]) < limit \
            and abs(c_open[1] - c_close[1]) < limit and abs(c_open[0] - c_close[0]) < limit:
        return True
    else:
        return False


def three_inside_up(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and c_open[0] > c_close[1] > c_open[1] > c_close[0] \
            and c_open[1] < c_open[2] < c_close[1] and c_open[2] < c_close[2] and c_low[2] >= c_open[1] \
            and c_close[2] > c_open[0]:
        return True
    else:
        return False


def three_inside_down(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[0] > c_open[1] > c_close[1] > c_open[0] > c_close[2] \
            and _average(c_open[1], c_close[1]) > c_open[2] > c_close[2]:
        return True
    else:
        return False


def three_outside_up(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[1] < c_close[0] < c_open[0] < c_close[1] and c_open[2] < c_close[1] < c_close[2]:
        return True
    else:
        return False


def three_outside_down(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[1] > c_close[0] > c_open[0] > c_close[1] > c_close[2] and c_open[2] > c_close[1] \
            and c_high[2] < c_open[1]:
        return True
    else:
        return False


def unique_three_river(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_open[1] > c_close[1] > c_close[0] and c_low[1] < c_low[0] \
            and c_close[0] <= c_open[2] < c_close[2] < c_close[1] < c_high[2]:
        return True
    else:
        return False


def concealing_baby(candles):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and c_open[1] > c_close[0] and c_open[1] > c_close[1] and c_high[2] > c_close[1] \
            and c_close[1] > c_open[2] > c_close[2] and c_open[3] >= c_high[2] and c_close[3] <= c_close[2]:
        return True
    else:
        return False


def loentical_three_cross(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[2] < c_open[2] <= c_close[1] < c_open[1] <= c_close[0] < c_open[0]:
        return True
    else:
        return False


def deliberation(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] and c_open[1] < c_close[1] and c_open[2] < c_close[2] and c_open[1] <= c_close[0] \
            and abs(c_open[2] - c_close[2]) < abs(c_open[1] - c_close[1]) and c_open[2] > c_close[1] and c_low[2] >= \
            c_close[1]:
        return True
    else:
        return False


def matching_low(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[1] <= c_close[0] < c_open[0] <= c_high[1] and c_close[1] < c_open[1] <= c_open[0]:
        return True
    else:
        return False


def matching_high(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[0] > c_open[0] >= c_low[1] and c_close[0] >= c_close[1] > c_open[1] > c_open[0]:
        return True
    else:
        return False


def upside_gap_two_crows(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] and c_open[2] > c_open[1] > c_close[1] > c_close[2] >= c_high[0]:
        return True
    else:
        return False


def homing_pigeon(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_high[0] > c_open[0] >= c_high[1] > c_open[1] > c_close[1] > c_low[1] > c_close[0] > c_low[0]:
        return True
    else:
        return False


def advance_block(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if abs(c_open[2] - c_close[2]) < abs(c_open[1] - c_close[1]) < abs(c_open[0] - c_close[0]) \
            and c_open[0] < c_close[0] and c_open[1] < c_close[1] and c_open[2] < c_close[2] \
            and c_open[1] < c_close[0] and c_open[2] < c_close[1] and c_high[1] > c_close[2] \
            and c_low[2] < _average(c_open[1], c_close[1]):
        return True
    else:
        return False


def two_crows(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if abs(c_open[0] - c_close[0]) > abs(c_open[1] - c_close[1]) \
            and abs(c_open[2] - c_close[2]) > abs(c_open[1] - c_close[1]) and c_open[0] < c_close[0] \
            and c_high[0] <= c_low[1] and c_open[1] > c_close[1] \
            and c_close[1] < c_open[2] <= _average(c_open[1], c_close[1]) and c_open[2] > c_close[2] \
            and c_low[2] < _average(c_open[0], c_close[0]):
        return True
    else:
        return False


def rising_three_methods(candles):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_low[3] >= c_low[0] and c_open[0] <= c_close[3] < c_open[3] < c_close[2] < c_open[2] <= c_close[1] \
            < c_close[1] < c_open[1] and c_high[3] > c_close[2]:
        return True
    else:
        return False


def falling_three_methods(candles):
    # work with at least 5 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] \
            and c_close[4] < c_open[1] < c_open[2] < c_close[1] < c_close[2] < c_open[3] < c_close[3] \
            and c_close[3] > c_open[4] > c_open[3] and c_close[4] < c_low[0]:
        return True
    else:
        return False


def upside_tasuki_gap(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] < c_close[2] < c_open[1] < c_open[2] < c_close[1]:
        return True
    else:
        return False


def downside_tasuki_gap(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] > c_close[2] > c_open[1] > c_open[2] > c_close[1]:
        return True
    else:
        return False


def sidebyside_white_lines_bullish(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] < c_open[2] < c_open[1] < c_close[2] < c_close[1] <= c_high[2] and c_low[1] > c_high[0]:
        return True
    else:
        return False


def sidebyside_white_lines_bearish(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] > c_close[1] >= c_close[2] > c_open[2] >= c_open[1] and c_high[1] <= c_low[0]:
        return True
    else:
        return False


def three_line_strike_bullish(candles, tolerance: float):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    first = abs(c_open[2] - c_close[2])
    sec = abs(c_open[1] - c_close[1])
    third = abs(c_open[0] - c_close[0])

    if c_close[3] < c_open[0] < c_open[1] < c_close[0] <= c_open[2] < c_close[1] < c_close[2] <= c_open[3] \
            and c_high[2] >= c_high[3] and abs(first - sec) < tolerance and abs(sec - third) < tolerance:
        return True
    else:
        return False


def separating_lines_bullish(candles, tolerance: float):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    first = abs(c_open[1] - c_close[1])
    sec = abs(c_open[0] - c_close[0])

    if abs(first - sec) < tolerance and c_open[0] > c_close[0] and c_high[0] > c_open[1] and c_open[1] < c_close[1] \
            and c_low[1] < c_open[0] < c_open[1]:
        return True
    else:
        return False


def separating_lines_bearish(candles, tolerance: float):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    first = abs(c_open[1] - c_close[1])
    sec = abs(c_open[0] - c_close[0])

    if abs(first - sec) < tolerance and c_open[0] < c_close[0] < c_open[1] <= c_open[0] < c_high[1] \
            and c_low[0] < c_open[1]:
        return True
    else:
        return False


def three_line_strike_bearish(candles, tolerance: float):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    first = abs(c_open[2] - c_close[2])
    sec = abs(c_open[1] - c_close[1])
    third = abs(c_open[0] - c_close[0])

    if c_open[3] < c_close[2] < c_close[1] < c_open[2] < c_close[0] < c_open[1] < c_open[0] < c_close[3] \
            and c_high[0] < c_close[3] and abs(first - sec) < tolerance and abs(sec - third) < tolerance:
        return True
    else:
        return False


def upside_gap_three_methods(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[2] < c_close[0] < c_open[1] < c_open[2] < c_close[1] and c_low[1] > c_high[0]:
        return True
    else:
        return False


def downside_gap_three_methods(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[2] > c_close[0] > c_open[1] > c_open[2] > c_close[1] and c_high[1] < c_low[0]:
        return True
    else:
        return False


def on_neck_line_bullish(candles, tolerance: float):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] < c_close[1] < c_open[1] and abs(c_low[1] - c_close[1]) < tolerance \
            and abs(c_open[0] - c_close[0]) > abs(c_open[1] - c_close[1]) and c_close[1] <= c_high[0]:
        return True
    else:
        return False


def on_neck_line_bearish(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] > c_close[1] > c_open[1] and abs(c_open[0] - c_close[0]) > abs(c_open[1] - c_close[1]) \
            and c_close[1] <= c_low[0]:
        return True
    else:
        return False


def breakaway_bullish(candles):
    # work with at least 5 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] > c_open[1] and c_close[1] < c_close[2] < c_open[2] and c_open[3] > c_close[2] \
            and c_open[3] > c_close[3] and c_open[4] < c_close[4] and c_open[4] < c_open[3] and c_close[4] > c_open[1]:
        return True
    else:
        return False


def breakaway_bearish(candles):
    # work with at least 5 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] <= c_open[1] < c_close[1] < c_close[2] < c_open[1] < c_open[2] \
            and c_open[2] > c_close[2] and c_close[2] < c_open[3] < c_close[3] and c_close[3] > c_open[2] \
            and c_open[4] < _average(c_open[3], c_close[3]) and c_close[4] < c_open[1]:
        return True
    else:
        return False


def in_neck_line_bullish(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] <= c_close[1] < c_open[1] and abs(c_open[0] - c_close[0]) > abs(c_open[1] - c_close[1]):
        return True
    else:
        return False


def in_neck_line_bearish(candles):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] >= c_close[1] > c_open[1] and abs(c_open[0] - c_close[0]) > abs(c_open[1] - c_close[1]):
        return True
    else:
        return False


# pin script
def three_white_soldiers(candles):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] > c_open[1] and c_close[1] > _average(c_close[1], c_open[1]) \
            and c_open[1] < c_open[2] < c_close[1] and c_close[2] > _average(c_close[2], c_open[2]) \
            and c_open[2] < c_open[3] < c_close[2] and c_close[3] > _average(c_close[3], c_open[3]) \
            and c_high[1] < c_high[2] < c_high[3]:
        return True
    else:
        return False


def three_black_crows(candles):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] < c_open[1] and c_close[1] < _average(c_close[1], c_open[1]) \
            and c_open[1] > c_open[2] > c_close[1] and c_close[2] < _average(c_close[2], c_open[2]) \
            and c_open[2] > c_open[3] > c_close[2] and c_close[3] < _average(c_close[3], c_open[3]) \
            and c_low[1] > c_low[2] > c_low[3]:
        return True
    else:
        return False


def engulfing_bullish(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_high[2] > c_high[1] and c_low[2] < c_low[1] and c_open[2] < c_open[1] and c_close[2] > c_close[1] \
            and c_close[2] > c_open[2] and c_close[1] < c_close[0] and c_close[2] > c_open[1]:
        return True
    else:
        return False


def engulfing_bearish(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_high[2] > c_high[1] and c_low[2] < c_low[1] and c_open[2] > c_open[1] and c_close[2] < c_close[1] \
            and c_close[2] < c_open[2] and c_close[1] > c_close[0] and c_close[2] < c_open[1]:
        return True
    else:
        return False


def harami_bullish(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[1] > c_close[1] and c_close[1] < c_close[0] and c_close[1] < c_open[2] < c_open[1] \
            and c_close[1] < c_close[2] < c_open[1] and c_high[2] < c_high[1] and c_low[2] > c_low[1] \
            and c_close[2] >= c_open[2]:
        return True
    else:
        return False


def harami_bearish(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[1] < c_close[1] and c_close[1] > c_close[0] and c_close[1] > c_open[2] > c_open[1] \
            and c_close[1] > c_close[2] > c_open[1] and c_high[2] < c_high[1] and c_low[2] > c_low[1] \
            and c_close[2] <= c_open[2]:
        return True
    else:
        return False


def piercing_line(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[0] > c_close[1] and c_open[2] < c_low[1] and _average(c_open[1], c_close[1]) < c_close[2] < c_open[1]:
        return True
    else:
        return False


def dark_cloud_cover(candles):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[0] < c_close[1] and c_open[2] > c_high[1] and _average(c_open[1], c_close[1]) > c_close[2] > c_open[1]:
        return True
    else:
        return False


def morning_star(candles):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[0] > c_close[1] > c_open[2] and c_open[1] > c_close[1] > c_close[2] \
            and c_open[3] > c_open[2] and c_open[3] > c_close[2] and c_close[3] > c_close[1] \
            and c_open[1] - c_close[1] > c_close[3] - c_open[3]:
        return True
    else:
        return False


def evening_star(candles):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_close[0] < c_close[1] < c_open[2] and c_open[1] < c_close[1] < c_close[2] \
            and c_open[3] < c_open[2] and c_open[3] < c_close[2] and c_close[3] < c_close[1] \
            and c_close[1] - c_open[1] > c_open[3] - c_close[3]:
        return True
    else:
        return False


def belt_hold_bullish(candles, tolerance: float):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] > c_open[1] and c_low[0] > c_open[1] and abs(c_open[1] - c_low[1]) < tolerance \
            and c_close[1] > _average(c_close[1], c_open[1]):
        return True
    else:
        return False


def belt_hold_bearish(candles, tolerance: float):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] < c_open[1] and c_high[0] < c_open[1] \
            and abs(c_open[1] - c_high[1]) < tolerance and c_close[1] < _average(c_close[1], c_open[1]):
        return True
    else:
        return False


def three_stars_in_the_south(candles, tolerance: float):
    # work with at least 4 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and c_open[1] > c_close[1] and abs(c_open[1] - c_high[1]) < tolerance \
            and c_close[2] < c_open[2] < c_open[1] and c_open[2] > c_close[1] and c_low[2] > c_low[1] \
            and abs(c_open[2] - c_high[2]) < tolerance and c_close[3] < c_open[3] < c_open[2] \
            and c_open[3] > c_close[2] and abs(c_open[3] - c_high[3]) < tolerance \
            and abs(c_close[3] - c_low[3]) < tolerance and c_close[3] >= c_low[2]:
        return True
    else:
        return False


def stick_sandwich(candles, tolerance: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and c_close[0] < c_open[1] < c_close[1] < c_open[2] and c_open[2] > c_close[2] \
            and abs(c_close[2] - c_close[0]) < tolerance:
        return True
    else:
        return False


def meeting_line_bullish(candles, tolerance: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and c_open[1] > c_close[1] and abs(c_close[1] - c_close[2]) < tolerance \
            and c_open[2] < c_close[2] and c_open[1] >= c_high[2]:
        return True
    else:
        return False


def meeting_line_bearish(candles, tolerance: float):
    # work with at least 3 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] and c_open[1] < c_close[1] and abs(c_close[1] - c_close[2]) < tolerance \
            and c_open[2] > c_close[2] and c_open[1] <= c_low[2]:
        return True
    else:
        return False


def kicking_bullish(candles, tolerance: float):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and abs(c_open[0] - c_high[0]) < tolerance and abs(c_close[0] - c_low[0]) < tolerance \
            and c_open[1] > c_open[0] and abs(c_open[1] - c_low[1]) < tolerance \
            and abs(c_close[1] - c_high[1]) < tolerance and c_close[1] - c_open[1] > c_open[0] - c_close[0]:
        return True
    else:
        return False


def kicking_bearish(candles, tolerance: float):
    # work with at least 2 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] < c_close[0] and abs(c_open[0] - c_low[0]) < tolerance and abs(c_close[0] - c_high[0]) < tolerance \
            and c_open[1] < c_open[0] and abs(c_open[1] - c_high[1]) < tolerance \
            and abs(c_close[1] - c_low[1]) < tolerance and c_open[1] - c_close[1] > c_close[0] - c_open[0]:
        return True
    else:
        return False


def ladder_bottom(candles):
    # work with at least 5 candle and return True if pattern be true
    c_open, c_high, c_close, c_low = get_ohcl(candles)
    if c_open[0] > c_close[0] and c_close[1] < c_open[1] < c_open[0] and c_close[2] < c_open[2] < c_open[1] \
            and c_close[3] < c_open[3] < c_open[2] and c_close[4] > c_open[4] > c_open[3] \
            and c_low[0] > c_low[1] > c_low[2] > c_low[3]:
        return True
    else:
        return False


def candles_manager(candles):
    c_high, c_low, c_close, c_open = [], [], [], []
    for index, candle in candles.iterrows():
        c_high.append(candle['high'])
        c_low.append(candle['low'])
        c_close.append(candle['close'])
        c_open.append(candle['open'])
        print(index)
    return c_open, c_high, c_close, c_low


def get_all_patterns(dataframe: pd.DataFrame):
    # all patterns that work with 2 candles
    for i in range(0, len(dataframe), 2):
        try:
            dataframe.loc[i + 1, 'hammer'] = 1 if hammer(dataframe[i:i + 2].reset_index(drop=True)) else 0
            # do for all 2 candles patterns
        except:
            break
    # all patterns that work with 3 candles
    for i in range(0, len(dataframe), 3):
        try:
            dataframe.loc[i + 2, 'inverted_hammer'] = 1 if inverted_hammer(
                dataframe[i:i + 3].reset_index(drop=True)) else 0
            # do for all 3 candles patterns
        except:
            break

    # all patterns that work with 4 candles
    for i in range(0, len(dataframe), 4):
        try:
            dataframe.loc[i + 3, 'concealing_baby'] = 1 if concealing_baby(
                dataframe[i:i + 4].reset_index(drop=True)) else 0
            # do for all 4 candles patterns
        except:
            break
    # all patterns that work with 5 candles
    for i in range(0, len(dataframe), 5):
        try:
            dataframe.loc[i + 4, 'falling_three_methods'] = 1 if falling_three_methods(
                dataframe[i:i + 5].reset_index(drop=True)) else 0
            # do for all 5 candles patterns
        except:
            break
    return dataframe

