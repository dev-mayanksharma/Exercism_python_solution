"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in {'J','Q','K'}:
        return 10
    elif card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    facecard = {'K','J','Q'}
    num = {'2','3','4','5','6','7','8','9','10'}
      #both facecards 
    if card_one in facecard and card_two in facecard:
        return (card_one,card_two)
    #one facecard without ace card 
    elif (card_one in facecard or card_two in facecard) and 'A' not in (card_one, card_two):
        if card_one in facecard and card_two !='10':
            return card_one
        elif card_two in facecard and card_one!='10':
            return card_two
        return (card_one,card_two)
    #facecard with ace card 
    elif (card_one in facecard or card_two in facecard) and 'A' in (card_one, card_two):
        if card_one in facecard:
            return card_one
        return card_two  
    #number and ace  cards 
    elif card_one in num or card_two in num:
        if card_one in num and card_two in num:
            if int(card_one) > int(card_two):
                return card_one
            elif int(card_one) == int(card_two):
                return (card_one,card_two)
            return card_two
        elif card_one in num:
            return card_one
        return card_two
    #both ace cards
    else:
        return (card_one,card_two)
    

    
    


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    facecard = {'K','Q','J'}

    if card_one in facecard:
        val_one = 10
    elif card_one == 'A':
        val_one = 11
    else:
        val_one = int(card_one)

    if card_two in facecard:
        val_two = 10
    elif card_two == 'A':
        val_two = 11
    else:
        val_two = int(card_two)

    if val_one + val_two + 11 <= 21:
        return 11
    return 1
     

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    balckjack_card = {'K','Q','10','J'}
    if card_one in balckjack_card and card_two == 'A':
        return True
    elif card_one == 'A' and card_two in balckjack_card:
        return True  
    return False 



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    samevalue = {'K','J','Q','10'}
    num = {'2','3','4','5','6','7','8','9'}
    if card_one in samevalue and card_two in samevalue:
        return True 
    elif card_one in num and card_two in num:
        if int(card_one) == int(card_two):
            return True
        return False
    elif card_one == 'A' and card_two == 'A':
        return True
    return False

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    tens = {'10','K','Q','J'}

    if card_one in tens:          
        val_one = 10
    elif card_one == 'A':
        val_one = 1
    else:
        val_one = int(card_one)

    if card_two in tens:
        val_two = 10
    elif card_two == 'A':         
        val_two = 1
    else:
        val_two = int(card_two)

    if val_one + val_two in {9, 10, 11}:
        return True
    return False
