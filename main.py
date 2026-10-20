import argparse
import logging
import os
import sys
from datetime import datetime
import qrcode

os.makedirs("logs", exist_ok=True)
os.makedirs("qr_codes", exist_ok=True)

log_file = os.path.join("logs", "qr_generator.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

def main():
    logging.info("Welcome to the QR Code Generator application!")
    logging.info(f"Current Working Directory: {os.getcwd()}")

    parser = argparse.ArgumentParser(description="Generate a QR Code for a given URL.")
    parser.add_argument(
        "--url",
        type=str,
        default="http://github.com/kaw393939",
        help="Target URL for QR code generation"
    )
    args = parser.parse_args()
    target_url = args.url
    logging.info(f"Target URL received: {target_url}")

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(target_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        filename = f"qrcode_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        output_path = os.path.join("qr_codes", filename)
        img.save(output_path)

        logging.info(f"QR Code successfully generated and saved to: {output_path}")
        print(f"[SUCCESS] QR Code generated: {output_path}")
    except Exception as e:
        logging.error(f"Error during QR Code generation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
