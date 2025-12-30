<div align="center">
  <img src="https://raw.githubusercontent.com/MatthewJakubowski/Universal-Lab-Converter/main/going_dark_cover.jpg" width="100%" alt="System Status: Going Dark. Deep Work Protocol.">
</div>

# 🧬 Universal Lab Converter PRO (v2.0)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI Assisted](https://img.shields.io/badge/AI_Co--Pilot-Google_Gemini-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=for-the-badge)

> **The Ultimate Laboratory Conversion Tool.**
> Bridging the gap between Medical Diagnostics and Software Engineering.

---

## 🤖 AI & Learning Transparency
**This project is a key milestone in my transition from Medical Analysis to IT (#FromPipetteToPython).**

While the **medical logic, validation, and domain knowledge** (15 years of experience) are mine, the **code architecture and Python syntax** were developed with the active assistance of **Google Gemini** (acting as my virtual Mentor & Architect).

* **My Goal:** To master Python Data Structures (Dictionaries, Loops) and Clean Code principles.
* **The Process:** I design the logic based on laboratory needs -> AI suggests the syntax -> I verify and implement.

---

## 🎯 About The Project
In medical diagnostics, shifting between **Conventional Units** (mg/dL, ng/mL) and **SI Units** (mmol/L, pmol/L) is a daily struggle. This tool automates the process using a massive database of conversion factors based on:

* **[span_0](start_span)Tietz Clinical Guide to Laboratory Tests**[span_0](end_span)
* **[span_1](start_span)SI Unit International Standards**[span_1](end_span)
* **Real-world Clinical Protocols** (Serum, Plasma, Urine, CSF).

### ⚡ Key Features (v2.0 Update)
* **🔄 Bidirectional Conversion:** Calculate from Conventional to SI **AND** from SI to Conventional (e.g., convert mmol/L back to mg/dL).
* **📚 Massive Database (150+ Parameters):** Covers Biochemistry, Hormones, Tumor Markers, TDM (Drugs), Toxicology, and Rare Diseases (e.g., *Gastrin, Serotonin*).
* **🔍 Smart Search Engine:** Just type "Gluc" or "TSH" to find the test instantly.
* **📂 Context Aware:** Different conversion factors for Urine (24h collection) vs Serum.
* **⚠️ Educational Warnings:** Highlights complex calculations (e.g., HbA1c formulas, Promille vs mg/dL).

---

## 🚀 How to Run
This tool is written in **Pure Python**. No external libraries (`pip install`) are required.

1.  **Clone the repository** (or download `main.py`):
    ```bash
    git clone [https://github.com/MatthewJakubowski/Universal-Lab-Converter.git](https://github.com/MatthewJakubowski/Universal-Lab-Converter.git)
    ```
2.  **Navigate to the folder:**
    ```bash
    cd Universal-Lab-Converter
    ```
3.  **Run the script:**
    ```bash
    python main.py
    ```

---

## 🧪 Example Usage

```text
[S] SEARCH (Enter name): Gluc

🔍 Found 1 matching results:
1. Glukoza   | BIOCHEMIA

> Select number: 1

🧪 Glukoza
Select direction:
 [1] mg/dL ➡️ mmol/L (Conventional -> SI)
 [2] mmol/L ➡️ mg/dL (SI -> Conventional)

> Option (1/2): 1
> Enter result in [mg/dL]: 95

----------------------------------------
✅ WYNIK SI: 5.27 mmol/L
----------------------------------------
````````````````````````````````````````
----------------------------------------

## 👨‍🔬 About the Author

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)

**Mateusz Jakubowski**
*Medical Analyst (15y exp) ➡️ Aspiring AI Engineer & Python Developer.*

I am building this project entirely on a mobile environment (**Samsung DeX** + **Pydroid 3**) to prove that you can engineer software anywhere.

* **Connect with me:** [LinkedIn](https://www.linkedin.com/in/mateuszjakubowski)
* **Follow my journey:** #FromPipetteToPython

---

### ⚠️ Medical Disclaimer

*This software is for educational and informational purposes only. While every effort has been made to ensure the accuracy of conversion factors (based on Tietz/SI standards), it should NOT be used for clinical decision-making without verification. Always rely on your validated Laboratory Information System (LIMS).*



