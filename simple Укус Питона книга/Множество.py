bri = set(['Бразилия', "Россия", "Молдова"])
"Индия" in bri

"Бразилия" in bri

bric = bri.copy()
bric.add("Китай")
bric.issuperset(bri)
bri.remove('Бразилия')

bri & bric
