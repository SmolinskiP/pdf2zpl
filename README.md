
# Zebra Label Printer Script

This script converts a PDF file to ZPL (Zebra Programming Language) format and sends it to a Zebra label printer. It includes functionality to:

- Convert PDF to an image
- Resize the image to fit label dimensions
- Convert the image to ZPL format
- Send the ZPL code via Ethernet or serial port
- Save the ZPL code to a file

## Requirements

- Python 3.x
- Install required libraries using:
  ```bash
  pip install pdf2image pillow pyserial
  ```
- Poppler for Windows (add to `PATH` or specify `poppler_path`)

## Usage

1. **Convert PDF and Save ZPL to File**:
   ```python
   save_zpl_to_file(zpl_command, 'my_label.zpl')
   ```

2. **Send ZPL to Printer via Ethernet**:
   ```python
   send_zpl_over_ethernet(zpl_command, '192.168.0.1')
   ```

3. **Send ZPL to Printer via Serial Port**:
   ```python
   send_zpl_over_serial(zpl_command, 'COM3')
   ```

## Label Dimensions

- Default label width: 10.16 cm (4 inches)
- Default label height: 15.24 cm (6 inches)
- DPI: 300

You can adjust these dimensions by modifying the `label_width_cm`, `label_height_cm`, and `dpi` values in the script.

## Notes

- Ensure the printer's IP address and serial port configuration are correct before sending data.
- The script processes only the first page of the PDF.

## Example

Convert and send a PDF label via Ethernet:
```python
send_zpl_over_ethernet(zpl_command, '192.168.0.1')
```
