# Funktion "Berechnung"
def berechnung():
    # Abfrage von Ist-Länge und Ist-QRG
    print()
    laengeist = float(input("Aktuelle Schenkellänge des Dipols in Meter: "))
    qrgist = float(input("Aktuelle Resonanzfrequenz in MHz mit bestem SWV: "))
    # Abfrage von Soll-QRG
    qrgsoll = float(input("Gewünschte Frequenz in MHz: "))
    # Berechnung Verkürzungsfaktor
    vf = laengeist / ((300.0/qrgist)/4.0)
    # Berechnung der Soll-Länge
    laengesoll = round(((300.0/qrgsoll)/4.0)*vf, 2)
    # Ausgabe der Ergebnisse
    print()
    print("Aktueller Verkürzungsfaktor:", round(vf, 3))
    print("Ideale Schenkellänge für", qrgsoll,  "MHz:", laengesoll, "Meter.")
    print()

# Begrüßung
print()
print("Dipolschenkelrechner von DL1NUX (C) 2021")
print()
print("Bitte alle Dezimalzahlen mit Punkt eingeben, NICHT mit Komma!")
wiederholen="Y"
while wiederholen.upper()=="Y" or wiederholen.upper()=="J":
    berechnung()
    wiederholen = input("Nochmal berechnen [J,Y,N]? ")
    if wiederholen.upper()=="Y" or wiederholen.upper()=="J":
      print()
      print("Und weiter gehts ...")
      
print()
print("Viel Erfolg beim Basteln!")
print("--... ...--")
print()