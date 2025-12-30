import sys

# ==============================================================================
# 🧬 UNIVERSAL LAB CONVERTER PRO (BIDIRECTIONAL EDITION)
# Author: Mateusz Jakubowski
# Co-pilot: Google Gemini (AI Assisted Development)
# Status: Learning Project / Educational Purpose
# ==============================================================================

# ℹ️ BAZA DANYCH: Skonsolidowana (Tietz Clinical Guide / SI Standards / Protokoly PL)
lab_database = {
    "01. BIOCHEMIA KLINICZNA (SUROWICA/OSOCZE)": {
        "Albumina":            {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "g/L"},
        "Alfa-amylaza":        {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "ALP (Fosfataza zas.)":{"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "ALT (Aminotransferaza)":{"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "AST (Aminotransferaza)":{"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Amoniak":             {"factor": 0.587,  "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "Białko Całkowite":    {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "g/L"},
        "Bilirubina Całkowita": {"factor": 17.1,  "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "Bilirubina (Wolna/Związana)": {"factor": 17.1, "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "Cholesterol Całkowity": {"factor": 0.0259, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Cholesterol HDL/LDL": {"factor": 0.0259, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Chlorki":             {"factor": 1.0,    "unit_in": "mEq/L", "unit_out": "mmol/L"},
        "CK (Kinaza kreatynowa)": {"factor": 1.0, "unit_in": "U/L",   "unit_out": "U/L"},
        "CRP / CRP hs":        {"factor": 10.0,   "unit_in": "mg/dL", "unit_out": "mg/L"},
        "Cynk":                {"factor": 0.153,  "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "Fosfor nieorganiczny": {"factor": 0.323, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "GGTP":                {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Glukoza":             {"factor": 0.0555, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Homocysteina":        {"factor": 1.0,    "unit_in": "µmol/L", "unit_out": "µmol/L"},
        "Kreatynina":          {"factor": 88.4,   "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "Kwas moczowy":        {"factor": 59.48,  "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "Kwas mlekowy (Lactate)":{"factor": 0.111,  "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "LDH":                 {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Lipaza":              {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Magnez":              {"factor": 0.411,  "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Miedź":               {"factor": 0.157,  "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "Mocznik (Urea)":      {"factor": 0.166,  "unit_in": "mg/dL", "unit_out": "mmol/L (Jako Mocznik)"},
        "BUN (Azot Mocznika)": {"factor": 0.357,  "unit_in": "mg/dL", "unit_out": "mmol/L (Jako Mocznik)"},
        "Potas":               {"factor": 1.0,    "unit_in": "mEq/L", "unit_out": "mmol/L"},
        "Sód":                 {"factor": 1.0,    "unit_in": "mEq/L", "unit_out": "mmol/L"},
        "Triglicerydy":        {"factor": 0.0113, "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Wapń Całkowity":      {"factor": 0.25,   "unit_in": "mg/dL", "unit_out": "mmol/L"},
        "Żelazo":              {"factor": 0.179,  "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "TIBC / UIBC":         {"factor": 0.179,  "unit_in": "µg/dL", "unit_out": "µmol/L"}
    },
    "02. ENDOKRYNOLOGIA (HORMONY TARCZYCY I PŁCIOWE)": {
        "ACTH":                {"factor": 0.22,   "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "Aldosteron":          {"factor": 27.7,   "unit_in": "ng/dL", "unit_out": "pmol/L"},
        "AMH (Anty-Mullerian)": {"factor": 7.14,  "unit_in": "ng/mL", "unit_out": "pmol/L"},
        "Androstendion":       {"factor": 0.0349, "unit_in": "ng/dL", "unit_out": "nmol/L"},
        "Beta-HCG (Total)":    {"factor": 1.0,    "unit_in": "mIU/mL", "unit_out": "IU/L"},
        "C-peptyd":            {"factor": 0.331,  "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "DHEA-SO4":            {"factor": 0.027,  "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "DHEA (Niezwiązany)":  {"factor": 3.47,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Estradiol (E2)":      {"factor": 3.67,   "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "Estriol Wolny (uE3)": {"factor": 3.47,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "FSH":                 {"factor": 1.0,    "unit_in": "mIU/mL", "unit_out": "IU/L"},
        "FT3 (Wolne T3)":      {"factor": 1.54,   "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "FT4 (Wolne T4)":      {"factor": 12.87,  "unit_in": "ng/dL", "unit_out": "pmol/L"},
        "Hormon Wzrostu (hGH)": {"factor": 1.0,   "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Insulina":            {"factor": 6.945,  "unit_in": "µIU/mL", "unit_out": "pmol/L"},
        "IGF-1 (Somatomedyna C)":{"factor": 0.13,  "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Kortyzol":            {"factor": 27.59,  "unit_in": "µg/dL", "unit_out": "nmol/L"},
        "LH":                  {"factor": 1.0,    "unit_in": "mIU/mL", "unit_out": "IU/L"},
        "Parathormon (PTH)":   {"factor": 1.0,    "unit_in": "pg/mL", "unit_out": "ng/L"},
        "Progesteron":         {"factor": 3.18,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Prolaktyna":          {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Renina":              {"factor": 1.0,    "unit_in": "µIU/mL", "unit_out": "mIU/L"},
        "SHBG":                {"factor": 1.0,    "unit_in": "nmol/L", "unit_out": "nmol/L"},
        "Testosteron Całk.":   {"factor": 0.0347, "unit_in": "ng/dL", "unit_out": "nmol/L"},
        "Testosteron Wolny":   {"factor": 3.47,   "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "TSH":                 {"factor": 1.0,    "unit_in": "µIU/mL", "unit_out": "mIU/L"},
        "17-OH Progesteron":   {"factor": 3.03,   "unit_in": "ng/mL", "unit_out": "nmol/L"}
    },
    "03. MARKERY NOWOTWOROWE (ONKOLOGIA)": {
        "AFP":                 {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "CA 125":              {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"},
        "CA 15-3":             {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"},
        "CA 19-9":             {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"},
        "CA 72-4":             {"factor": 1.0,    "unit_in": "U/mL",  "unit_out": "kU/L"},
        "CEA":                 {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Chromogranina A":     {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Cyfra 21-1":          {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "HE4":                 {"factor": 1.0,    "unit_in": "pmol/L", "unit_out": "pmol/L"},
        "Kalcytonina":         {"factor": 1.0,    "unit_in": "pg/mL", "unit_out": "ng/L"},
        "NSE":                 {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "PSA Całkowite":       {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "PSA Wolne":           {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "SCC-Ag":              {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Serotonina":          {"factor": 5.67,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "TPS / TPA":           {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "Tyreoglobulina (Tg)": {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"}
    },
    "04. WITAMINY I MIKROELEMENTY": {
        "Witamina A (Retinol)": {"factor": 0.0349, "unit_in": "µg/dL", "unit_out": "µmol/L"},
        "Witamina B1 (Tiamina)": {"factor": 29.6,  "unit_in": "µg/dL", "unit_out": "nmol/L"},
        "Witamina B6":         {"factor": 5.91,   "unit_in": "µg/L",  "unit_out": "nmol/L"},
        "Witamina B12":        {"factor": 0.738,  "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "Kwas Foliowy":        {"factor": 2.27,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Witamina D (25-OH)":  {"factor": 2.496,  "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Witamina E":          {"factor": 23.2,   "unit_in": "mg/dL", "unit_out": "µmol/L"},
        "Chrom":               {"factor": 19.23,  "unit_in": "µg/L",  "unit_out": "nmol/L"},
        "Nikiel":              {"factor": 17.04,  "unit_in": "µg/L",  "unit_out": "nmol/L"},
        "Selen":               {"factor": 0.0127, "unit_in": "µg/L",  "unit_out": "µmol/L"},
        "Ołów":                {"factor": 0.00483,"unit_in": "µg/dL", "unit_out": "µmol/L"}
    },
    "05. LEKI I TOKSYKOLOGIA (TDM)": {
        "Cyklosporyna A":      {"factor": 0.832,  "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Digoksyna":           {"factor": 1.28,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Etanol (Alkohol)":    {"factor": 0.217,  "unit_in": "mg/dL", "unit_out": "mmol/L (Uwaga: Promile = mg/dL/100)"},
        "Fenytoina":           {"factor": 3.96,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Karbamazepina":       {"factor": 4.23,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Kwas Walproinowy":    {"factor": 6.93,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Lamotrygina":         {"factor": 3.91,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Lewetyracetam":       {"factor": 5.88,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Lit":                 {"factor": 1.0,    "unit_in": "mmol/L", "unit_out": "mEq/L"},
        "Paracetamol":         {"factor": 6.61,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Salicylany":          {"factor": 0.0072, "unit_in": "mg/L",  "unit_out": "mmol/L"},
        "Sirolimus":           {"factor": 1.09,   "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Takrolimus":          {"factor": 1.244,  "unit_in": "ng/mL", "unit_out": "nmol/L"},
        "Teofilina":           {"factor": 5.55,   "unit_in": "µg/mL", "unit_out": "µmol/L"},
        "Wankomycyna":         {"factor": 0.69,   "unit_in": "µg/mL", "unit_out": "µmol/L"}
    },
    "06. BIAŁKA SPECYFICZNE I IMMUNOCHEMIA": {
        "Beta-2-mikroglobulina":{"factor": 84.7,  "unit_in": "mg/L",  "unit_out": "nmol/L"},
        "Ceruloplazmina":      {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "mg/L"},
        "Haptoglobina":        {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "mg/L"},
        "IgA / IgG / IgM":     {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "g/L"},
        "IgE Całkowite":       {"factor": 2.4,    "unit_in": "IU/mL", "unit_out": "µg/L (Masa)"},
        "Interleukina 6":      {"factor": 1.0,    "unit_in": "pg/mL", "unit_out": "ng/L"},
        "Prokalcytonina (PCT)": {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Prealbumina":         {"factor": 10.0,   "unit_in": "mg/dL", "unit_out": "mg/L"},
        "Transferyna":         {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "g/L"},
        "ASO":                 {"factor": 1.0,    "unit_in": "IU/mL", "unit_out": "kIU/L"},
        "RF (Czynnik Reum.)":  {"factor": 1.0,    "unit_in": "IU/mL", "unit_out": "kIU/L"}
    },
     "07. HEMATOLOGIA I KRZEPNIĘCIE": {
        "D-Dimery":            {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L (FEU)"},
        "Fibrynogen":          {"factor": 0.01,   "unit_in": "mg/dL", "unit_out": "g/L"},
        "Hemoglobina":         {"factor": 10.0,   "unit_in": "g/dL",  "unit_out": "g/L"},
        "Antytrombina":        {"factor": 1.0,    "unit_in": "%",     "unit_out": "%"},
        "Białko C / S":        {"factor": 1.0,    "unit_in": "%",     "unit_out": "%"}
    },
    "08. CUKRZYCA I METABOLIZM": {
        "HbA1c (Hemoglobina glikowana)": {"factor": 10.929, "unit_in": "% (NGSP) -> (Wzór IFCC)", "unit_out": "mmol/mol"},
        "Fruktozamina":        {"factor": 1.0,    "unit_in": "µmol/L", "unit_out": "µmol/L"},
        "Wolne Kwasy Tłuszczowe (WKT)": {"factor": 1.0, "unit_in": "mmol/L", "unit_out": "mmol/L"}
    },
    "09. KARDIOLOGIA": {
        "Troponina I (hs)":    {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Troponina T (hs)":    {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "CK-MB (Masa)":        {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "NT-proBNP":           {"factor": 0.118,  "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "BNP":                 {"factor": 0.289,  "unit_in": "pg/mL", "unit_out": "pmol/L"},
        "Mioglobina":          {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"}
    },
    "10. DIAGNOSTYKA MOCZU (ZBIÓRKA DOBOWA / DZM)": {
        "Wapń w DZM":          {"factor": 0.025,  "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Fosfor w DZM":        {"factor": 0.0323, "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Magnez w DZM":        {"factor": 0.0411, "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Kreatynina w DZM":    {"factor": 0.00884,"unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Mocznik w DZM":       {"factor": 0.0166, "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Kwas Moczowy w DZM":  {"factor": 0.0059, "unit_in": "mg/24h", "unit_out": "mmol/24h"},
        "Białko w DZM":        {"factor": 0.001,  "unit_in": "mg/24h", "unit_out": "g/24h"},
        "Kwas WMA (VMA)":      {"factor": 5.05,   "unit_in": "mg/24h", "unit_out": "µmol/24h"},
        "Kwas 5-HIAA":         {"factor": 5.23,   "unit_in": "mg/24h", "unit_out": "µmol/24h"},
        "Porfobilinogen":      {"factor": 4.42,   "unit_in": "mg/24h", "unit_out": "µmol/24h"},
        "Adrenalina (DZM)":    {"factor": 5.46,   "unit_in": "µg/24h", "unit_out": "nmol/24h"},
        "Noradrenalina (DZM)": {"factor": 5.91,   "unit_in": "µg/24h", "unit_out": "nmol/24h"},
        "Dopamina (DZM)":      {"factor": 6.53,   "unit_in": "µg/24h", "unit_out": "nmol/24h"},
        "Metoksykatecholaminy": {"factor": 1.0,   "unit_in": "µg/24h", "unit_out": "µg/24h (Różne MW)"}
    },
    "11. OSTEOPOROZA I KOŚCI": {
        "Osteokalcyna":        {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "Beta-CTx (CrossLaps)":{"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"},
        "P1NP":                {"factor": 1.0,    "unit_in": "ng/mL", "unit_out": "µg/L"}
    },
    "12. GASTROLOGIA I WĄTROBA (SPECIAL)": {
        "Kwasy Żółciowe (Całkowite)": {"factor": 1.0,    "unit_in": "µmol/L", "unit_out": "µmol/L"},
        "Gastryna":            {"factor": 1.0,    "unit_in": "pg/mL", "unit_out": "ng/L"},
        "Cholinoesteraza":     {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L (kU/L x 0.001)"},
        "Elastaza trzustkowa": {"factor": 1.0,    "unit_in": "µg/g",  "unit_out": "µg/g (Kał)"}
    },
    "13. DIAGNOSTYKA SPECJALISTYCZNA (RÓŻNE)": {
        "Cystatyna C":         {"factor": 10.0,   "unit_in": "mg/dL", "unit_out": "mg/L (Standard)"},
        "Kwas Metylomalonowy (MMA)": {"factor": 1.0, "unit_in": "nmol/L", "unit_out": "nmol/L"},
        "Aldolaza":            {"factor": 1.0,    "unit_in": "U/L",   "unit_out": "U/L"},
        "ACE (Enzym konwertujący)": {"factor": 1.0, "unit_in": "U/L", "unit_out": "U/L"},
        "Erytropoetyna (EPO)": {"factor": 1.0,    "unit_in": "mIU/mL", "unit_out": "IU/L"}
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
                # Skracamy nazwę kategorii dla czytelności (usuwa numer np. "01. ")
                kat_short = kat.split('.', 1)[-1].strip() if '.' in kat else kat
                print(f"{i}. {nazwa:<30} | {kat_short}")
            
            try:
                numer = input("\nWybierz numer (lub Enter by wrócić): ")
                if not numer: continue
                
                wybor = int(numer)
                if 1 <= wybor <= len(znalezione):
                    _, nazwa_badania, dane = znalezione[wybor - 1]
                    
                    print(f"\n🧪 {nazwa_badania}")
                    
                    # --- NOWOŚĆ: WYBÓR KIERUNKU ---
                    print("Wybierz kierunek konwersji:")
                    print(f" [1] {dane['unit_in']} ➡️ {dane['unit_out']} (Konwencjonalne -> SI)")
                    print(f" [2] {dane['unit_out']} ➡️ {dane['unit_in']} (SI -> Konwencjonalne)")
                    
                    kierunek = input("Opcja (1/2): ").strip()
                    
                    try:
                        if kierunek == '1':
                            # STANDARDOWE (MNOŻENIE)
                            wartosc = float(input(f"Podaj wynik w [{dane['unit_in']}]: "))
                            wynik = wartosc * dane['factor']
                            jednostka = dane['unit_out']
                        elif kierunek == '2':
                            # ODWROTNE (DZIELENIE)
                            wartosc = float(input(f"Podaj wynik w [{dane['unit_out']}]: "))
                            if dane['factor'] == 0:
                                print("❌ Błąd: Przelicznik wynosi 0.")
                                continue
                            wynik = wartosc / dane['factor']
                            jednostka = dane['unit_in']
                        else:
                            print("❌ Nieznana opcja.")
                            continue

                        print("-" * 40)
                        print(f"✅ WYNIK: {wynik:.4g} {jednostka}")
                        print("-" * 40)
                        
                        if "HbA1c" in nazwa_badania:
                            print("⚠️ Uwaga: HbA1c wymaga specjalnego wzoru, wynik jest szacunkowy.")
                            
                    except ValueError:
                        print("❌ Błąd: To nie jest liczba!")
                else:
                    print("❌ Nieprawidłowy numer.")
            except ValueError:
                print("❌ Błąd wyboru.")

if __name__ == "__main__":
    main()
