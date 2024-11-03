# Product Description Generator

This project provides a custom Python-based solution for generating detailed product descriptions for a vehicle conversion company's website. The script automates the collection of technical specifications, optional features, and customizable options for each vehicle, and saves the generated descriptions to a text file.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Example Output](#example-output)

## Overview

The Product Description Generator is designed for businesses needing to quickly create accurate and comprehensive descriptions of various products. The script collects information directly from the user and produces a formatted description file, with options for customization.

## Features

- **User Input for Specifications:** Allows user inputs for vehicle attributes like weight, power, and size.
- **Customizable Options Parsing:** Reads options from an `options.txt` file, with options to add, modify, or skip each option.
- **Configurable File Generation:** Automatically generates a unique description file for each vehicle.
- **Customizable Template Parsing:** Uses `custom_options.txt` to create sections where specific details can be entered for additional personalization.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/username/repo-name.git 
   ```

2. **Navigate into the directory:**
   ```
   cd repo-name
   ```

3. **Ensure Python 3 is installed on your system.**

## Usage

1. **Prepare Input Files:**
   - Create an `options.txt` file with each line representing an option (e.g., "Sunroof").
   - Create a `custom_options.txt` file with sections separated by `$` for custom entries.

2. **Run the Script:**
   Execute the following command:
   ```
   python description_generator.py
   ```

3. **Follow the Prompts:**
   Enter vehicle specifications and select options as prompted.

## File Structure

The main files in this project are:
- `description_generator.py`: The primary script file for generating product descriptions.
- `options.txt`: Contains default vehicle options, one per line.
- `custom_options.txt`: Specifies customizable sections for product descriptions.

## Example Output

After running the script and inputting the required data, a sample output file may look like this:

```
✅ Mercedes Sprinter 517 CDI, 5500 KG, 140 KW, 7367 mm
✅ Anvelope 205/75/R16 C
✅ Rezervor principal 93 litri
✅ Cutie de viteze manuală ECO Gear pe 6 trepte
```

## Contributing

Contributions are welcome! Please submit a pull request if you’d like to add features or improvements.

## License

This project is licensed under the MIT License.


# 

### Roumanian Translation Below

# Generator Descriere Produs

Acest proiect oferă o soluție personalizată în Python pentru generarea de descrieri detaliate ale produselor pentru site-ul unei companii de conversii de vehicule. Scriptul automatizează colectarea specificațiilor tehnice, opțiunilor și alegerilor personalizabile pentru fiecare vehicul, și salvează descrierile generate într-un fișier text.

## Cuprins
- [Prezentare Generală](#prezentare-generală)
- [Funcționalități](#funcționalități)
- [Instalare](#instalare)
- [Utilizare](#utilizare)
- [Structura Fișierelor](#structura-fișierelor)
- [Exemplu de Output](#exemplu-de-output)

## Prezentare Generală

Generatorul de Descrieri Produs este conceput pentru afacerile care au nevoie să creeze rapid descrieri precise și cuprinzătoare ale diferitelor produse. Scriptul colectează informațiile direct de la utilizator și produce un fișier de descriere formatat, cu opțiuni de personalizare.

## Funcționalități

- **Introducere de Date pentru Specificații:** Permite introducerea atributelor vehiculului, precum greutate, putere și dimensiune.
- **Parcurgerea Opțiunilor Personalizabile:** Citește opțiunile dintr-un fișier `options.txt`, cu opțiuni de adăugare, modificare sau omiterea fiecărei opțiuni.
- **Generarea Fișierului Configurabil:** Generează automat un fișier de descriere unic pentru fiecare vehicul.
- **Parcurgerea Șablonului Personalizabil:** Utilizează `custom_options.txt` pentru a crea secțiuni în care pot fi introduse detalii specifice pentru o personalizare suplimentară.

## Instalare

1. **Clonați acest repository:**
   ```
   git clone https://github.com/username/repo-name.git 
   ```

2. **Navigați în directorul proiectului:**
   ```
   cd repo-name
   ```

3. **Asigurați-vă că Python 3 este instalat pe sistemul dumneavoastră.**

## Utilizare

1. **Pregătiți Fișierele de Intrare:**
   - Creați un fișier `options.txt` cu fiecare linie reprezentând o opțiune (de ex., "Trapa").
   - Creați un fișier `custom_options.txt` cu secțiuni separate prin `$` pentru intrări personalizate.

2. **Rulați Scriptul:**
   Executați următoarea comandă:
   ```
   python description_generator.py
   ```

3. **Urmăriți Instrucțiunile:**
   Introduceți specificațiile vehiculului și selectați opțiunile conform solicitărilor.

## Structura Fișierelor

Principalele fișiere din acest proiect sunt:
- `description_generator.py`: Fișierul script principal pentru generarea descrierilor produselor.
- `options.txt`: Conține opțiunile de bază ale vehiculului, câte una pe linie.
- `custom_options.txt`: Specifică secțiuni personalizabile pentru descrierile produselor.

## Exemplu de Output

După rularea scriptului și introducerea datelor necesare, un fișier de ieșire exemplu poate arăta astfel:

```
✅ Mercedes Sprinter 517 CDI, 5500 KG, 140 KW, 7367 mm
✅ Anvelope 205/75/R16 C
✅ Rezervor principal 93 litri
✅ Cutie de viteze manuală ECO Gear pe 6 trepte
```

## Contribuții

Contribuțiile sunt binevenite! Vă rugăm să trimiteți un pull request dacă doriți să adăugați funcționalități sau îmbunătățiri.

## Licență

Acest proiect este licențiat sub Licența MIT.