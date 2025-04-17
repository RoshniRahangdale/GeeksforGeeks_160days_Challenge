def trim_leading_zeros(s):
    first_one = s.find('1')
    return s[first_one:] if first_one != -1 else "0"

def add_binary(s1, s2):
    s1 = trim_leading_zeros(s1)
    s2 = trim_leading_zeros(s2)

    n = len(s1)
    m = len(s2)

    # Ensure s1 is the longer string
    if n < m:
        s1, s2 = s2, s1
        n, m = m, n

    j = m - 1
    carry = 0
    result = []

    for i in range(n - 1, -1, -1):
        bit1 = int(s1[i])
        bit_sum = bit1 + carry

        if j >= 0:
            bit2 = int(s2[j])
            bit_sum += bit2
            j -= 1

        bit = bit_sum % 2
        carry = bit_sum // 2
        result.append(str(bit))

    if carry > 0:
        result.append('1')

    return ''.join(result[::-1])

if __name__ == "__main__":
    s1 = [10010]
    s2 = [1010]
    result = add_binary(s1, s2)
    print("Sum of binary strings:", result)
