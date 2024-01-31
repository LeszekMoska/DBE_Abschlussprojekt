# Benutzereingabe
temperatur = input("Gib die Temperatur ein (warm, kalt): ")
wetter = input("Gib das Wetter ein (regnerisch, verschneit, sonnig): ")

# Vorschlag
if temperatur == "warm":
    if wetter == "sonnig":
        vorschlag = "Trage leichte Kleidung und Sonnencreme."
    elif wetter == "regnerisch":
        vorschlag = "Nimm einen Regenschirm mit und trage leichte Kleidung."
    elif wetter == "verschneit":
        vorschlag = "Macht doch null Sinn!Try again bro mit logischen Eingaben."
    else:
        vorschlag = "Unbekanntes Wetter."
elif temperatur == "kalt":
    if wetter == "sonnig":
        vorschlag = "Trage warme Kleidung und eine Sonnenbrille."
    elif wetter == "regnerisch":
        vorschlag = "Trage warme Kleidung und nimm einen Regenschirm mit."
    elif wetter == "verschneit":
        vorschlag = "Trage winterfeste Kleidung und Stiefel."
    else:
        vorschlag = "Unbekanntes Wetter."

else:
    vorschlag = "Gib bitte nur die möglichen Auswahlen an, sonst wird das nichts."

# Kleidungsvorschlags
print("Kleidungsvorschlag:", vorschlag)
# Zusatz