from pdf2image import convert_from_path
from PIL import Image
import math
import serial

# Provide the PDF path and Poppler location
images = convert_from_path('et.pdf', poppler_path=r"C:\poppler-24.08.0\Library\bin")

# Specify label dimensions in centimeters
label_width_cm = 10.16   # e.g., 10.16 cm (4 inches)
label_height_cm = 15.24  # e.g., 15.24 cm (6 inches)
dpi = 300

#____________________________________________
# Below this line, it's better not to modify anything except the last command sending the instruction to the printer!
#____________________________________________

label_width_inch = label_width_cm / 2.54
label_height_inch = label_height_cm / 2.54
image = images[0]

label_width_px = int(label_width_inch * dpi)
label_height_px = int(label_height_inch * dpi)
image = image.resize((label_width_px, label_height_px))
image = image.convert('1')

width, height = image.size
if width % 8 != 0:
    new_width = (width + 7) // 8 * 8
    image = image.resize((new_width, height))
    width = new_width

pixels = image.load()

def image_to_zpl(image):
    width, height = image.size
    data = ''
    for y in range(height):
        row = ''
        for x in range(0, width, 8):
            byte = 0
            for bit in range(8):
                if x + bit < width:
                    pixel = pixels[x + bit, y]
                    if pixel == 0:
                        byte |= 1 << (7 - bit)
                else:
                    byte |= 1 << (7 - bit)
            row += '{:02X}'.format(byte)
        data += row + '\n'
    return data

zpl_data = image_to_zpl(image)

bytes_per_row = width // 8
total_bytes = bytes_per_row * height
zpl_command = f"^XA\n^FO0,0\n^GFA,{total_bytes},{total_bytes},{bytes_per_row},\n{zpl_data}^FS\n^XZ"


with open('etykieta.zpl', 'w') as f:
    f.write(zpl_command)

def send_zpl_over_ethernet(zpl_command, printer_ip, port=9100):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((printer_ip, port))
        sock.sendall(zpl_command.encode('utf-8'))

    except Exception as e:
        print(f"Błąd podczas wysyłania danych: {e}")

    finally:
        sock.close()

def save_zpl_to_file(zpl_command, filename='etykieta.zpl'):
    with open(filename, 'w') as f:
        f.write(zpl_command)

def send_zpl_over_serial(zpl_command, serial_port, baudrate=9600):
    try:
        # Otwarcie portu szeregowego
        with serial.Serial(port=serial_port, baudrate=baudrate, timeout=1) as ser:
            # Konwertuj kod ZPL na bajty i wyślij do drukarki
            ser.write(zpl_command.encode('utf-8'))

    except Exception as e:
        print(f"Błąd podczas wysyłania danych: {e}")

#-----------------------------------------------------------------
"""
Sends ZPL code to a Zebra printer via Ethernet.

:param zpl_command: ZPL code to send (string).
:param printer_ip: Printer IP address (string).
:param port: Printer TCP port (default 9100).

EXAMPLE USAGE:
send_zpl_over_ethernet(zpl_command, "192.168.0.1")
"""
#-----------------------------------------------------------------
"""
Sends ZPL code to a Zebra printer via a serial port.

:param zpl_command: ZPL code to send (string).
:param serial_port: Name of the serial port (e.g., 'COM1' on Windows or '/dev/ttyUSB0' on Linux).
:param baudrate: Transmission speed (default 9600).

EXAMPLE USAGE:
send_zpl_over_serial(zpl_command, "COM3")
"""
#-----------------------------------------------------------------
"""
Saves ZPL code to a file.

:param zpl_command: ZPL code to save (string).
:param filename: File name to save to (default 'etykieta.zpl').

EXAMPLE USAGE:
save_zpl_to_file(zpl_command, r'X:\\Path\\to\\file\\my_label.zpl')
"""
#-----------------------------------------------------------------

save_zpl_to_file(zpl_command, r'moja_etykieta.zpl')
