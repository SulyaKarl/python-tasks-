import math

# 17-НҰСҚА

def task_17_1(N=400):
    """
    17-нұсқа, 1-есеп:
    400 символдан тұратын алфавит. 2^k >= N шарты бойынша 
    әр символға қажетті бит санын (k) есептеу.
    """
    k = math.ceil(math.log2(N))
    return k

def task_17_2(encoded_msg, codes):
    """
    17-нұсқа, 2-есеп:
    Хабарды солдан оңға қарай кодтық сөздерге бөліп декодтау.
    Хабар: 1010110111
    """
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_chars = []
    current_code = ""
    
    for bit in encoded_msg:
        current_code += bit
        if current_code in reverse_codes:
            decoded_chars.append(reverse_codes[current_code])
            current_code = ""
            
    return "".join(decoded_chars)


# 7-НҰСҚА

def task_7_1(N=121):
    """
    7-нұсқа, 1-есеп:
    121 символдан тұратын алфавит. 2^k >= N шарты бойынша 
    әр символға қажетті бит санын (k) есептеу.
    """
    k = math.ceil(math.log2(N))
    return k

def task_7_2(encoded_msg, codes):
    """
    7-нұсқа, 2-есеп:
    Хабарды солдан оңға қарай кодтық сөздерге бөліп декодтау.
    Хабар: 111011010
    """
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_chars = []
    current_code = ""
    
    for bit in encoded_msg:
        current_code += bit
        if current_code in reverse_codes:
            decoded_chars.append(reverse_codes[current_code])
            current_code = ""
            
    return "".join(decoded_chars)


if __name__ == "__main__":
    codes = {'A': '0', 'B': '10', 'C': '110', 'D': '111'}

    print("--- 17-НҰСҚА ---")
    res_17_1 = task_17_1(400)
    print(f"1-есеп жауабы: {res_17_1} бит (2^9 >= 400)")
    
    msg_17 = "1010110111"
    res_17_2 = task_17_2(msg_17, codes)
    print(f"2-есеп декодталған мәтіні ('{msg_17}'): {res_17_2}\n")

    print("--- 7-НҰСҚА ---")
    res_7_1 = task_7_1(121)
    print(f"1-есеп жауабы: {res_7_1} бит (2^7 >= 121)")
    
    msg_7 = "111011010"
    res_7_2 = task_7_2(msg_7, codes)
    print(f"2-есеп декодталған мәтіні ('{msg_7}'): {res_7_2}")
