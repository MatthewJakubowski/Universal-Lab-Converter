import sys

# ==============================================================================
# 🧬 UNIVERSAL LAB CONVERTER PRO (ULTIMATE EDITION)
# Author: Mateusz Jakubowski
# Co-pilot: Google Gemini (AI Assisted Development)
# Status: Learning Project / Educational Purpose
# ==============================================================================

# Baza danych oparta na standardach: Tietz Clinical Guide / SI Standards / Protokoly Medyk & Diagnostyka
lab_database = {
    "01. BIOCHEMIA KLINICZNA (PODSTAWOWA)": {
        "Albumina":            {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "g/L"},
        "Alfa-amylaza":        {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "ALP (Fosfataza zas.)":{"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "ALT":                 {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "AST":                 {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Amoniak":             {"factor": 0.587,  "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "Białko Całkowite":    {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "g/L"},
        "Bilirubina Całkowita": {"factor": 17.1,  "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "Bilirubina (Wolna/Związana)": {"factor": 17.1, "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "Cholesterol Całkowity": {"factor": 0.0259, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Cholesterol HDL/LDL": {"factor": 0.0259, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "CK (Kinaza kreatynowa)": {"factor": 1.0, "unit_in": "U/L",   "unit_out": "U/L"},
        "CRP / CRP hs":        {"factor": 10.0,   "unit_in": "mg/dL", "unit_out": "mg/L"},
        "Cynk":                {"factor": 0.153,  "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "Fosfor nieorganiczny": {"factor": 0.323, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "GGTP":                {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Glukoza":             {"factor": 0.0555, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Kreatynina":          {"factor": 88.4,   "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "Kwas moczowy":        {"factor": 59.48,  "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "LDH":                 {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Lipaza":              {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Magnez":              {"factor": 0.411,  "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Mocznik":             {"factor": 0.166,  "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Potas":               {"factor": 1.0,    "unit_in": "mmol/L", "unit_out": "mEq/L"},
        "Sód":                 {"factor": 1.0,    "unit_in": "mmol/L", "unit_out": "mEq/L"},
        "Triglicerydy":        {"factor": 0.0113, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Wapń Całkowity":      {"factor": 0.25,   "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Żelazo":              {"factor": 0.179,  "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "TIBC / UIBC":         {"factor": 0.179,  "unit_in": "µg/dL", "unit_out": "µmol/L"}
    },
    "02. ENDOKRYNOLOGIA (HORMONY PODSTAWOWE)": {
        "ACTH":                {"factor": 0.22,   "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "Aldosteron":          {"factor": 27.7,   "unit_in": "ng/dL", "unit_out": "pmol/L"},
        "Beta-HCG":            {"factor": 1.0,    "unit_in": "mIU/mL", "unit_out": "IU/L"},
        "Kortyzol":            {"factor": 27.59,  "unit_in": "µg/dL", "unit_out": "nmol/L"},
        "Hormon Wzrostu (hGH)": {"factor": 1.0,   "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Insulina":            {"factor": 6.945,  "unit_in": "µIU/mL", "unit_out": "pmol/L"},
        "Parathormon (PTH)":   {"factor": 1.0,    "unit_in": "pg/mL", "unit_out": "ng/L"},
        "Prolaktyna":          {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "TSH":                 {"factor": 1.0,    "unit_in": "µIU/mL", "unit_out": "mIU/L"},
        "FT3 (Wolne T3)":      {"factor": 1.54,   "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "FT4 (Wolne T4)":      {"factor": 12.87,  "unit_in": "ng/dL", "unit_out": "pmol/L"}
    },
    "03. CUKRZYCA I METABOLIZM (ZAAWANSOWANE)": {
        "HbA1c (Hemoglobina glikowana)": {"factor": 10.929, "unit_in": "% (NGSP) -> uwaga: wzór!", "unit_out": "mmol/mol (IFCC) [Szac.]"},
        "C-Peptyd":            {"factor": 0.331,  "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Fruktozamina":        {"factor": 1.0,    "unit_in": "µmol/L", "unit_out": "µmol/L"},
        "Kwas Mlekowy (Lactate)":{"factor": 0.111,  "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Wolne Kwasy Tłuszczowe (WKT)": {"factor": 1.0, "unit_in": "mmol/L", "unit_out": "mmol/L"}
    },
    "04. KARDIOLOGIA I MARKERY SERCOWE": {
        "Troponina I (hs)":    {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Troponina T (hs)":    {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "CK-MB (Mass)":        {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "NT-proBNP":           {"factor": 0.118,  "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "BNP":                 {"factor": 0.289,  "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "Mioglobina":          {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Homocysteina":        {"factor": 1.0,    "unit_in": "µmol/L", "unit_out": "µmol/L (SI)"}
    },
    "05. HORMONY PŁCIOWE I PŁODNOŚĆ (ROZSZERZONE)": {
        "Estradiol (E2)":      {"factor": 3.671,  "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "Progesteron":         {"factor": 3.18,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Testosteron Całk.":   {"factor": 0.0347, "unit_in": "ng/dL", "unit_out": "nmol/L"},
        "Testosteron Wolny":   {"factor": 3.47,   "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "DHEA-SO4":            {"factor": 0.0027, "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "Androstendion":       {"factor": 0.0349, "unit_in": "ng/dL", "unit_out": "nmol/L"},
        "SHBG":                {"factor": 1.0,    "unit_in": "nmol/L", "unit_out": "nmol/L"},
        "17-OH Progesteron":   {"factor": 3.03,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "AMH (Rezerwa jajnikowa)": {"factor": 7.14, "unit_in": "ng/mL", "unit_out": "pmol/L"},
        "Inhibina B":          {"factor": 1.0,    "unit_in": "pg/mL", "unit_out": "ng/L"}
    },
    "06. WITAMINY I MIKROELEMENTY": {
        "Witamina B12":        {"factor": 0.738,  "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "Kwas Foliowy":        {"factor": 2.27,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Witamina D (25-OH)":  {"factor": 2.496,  "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Witamina A (Retinol)": {"factor": 0.0349, "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "Witamina B1 (Tiamina)": {"factor": 29.6,  "unit_in": "µg/dL", "unit_out": "nmol/L"},
        "Witamina B6":         {"factor": 5.91,   "unit_in": "µg/L",  "unit_out": "nmol/L"},
        "Witamina E":          {"factor": 23.2,   "unit_in": "mg/dL", "unit_out": "µmol/L"}
    },
    "07. MARKERY NOWOTWOROWE (PANEL ONKO)": {
        "PSA Całkowite":       {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "PSA Wolne (fPSA)":    {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "CEA":                 {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "AFP":                 {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "CA 125 (Jajnik)":     {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"},
        "CA 15-3 (Pierś)":     {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"},
        "CA 19-9 (Trzustka)":  {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"},
        "CA 72-4 (Żołądek)":   {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"},
        "Cyfra 21-1 (Płuca)":  {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "NSE (Neuronospecyficzna)": {"factor": 1.0, "unit_in": "ng/mL", "unit_out": "µg/L"},
        "SCC (Płaskonabłonkowy)":   {"factor": 1.0, "unit_in": "ng/mL", "unit_out": "µg/L"},
        "HE4 (Jajnik)":        {"factor": 1.0,    "unit_in": "pmol/L", "unit_out": "pmol/L"},
        "ROMA (Algorytm)":     {"factor": 1.0,    "unit_in": "%",     "unit_out": "%"}
    },
    "08. LEKI (TDM) I TOKSYKOLOGIA": {
        "Etanol (Alkohol)":    {"factor": 0.217,  "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Digoksyna":           {"factor": 1.28,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Karbamazepina":       {"factor": 4.23,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Kwas Walproinowy":    {"factor": 6.93,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Lit":                 {"factor": 1.0,    "unit_in": "mmol/L", "unit_out": "mEq/L"},
        "Paracetamol":         {"factor": 6.61,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Salicylany":          {"factor": 0.0072, "unit_in": "mg/L",  "unit_out": "mmol/L"},
        "Wankomycyna":         {"factor": 0.69,   "unit_in": "µg/mL", "unit_out": "µmol/L"}
    },
    "09. AUTOIMMUNOLOGIA I TARCZYCA": {
        "Anty-TPO":            {"factor": 1.0,    "unit_in": "IU/mL", "unit_out": "kIU/L"},
        "Anty-TG":             {"factor": 1.0,    "unit_in": "IU/mL", "unit_out": "kIU/L"},
        "TRAb (Receptor TSH)":{"factor": 1.0,    "unit_in": "IU/L",  "unit_out": "IU/L"},
        "Tyreoglobulina (Tg)": {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Anty-CCP":            {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"}
    },
    "10. INFEKCJE I STANY ZAPALNE": {
        "Prokalcytonina (PCT)": {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Interleukina 6 (IL-6)":{"factor": 1.0,    "unit_in": "pg/mL", "unit_out": "ng/L"},
        "ASO (Odczyn)":        {"factor": 1.0,    "unit_in": "IU/mL", "unit_out": "kIU/L"},
        "RF (Czynnik Reum.)":  {"factor": 1.0,    "unit_in": "IU/mL", "unit_out": "kIU/L"}
    },
    "11. DIAGNOSTYKA ANEMII (SPECIAL)": {
        "Erytropoetyna (EPO)": {"factor": 1.0,    "unit_in": "mIU/mL", "unit_out": "IU/L"},
        "Rozpuszczalny receptor transferyny (sTfR)": {"factor": 1.0, "unit_in": "mg/L", "unit_out": "mg/L"},
        "Ferrytyna":           {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"}
    },
    "12. HEMATOLOGIA I KRZEPNIĘCIE": {
        "Hemoglobina":         {"factor": 0.6206, "unit_in": "g/dL", "unit_out": "mmol/L (Fe)"},
        "Hemoglobina (SI)":    {"factor": 10.0,   "unit_in": "g/dL", "unit_out": "g/L"},
        "Fibrynogen":          {"factor": 0.01,   "unit_in": "mg/dL", "unit_out": "g/L"},
        "D-Dimery":            {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L (FEU)"}
    },
    "13. OSTEOPOROZA I KOŚCI": {
        "Osteokalcyna":        {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Beta-CTx (CrossLaps)":{"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "P1NP (Prokolagen)":   {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"}
    },
    "14. DIAGNOSTYKA MOCZU (ZBIÓRKA DOBOWA)": {
        "Wapń w DZM":          {"factor": 0.025,  "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Fosfor w DZM":        {"factor": 0.0323, "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Magnez w DZM":        {"factor": 0.0411, "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Kreatynina w DZM":    {"factor": 0.00884,"unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Mocznik w DZM":       {"factor": 0.0166, "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Kwas Moczowy w DZM":  {"factor": 0.0059, "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Białko w DZM":        {"factor": 0.001,  "unit_in": "mg/24h", "unit_out": "g/24h"}
    },
    "15. KATECHOLAMINY I NADCIŚNIENIE": {
        "Adrenalina":          {"factor": 5.46,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Noradrenalina":       {"factor": 5.91,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Dopamina":            {"factor": 6.53,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Kwas WMA (VMA)":      {"factor": 5.05,   "unit_in": "mg/24h", "unit_out": "µmol/24h"},
        "Metoksykatecholaminy": {"factor": 1.0,   "unit_in": "µg/24h", "unit_out": "µg/24h"},
        "Renina (Aktywność)":  {"factor": 1.0,    "unit_in": "ng/mL/h", "unit_out": "µg/L/h"}
    },
    "16. BIAŁKA SPECYFICZNE I INNE": {
        "Ceruloplazmina":      {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "mg/L"},
        "Haptoglobina":        {"factor": 0.1,    "unit_in": "mg/dL", "unit_out": "g/L"},
        "IgA / IgG / IgM":     {"factor": 0.01,   "unit_in": "mg/dL", "unit_out": "g/L"},
        "IgE Całkowite":       {"factor": 1.0,    "unit_in": "IU/mL", "unit_out": "kIU/L"},
        "Transferyna":         {"factor": 0.01,   "unit_in": "mg/dL", "unit_out": "g/L"}
    },
    "17. ALERGOLOGIA (DODATKI)": {
        "IgE Całkowite (Masa)": {"factor": 2.4,    "unit_in": "IU/mL", "unit_out": "ng/mL"},
        "ECP (Białko eozynofili)": {"factor": 1.0,"unit_in": "µg/L",  "unit_out": "µg/L"},
        "Tryptaza":            {"factor": 1.0,    "unit_in": "µg/L",  "unit_out": "µg/L"}
    }
}

# ==============================================================================
# 🧠 SILNIK WYSZUKIWANIA I INTERFEJS
# ==============================================================================

def print_header():
    print("\n" + "═" * 60)
    print("     🧬  UNIVERSAL LAB CONVERTER PRO (ULTIMATE)  🧬")
    print("        [Tietz Clinical Guide / SI Standards]")
    print(f"        Załadowano parametrów: {sum(len(v) for v in lab_database.values())}")
    print("═" * 60)

def znajdz_badanie(fraza):
    """Skanuje wszystkie kategorie w poszukiwaniu badania."""
    wyniki = []
    fraza = fraza.lower()
    for kategoria, badania in lab_database.items():
        for badanie, info in badania.items():
            if fraza in badanie.lower():
                wyniki.append((kategoria, badanie, info))
    return wyniki

def main():
    print_header()
    while True:
        print("\n[S] SZUKAJ (Wpisz nazwę, np. 'tsh', 'glukoza')")
        print("[L] LISTA KATEGORII")
        print("[X] WYJŚCIE")
        
        wybor_glowny = input("> ").strip().upper()
        
        if wybor_glowny == 'X':
            print("Going Dark. System Offline. 👋")
            break
        
        # Opcja listy kategorii
        elif wybor_glowny == 'L':
            print("\n📂 DOSTĘPNE MODUŁY:")
            for kat in lab_database.keys():
                print(f"• {kat}")
            continue
            
        # Logika wyszukiwania
        if wybor_glowny == 'S' or len(wybor_glowny) > 1:
            szukane = wybor_glowny if len(wybor_glowny) > 1 else input("Wpisz nazwę badania: ")
            
            znalezione = znajdz_badanie(szukane)
            
            if not znalezione:
                print("❌ Nie znaleziono badania w bazie.")
                continue
                
            print(f"\n🔍 Znaleziono {len(znalezione)} pasujących wyników:")
            for i, (kat, nazwa, info) in enumerate(znalezione, 1):
                # Skracamy nazwę kategorii dla czytelności
                kat_short = kat.split('.')[1].strip() if '.' in kat else kat
                print(f"{i}. {nazwa:<30} | {kat_short}")
            
            try:
                numer = input("\nWybierz numer (lub Enter by wrócić): ")
                if not numer: continue
                
                wybor = int(numer)
                if 1 <= wybor <= len(znalezione):
                    _, nazwa_badania, dane = znalezione[wybor - 1]
                    
                    print(f"\n🧪 {nazwa_badania}")
                    try:
                        wartosc = float(input(f"Podaj wynik w [{dane['unit_in']}]: "))
                        
                        # Przelicznik
                        wynik_si = wartosc * dane['factor']
                        
                        print("-" * 40)
                        # :.4g oznacza formatowanie "ogólne" (general) do 4 cyfr znaczących
                        print(f"✅ WYNIK SI: {wynik_si:.4g} {dane['unit_out']}")
                        print("-" * 40)
                        
                        # Ostrzeżenie dla HbA1c
                        if "HbA1c" in nazwa_badania:
                            print("⚠️ Uwaga: Przelicznik HbA1c jest szacunkowy.")
                            print("   Dokładny wzór: (HbA1c[%] - 2.15) * 10.929")
                            
                    except ValueError:
                        print("❌ Błąd: To nie jest liczba!")
                else:
                    print("❌ Nieprawidłowy numer.")
            except ValueError:
                print("❌ Błąd wyboru.")

if __name__ == "__main__":
    main()
