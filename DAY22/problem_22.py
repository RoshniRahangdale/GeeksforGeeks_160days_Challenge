# POTD -22
# Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith paper. The task is to find the H-index.

# H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times.


# =============================first approach (not good )==================================================
# Python Program to find H-index by sorting

# def hIndex(citations):
    
#     # Sort the citations in descending order
#     citations.sort(reverse=True)
#     n = len(citations)
#     idx = 0

#     # Keep incrementing idx till citations[idx] > idx
#     while idx < n and citations[idx] > idx:
#         idx += 1
#     return idx

# if __name__ == '__main__':
#     citations = [6, 0, 3, 5, 3]
#     print(hIndex(citations))
    
    
    
    # ================================second approach=================================================
# Python Program to find H-index using Counting Sort

def hIndex(citations):
    n = len(citations)
    freq = [0] * (n + 1)

    # Count the frequency of citations
    for citation in citations:
        if citation >= n:
            freq[n] += 1
        else:
            freq[citation] += 1

    idx = n
    
    # Variable to keep track of the count of papers
    # having at least idx citations
    s = freq[n]
    while s < idx:
        idx -= 1
        s += freq[idx]
    
    # Return the largest index for which the count of 
    # papers with at least idx citations becomes >= idx
    return idx

if __name__ == '__main__':
    citations = [6, 0, 3, 5, 3]
    print(hIndex(citations))    