# Assignment A
# We want to show payment cards as CARDTYPE####XXXXXXXX####.
# Frederik Juhl Andreasen
# 2021-09-30

def get_card_mask(card_type: str, card_number: str) -> str:
    return card_type + card_number[0 : 4] + 'XXXXXXXX' + card_number[-4 : -1] + card_number[-1]


print(get_card_mask('VISA', '12345678887654321'))
# VISA1234XXXXXXXX4321
