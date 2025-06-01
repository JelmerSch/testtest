print("Welkom bij mijn Pizzeria")
pizza_Maat = input("Hoe groot mag je pizza zijn? (s, m, l,): ").lower()
pepperoni = input("Wil je pepperoni op je pizza? (Ja/Nee): ").lower()
extra_Kaas = input("Wil je extra kaas op je pizza? (Ja/Nee): ").lower()
prijs = 0
if pizza_Maat == "s":
    prijs = 15
    if pepperoni == "ja":
        prijs += 2
elif pizza_Maat == "m":
    prijs = 20
    if pepperoni == "ja":
        prijs += 3
elif pizza_Maat == "L":
    prijs = 25
    if pepperoni == "ja":
        prijs +=3
if extra_Kaas == "ja":
    prijs += 1
print(f"Bedankt voor uw bestelling! Uw pizza kost €{prijs}")