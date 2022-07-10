"""
run length encoding method
https://www.pythonpool.com/run-length-encoding-python/
"""

def run_length_encoding(seq):
    compressed = []
    char = seq[0]
    count = 1
    for i in range(1, len(seq)):
        if char == seq[i]:
            count += 1
        else:
            # elseのタイミング、文字が変わったタイミングでappendする
            compressed.append([char, count])
            char = seq[i]
            count = 1
    compressed.append([char, count])
    return compressed

s = input()
a = run_length_encoding(s)
print(a)
