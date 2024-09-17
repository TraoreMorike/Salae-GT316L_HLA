# HighLevelAnalyzer

This repository contains a High-Level Analyzer (HLA) extension for Saleae Logic Analyzers. The HLA decodes transactions for the GT316L device, providing detailed insights into the communication between the device and its controller.

## Features

- Decodes I2C transactions for the GT316L device.
- Provides detailed information about the registers and their active bits.
- Supports various GT316L registers and their specific bitmaps.

## Installation

1. Clone this repository.
2. Follow the instructions on the [Saleae support page](https://support.saleae.com/extensions/high-level-analyzer-extensions) to install the HLA extension.

## Usage

1. Open Saleae Logic software.
2. Load the HLA extension.
3. Start capturing I2C transactions.
4. The decoded transactions will be displayed in the Saleae Logic software.

## Code Overview

### Main Components

- **HighLevelAnalyzer.py**: The main file containing the logic for decoding transactions.
- **GT316L_register_map**: A dictionary mapping register addresses to their names.
- **GT316L_register_bitmap**: A dictionary mapping register addresses to their bit descriptions.
- **decodeRegister**: A function to decode the active bits for a given register.
- **decodeBits**: A function to determine the active bits in a register.
- **Transaction**: A class representing an I2C transaction.
- **Hla**: The main class inheriting from [`HighLevelAnalyzer`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fmo.traore%2FDesktop%2FPENTEST%2FReverse_Engineering_SecureLock%2FGT316L_v3%2FHighLevelAnalyzer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A29%7D%7D%5D%2C%229b4a9926-9577-43cb-8daa-6f89af355d67%22%5D "Go to definition"), responsible for decoding frames.

### Example Code

```python
def decode_transaction(self, transaction):
    data_to_decode = bytearray()
    if len(transaction.data) > 1 and transaction.address == 0x59:
        reg_ptr = transaction.register_ptr
        data_to_decode = transaction.data[1:]
        for data in data_to_decode:
            decodeRegister(reg_ptr, decodeBits(reg_ptr, data, GT316L_register_bitmap))
            reg_ptr += 1
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

For more information and documentation, please visit the [Saleae support page](https://support.saleae.com/extensions/high-level-analyzer-extensions).

---

This README provides an overview of the High-Level Analyzer extension, its features, installation instructions, and a brief code overview. For detailed usage and contribution guidelines, please refer to the respective sections.