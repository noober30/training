veta = "the quick brown fox jumps over the lazy dog"
compr = [len(x) for x in veta.split() if x != "the"]
print(compr)


slova = veta.split()
slova_dlzka = []
for slovo in slova:
      if slovo != "the":
          slova_dlzka.append(len(slovo))
print(slova_dlzka)