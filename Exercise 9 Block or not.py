def bot8(pbot, p8_bot, p8_human):
    pbot_8 = 0
    p_human = 1 - pbot
    p8d = 0
    # P(8-digits) = P(8-digits | bot) x P(bot) + P(8-digits | human) x P(human)
    p8d = p8_bot * pbot + p8_human * p_human
    print("todennäköisyys, että seuraajan nimessä on 8-numeroinen koodi %s%%" % (p8d * 100))

    # P(bot | 8 - digits) = P(8-digits | bot)* P(bot) / P(8-digits)
    pbot_8 = (p8_bot * pbot) / p8d

    print(pbot_8)


# you can change these values to test your program with different values
pbot = 0.1  # todennäköisyys, että uusi seuraaja on botti -> P(bot)
p8_bot = 0.8  # todennäköisyys, että botin nimessä on 8-numeroinen koodi
# -> P(8-digits | bot)
p8_human = 0.05  # todennäköisyys, että ihmisen nimessä on 8-numeroinen koodi
# -> P(8-digits | human)
# P(8-digits) = P(8-digits | bot) x P(bot) + P(8-digits | human) x P(human)
# -> todennäköisyys, että nimessä (botti tai ihminen) on 8-numeroinen koodi

bot8(pbot, p8_bot, p8_human)
