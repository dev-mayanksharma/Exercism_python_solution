def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    decimal_value = 0
    for digit in digits:
        
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
        
       
        decimal_value = decimal_value * input_base + digit

    if decimal_value == 0:
        return [0]
    result_digits = []
    while decimal_value > 0:
        result_digits.append(decimal_value % output_base)
        decimal_value //= output_base
    return result_digits[::-1]
