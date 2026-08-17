# Beispieldaten
tagestemperaturen = [18, 22, 19, 25, 21, 17, 23]


# 1. Summe berechnen
def berechne_summe(werte):
    summe = 0
    for wert in werte:
        summe += wert
    return summe


# 2. Höchstwert finden
def finde_hoechstwert(werte):
    hoechstwert = werte[0]
    for wert in werte:
        if wert > hoechstwert:
            hoechstwert = wert
    return hoechstwert


# 3. Niedrigstwert finden
def finde_niedrigstwert(werte):
    niedrigstwert = werte[0]
    for wert in werte:
        if wert < niedrigstwert:
            niedrigstwert = wert
    return niedrigstwert


# 4. Durchschnitt berechnen (nutzt berechne_summe)
def berechne_durchschnitt(werte):
    summe = berechne_summe(werte)
    anzahl = len(werte)
    return summe / anzahl


# 5. Lineare Suche (einzelner Wert)
def lineare_suche(werte, gesuchter_wert):
    for index in range(len(werte)):
        if werte[index] == gesuchter_wert:
            return index
    return -1


# 6. Lineare Suche im Bereich (alle Indizes)
def lineare_suche_bereich(werte, untere_grenze, obere_grenze):
    gefundene_indizes = []
    for index in range(len(werte)):
        if untere_grenze <= werte[index] <= obere_grenze:
            gefundene_indizes.append(index)
    return gefundene_indizes


# Mehrwochen-Daten
wochen = [
    [18, 21, 19, 23, 17, 20, 22],
    [15, 16, 18, 20, 19, 17, 16],
    [22, 24, 23, 25, 21, 20, 19]
]  # 3 Wochen à 7 Tage


# 7. Durchschnitt einer bestimmten Woche
def berechne_wochendurchschnitt(wochen, woche_index):
    woche = wochen[woche_index]
    return berechne_durchschnitt(woche)


# 8. Woche mit höchstem Durchschnitt finden
def finde_beste_woche(wochen):
    bester_index = 0
    bester_durchschnitt = berechne_wochendurchschnitt(wochen, 0)

    for woche_index in range(len(wochen)):
        durchschnitt = berechne_wochendurchschnitt(wochen, woche_index)
        if durchschnitt > bester_durchschnitt:
            bester_durchschnitt = durchschnitt
            bester_index = woche_index

    return bester_index


# 9. Lineare Suche in der gesamten 2D-Liste
def lineare_suche_2d(wochen, gesuchter_wert):
    for woche_index in range(len(wochen)):
        for tag_index in range(len(wochen[woche_index])):
            if wochen[woche_index][tag_index] == gesuchter_wert:
                return (woche_index, tag_index)
    return None


# --- Testausgaben ---
if __name__ == "__main__":
    print("=== 1D-Liste: Tagestemperaturen ===")
    print("Werte:", tagestemperaturen)
    print("Summe:", berechne_summe(tagestemperaturen))
    print("Höchstwert:", finde_hoechstwert(tagestemperaturen))
    print("Niedrigstwert:", finde_niedrigstwert(tagestemperaturen))
    print("Durchschnitt:", berechne_durchschnitt(tagestemperaturen))

    print("\n--- Lineare Suche ---")
    print("Index von 25:", lineare_suche(tagestemperaturen, 25))
    print("Index von 99:", lineare_suche(tagestemperaturen, 99))

    print("\n--- Lineare Suche im Bereich 18-22 ---")
    print("Indizes:", lineare_suche_bereich(tagestemperaturen, 18, 22))

    print("\n=== 2D-Liste: Wochendaten ===")
    for i in range(len(wochen)):
        print(f"Woche {i}: {wochen[i]}")

    print("\n--- Wochendurchschnitte ---")
    for i in range(len(wochen)):
        print(f"Woche {i}: {berechne_wochendurchschnitt(wochen, i):.2f}°C")

    print("\n--- Beste Woche ---")
    beste = finde_beste_woche(wochen)
    print(f"Woche {beste} hat den höchsten Durchschnitt "
          f"({berechne_wochendurchschnitt(wochen, beste):.2f}°C)")

    print("\n--- Lineare Suche in 2D-Liste ---")
    position = lineare_suche_2d(wochen, 24)
    print(f"Wert 24 gefunden bei: {position}")  # (Woche, Tag)

    position2 = lineare_suche_2d(wochen, 99)
    print(f"Wert 99 gefunden bei: {position2}")  # None
