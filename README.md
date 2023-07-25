# Int-Bin-Hex_Converter
Application to convert integer <-> binary <-> hexadecimal

Use the input field to enter either int, bin, or hex number and choose appropriate type from combo box.
Upon clicking convert, the number will be displayed as all three options in the labelled output areas.

User can enter multiple numbers by using a "." as a separator. For example, an IP address entered as an 
integer: 192.168.1.1, will be displayed as binary: 11000000.10101000.1.1, and hex: C0.A8.1.1

Installs:
pip install pyinstaller
pip install PyQt5
pip install PyQt5 pyqt5-tools

pyqt_gui.ui can be opened with PyQt5 designer.exe
pyqt_gui.py can be converted to .py using -> pyuic5 -o pyqt_gui.py pyqt_gui.ui
executable can be built for win/mac/unix with pyinstaller -> pyinstaller --onefile --noconsole int-bin-hex.py
