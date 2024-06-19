# Base Converter Tool

## Description
A Python-based GUI tool for converting numbers between different bases.

<p align="center">
  <img src="https://github.com/LukeWait/base-converter/raw/main/assets/screenshots/base-converter-preview.png" alt="App Screenshot" width="550">
</p>

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [License](#license)
- [Source Code](#source-code)
- [Dependencies](#dependencies)

## Installation
### Executable
#### Windows
1. Download the latest Windows release from the [releases page](https://github.com/LukeWait/base-converter/releases).
2. Extract the contents to a desired location.
3. Run the `BaseConverter.exe` file.

#### Linux
1. Download the latest Linux release from the [releases page](https://github.com/LukeWait/base-converter/releases).
2. Extract the contents to a desired location.
3. Make the BaseConverter file executable by running the following command in the terminal:
    ```sh
    chmod +x BaseConverter
    ```
4. Run the BaseConverter file by navigating to the directory in the terminal and executing:
    ```sh
    ./BaseConverter
    ```

### From Source
To install and run the application from source:

1. Clone the repository:
    ```sh
    git clone https://github.com/LukeWait/base-converter.git
    cd base-converter
    ```

2. (Optional) Create and activate a virtual environment:
    - **Windows**:
      ```sh
      python -m venv base_converter_venv
      base_converter_venv\Scripts\activate
      ```
    - **Linux**:
      ```sh
      python3 -m venv base_converter_venv
      source base_converter_venv/bin/activate
      ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    - **Windows**:
      ```sh
      python src\base_converter.py
      ```
    - **Linux**:
      ```sh
      python src/base_converter.py
      ```

## Usage
Use the input field to enter either an integer, binary, or hexadecimal number and choose the appropriate type from the combo box. Upon clicking convert, the number will be displayed as all three options in the labeled output areas.

You can enter multiple numbers by using a "." as a separator. For example, an IP address entered as an integer: `192.168.1.1`, will be displayed as binary: `11000000.10101000.1.1`, and hexadecimal: `C0.A8.1.1`.

## Development
### Using PyQt Designer
The `pyqt_gui.ui` file can be opened and edited with PyQt Designer. PyQt Designer is a tool for designing and building GUIs from Qt widgets graphically and is included in pyqt5-tools==5.15.9.3.3.

To open PyQt Designer from the cloned GitHub repository:
- **Windows**:
  Navigate to the `Scripts` folder of your virtual environment or Python installation and run `designer.exe`.
  ```sh
  base_converter_venv\Scripts\qt5-tools.exe designer
  ```

- **Linux**:  
  ```sh
  .base_converter_venv/lib/python3.11/site-packages/qt5_applications/Qt/bin/designer
  ```

### Converting `.ui` to `.py`
Project files in PyQt Designer are saved as `.ui`. To convert the `.ui` file to a `.py` file, use the following command:
```sh
pyuic5 -o src/pyqt_gui.py src/pyqt_gui.ui
```

### Building Executables with PyInstaller
To build executables for Windows, macOS, and Linux, you can use PyInstaller. I recommend using PyInstaller version 6.1.0 as it is stable and doesn't result in the executable being flagged as a virus like some newer versions. First, ensure you have PyInstaller installed:
```sh
pip install pyinstaller==6.1.0
```
Then, run the following command to create an executable:
```sh
pyinstaller --onefile --noconsole src/base_converter.py
```
This will generate the executable in the `dist` directory. It will also create a `build` directory and `.spec` file. These are used in the build process and can be safely removed.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Source Code
The source code for this project can be found in the GitHub repository: [https://github.com/LukeWait/base-converter](https://github.com/LukeWait/base-converter).

## Dependencies
For those building from source, the dependencies listed in `requirements.txt` are:
- PyQt5==5.15.9
- pyqt5-tools==5.15.9.3.3
