# X3-OSINT


## Overview

The **X3-OSINT** is a Python-based tool that allows you to quickly check the availability of a specific username across multiple social media platforms. The tool automates the process of visiting each platform, checking if the username exists, and then saving the results in an Excel file.

This tool is useful for:
- Social media management
- OSINT (Open Source Intelligence) tasks
- Personal use, for tracking or reserving usernames

### Features
- Supports 8 popular social media platforms:
  - Twitter
  - Instagram
  - GitHub
  - Facebook
  - LinkedIn
  - TikTok
  - Reddit
  - Twitch
- Saves results in an Excel file for future reference.
- Random User-Agent for better request handling.
- Easy to use with a simple menu-driven interface.

## Requirements

Before running the tool, ensure you have the following installed:

1. **Python 3.x** (Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/)).
   
2. Install the necessary Python libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can manually install the required libraries:
   ```bash
   pip install requests pandas
   ```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mubbashirulislam/X3-OSINT.git
   ```
   
2. **Navigate to the Project Directory:**
   ```bash
   cd social-X3-OSINT
   ```

3. **Install the Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

Once everything is set up, you can run the tool using the following steps:

1. **Run the Script:**
   ```bash
   python X3-OSINT.py
   ```

2. **Follow the Prompts:**
   - You will be greeted with a menu where you can:
     - Enter a username to search.
     - Exit the program.
   
   Example:
   ```
   ================================================================
   
   ██╗  ██╗██████╗        ██████╗ ███████╗██╗███╗   ██╗████████╗
   ╚██╗██╔╝╚════██╗      ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
    ╚███╔╝  █████╔╝█████╗██║   ██║███████╗██║██╔██╗ ██║   ██║   
    ██╔██╗  ╚═══██╗╚════╝██║   ██║╚════██║██║██║╚██╗██║   ██║   
   ██╔╝ ██╗██████╔╝      ╚██████╔╝███████║██║██║ ╚████║   ██║   
   ╚═╝  ╚═╝╚═════╝        ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                                
   Developed by X3NIDE
   Github: https://github.com/mubbashirulislam
   
   ================================================================
   
   Options:
   1. Search username
   2. Exit
   
   What do you want to do? (1 or 2): 
   ```

3. **Enter the Username:**
   - After selecting option `1`, you'll be prompted to enter the username you want to check.
   - The tool will then search for that username across all supported platforms and show you the active accounts.

4. **Saving Results:**
   - The tool will automatically save the results in an Excel file inside the `results` directory.
   - The filename will follow this format: `social_media_<username>_<timestamp>.xlsx`.

## Supported Platforms

The tool currently checks for usernames on the following platforms:
- **Twitter**
- **Instagram**
- **GitHub**
- **Facebook**
- **LinkedIn**
- **TikTok**
- **Reddit**
- **Twitch**

## Example Output

Here is an example of what you might see when running the tool:

```
Starting search for username: exampleuser
Checking Twitter... Not found
Checking Instagram... Found!
Checking GitHub... Found!
Checking Facebook... Not found
...
Found accounts:
Instagram: https://instagram.com/exampleuser
GitHub: https://github.com/exampleuser
Results saved to results/social_media_exampleuser_20241018_1450.xlsx
```

## Future Enhancements

- Support for additional platforms.
- Improved error handling and retries.
- Adding proxy support for more anonymity.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author

Developed by **X3NIDE**  
GitHub: [mubbashirulislam](https://github.com/mubbashirulislam)
```
