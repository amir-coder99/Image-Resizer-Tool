import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"

# Ask user for mode
print("\n=== Image Resizer & Converter Tool ===")
print("1 - Resize & Convert")
print("2 - Resize Only")
print("3 - Convert Only (no resize)")

mode = input("Choose mode (1/2/3): ").strip()

# If resize is needed, ask for size
max_size = None
if mode in ("1", "2"):
    try:
        max_width = int(input("Enter new width (px): "))
        max_height = int(input("Enter new height (px): "))
        max_size = (max_width, max_height)
    except ValueError:
        print("❌ Invalid size entered.")
        exit()

# If conversion is needed, ask for output format
output_format = None
if mode in ("1", "3"):
    output_format = input("Enter output format (JPEG, PNG, etc.): ").upper() or "JPEG"

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        file_path = os.path.join(input_folder, filename)
        try:
            with Image.open(file_path) as img:
                img_copy = img.copy()

                # Resize if required (upscale + keep aspect ratio)
                if max_size:
                    orig_width, orig_height = img_copy.size
                    ratio = min(max_size[0] / orig_width, max_size[1] / orig_height)
                    new_size = (int(orig_width * ratio), int(orig_height * ratio))
                    img_copy = img_copy.resize(new_size, Image.LANCZOS)

                # Handle format conversion
                if output_format:
                    base_name = os.path.splitext(filename)[0]
                    save_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
                    img_copy.save(save_path, output_format)
                else:
                    save_path = os.path.join(output_folder, filename)
                    img_copy.save(save_path, img.format)

                print(f"✅ Processed: {save_path}")

        except Exception as e:
            print(f"❌ Failed: {filename} — {e}")

print("🎯 All images processed successfully!")