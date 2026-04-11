def response(hey_bob):
    strip = hey_bob.strip()
    if strip == "":
        return "Fine. Be that way!"
    
    is_question = strip.endswith("?")
    has_letters = any(c.isalpha() for c in hey_bob)
    is_yelling = has_letters and hey_bob.upper() == hey_bob

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    return "Whatever."
