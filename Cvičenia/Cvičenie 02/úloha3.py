#total_width +3 bol len pokus omyl ale funguje pri kazdom zarovnani. FTW!!!!

def tabulka(width):
    total_width = width*4
    print("+{:-^{}}+".format("Tabuľka číselných sústav", total_width+3))
    print("|{:^{width}}|{:^{width}}|{:^{width}}|{:^{width}}|".format("dec", "bin", "hex", "oct", width = width))
    print("+{:-^{}}+".format("",total_width+3))
    for i in range(0, 16):
        print("|{:^{width}}|{:<{width}}|{:<{width}}|{:<{width}}|".format(i, bin(i), hex(i), oct(i), width=width))
    print("+{:-^{}}+".format("",total_width+3))

width = int(input("Zadaj počet znakov zarovnania : "))
tabulka(width)












