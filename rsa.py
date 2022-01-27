import math
from random import randint

alphabet = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_len = len(alphabet)

def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def phi(p, q):
    return (p - 1) * (q - 1)

def find_e(p, q):
    euler = phi(p,q)
    for e in range(3, euler):
        if gcd(e, euler) == 1:
            return e
    raise Exception("E cannot be found! Choose another pair of (p, q)")

def get_message_number(message, n):
    length = len(message)
    s = 0
    power = 0
    for i in range(length - 1, -1, -1):
        index = alphabet.index(message[i])
        s = s + index * pow_mod(alphabet_len, power, n)
        power = power + 1      
    return s

def pow_mod(base, exponent, n):
    p = 1
    for _ in range(exponent):
        p = (p * base) % n 
    return p

def encrypt(message, p, q, l, k):
    n = p * q
    print("n: ", n)
    print("phi(n): ", phi(p,q))
    e = find_e(p, q)
    print("e: ", e)
    blocks = get_blocks(message, k)
    numeric = get_blocks_numerical_equivalent(message, k, n)
    print("blocks: ", blocks)
    print("numeric: ", numeric)
    for num in numeric:
        numc = pow_mod(num, e, n)
        coef = generate_coef(l)
        sum =  get_sum_of_pseudo_linear_combination(coef, l)
        while not sum == numc:
            coef = generate_coef(l)#this should be done in a cleaner way
            sum = get_sum_of_pseudo_linear_combination(coef, l)
        block_encrypted = ""
        for c in coef:
            block_encrypted = block_encrypted + alphabet[c]
        print(coef, '-> ', sum, ' ->', block_encrypted)

def get_sum_of_pseudo_linear_combination(coef, l):
    s = 0
    for p in range(l - 1, -1, -1):
        s = s + coef[l-p-1] * pow(alphabet_len, p)
    return s

def generate_coef(l):
    coef = []
    for _ in range(l):
        coef.append(randint(0, alphabet_len - 1))
    return coef

def get_blocks_numerical_equivalent(message, k, n):
    blocks = get_blocks(message, k)
    numeric = []
    for block in blocks:
        numeric.append(get_message_number(block, n))
    return numeric

def get_blocks(message, k):
    length = len(message)
    blocks = []
    for i in range(0, length, k):
        if i + k > length - 1:
            last_block = ""
            for j in range(i, length):
                last_block = last_block + message[j]
            for j in range(i + k - length):
                last_block  = last_block + "_"
            blocks.append(last_block)
        else:
            blocks.append(message[i:i+k])
    return blocks

def decrypt(message, p, q, l, k): 
    n = p * q
    print("n: ", n)
    print("phi(n): ", phi(p,q))
    e = find_e(p, q)
    print("e: ", e)
    d = get_d(e, p, q)
    print("d: ", d)
    blocks = get_blocks(message, l)
    numeric = get_blocks_numerical_equivalent(message, l, n)
    print("blocks: ", blocks)
    print("numeric: ", numeric)
    for num in numeric:
        numc = pow_mod(num, d, n)
        coef = generate_coef(k)
        sum =  get_sum_of_pseudo_linear_combination(coef, k)
        while not sum == numc:
            coef = generate_coef(k)#this should be done in a cleaner way
            sum = get_sum_of_pseudo_linear_combination(coef, k)
        block_decrypted = ""
        for c in coef:
            block_decrypted = block_decrypted + alphabet[c]
        print(coef, '-> ', sum, ' ->', block_decrypted)

#d = e^-1 mod phi(n) the private key
def get_d(e, p, q):
    n = p * q
    phif = phi(p, q)
    gcd, a, b = extended_euclidian_algorithm(phif, e)
    assert(gcd == 1)
    assert(1 == a * phif + b * e)
    if b < 0:
        return -b
    return b

def extended_euclidian_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidian_algorithm(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

print("##################################")
for i in range(alphabet_len):
    print(i , ' -> ', alphabet[i])
print("##################################")
encrypt('PARIS_', 43, 61, 3, 2)
print("##################################")
decrypt('DOMFAFFYB', 53, 97, 3, 2)