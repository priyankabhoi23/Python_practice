def convert(octal):
    print("Equivalent Binary Number:",end="")
    for i in range(len(octal)):
        switcher={
             0: "000",
            1: "001",
            2: "010",
            3: "011",
            4: "100",
            5: "101",
            6: "110",
            7: "111"
        }
        print(switcher.get(int(octal[i]),"Invalid Octal Number"),end="")
octal=list(input("Insert an octal number:"))
convert(octal)