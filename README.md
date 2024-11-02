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
   python description_generator.py```

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
