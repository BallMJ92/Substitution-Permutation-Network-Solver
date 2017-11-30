class xor:

    def main(self):
        bits, key, xored, permutation = [], [], [], []

        userinput = str(input("enter bits: "))
        xorby = str(input("enter XOR key: "))

        bits.append(userinput[0]), bits.append(userinput[1]), bits.append(userinput[2])
        key.append(xorby[0]), key.append(xorby[1]), key.append(xorby[2])

        print("Bits: ", bits)
        print("Key: ", key)

        if bits[0] == key[0]:
            xored.append("0")
        else:
            xored.append("1")

        if bits[1] == key[1]:
            xored.append("0")
        else:
            xored.append("1")

        if bits[2] == key[2]:
            xored.append("0")
        else:
            xored.append("1")

        print("After Xoring: ",xored)

        permutation.append(xored[2]), permutation.append(xored[0]), permutation.append(xored[1])

        print("After S-Box Permutation: ", permutation)

if __name__ == '__main__':
    xoring = xor()
    xoring.main()