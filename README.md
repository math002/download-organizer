# File Organizer Script

## Overview

This Python script is a handy tool for organizing your downloads folder. It automatically categorizes files based on their extensions into separate directories. No more clutter – just a neatly organized space!

## How to Use

1. Clone the repository to your local machine.
2. Update the `user` variable with your OS username.
3. Run the script!

## Folder Structure

- **Inst**: Contains installer files (msi, exe).
- **Img**: Holds image files (jpg, png, gif).
- **Doc**: Stores document files (doc, docx, pdf, xls, xlsx).

## Usage Example

```bash
python organize.py
```

## Customization

Feel free to modify the `mydict` dictionary to include additional folders or extensions according to your preferences.

```python
mydict = {
    # ... your custom configurations here ...
}
```

## Contributing

If you have ideas for improvements or find any issues, feel free to open an [issue](https://github.com/math002/download-organizer/issues) or submit a [pull request](https://github.com/math002/download-organizer/pulls).