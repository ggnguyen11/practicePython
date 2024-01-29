# practicepython.org | exercise 13 | 01/29/2024
# prompt: write program asking user how many Fibonnaci numbers to generate
# and then generate them. Use functions, ask user to enter number of numbers
# in the sequence to generate.
# hint: fibonnaci sequence is a sequence of numbers where the next number
# in the sequence is the sum of the previous two numbers
# ex: (1, 1, 2, 3, 5, 8, 13, 21)
fibSeq = []

fibSeqLength = int(input("Give me a number for the length of the fibonacci" \
                         + " sequence to be generated: "))

def gen_fibSeq(fibSeqLength):
    fibSeq.append(1)
    fibSeq.append(1)
    for i in range(fibSeqLength - 2):
        fibSeq.append((fibSeq[i]) + (fibSeq[i + 1]))
        i += 1
    print(fibSeq)

gen_fibSeq(fibSeqLength)