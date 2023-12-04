# E-Coupon-Clipping-GE
Automate the process of signing in and clipping all available e-coupons. 

Overview
This Python script automates the process of logging into the Giant Eagle website and clipping digital coupons. It is designed to navigate through the site, handle the login process, and automatically "clip" all available e-coupons, making the task of collecting coupons effortless and efficient.

How It Works
The script uses Selenium, a powerful tool for controlling web browsers through programs, to interact with the Giant Eagle website. It performs the following steps:

Navigates to the Giant Eagle coupon page.
Manages cookie consent pop-ups.
Provides user login functionality.
Scrolls through the coupons page to ensure all coupons are loaded.
Automatically clips each available coupon.
Security Concerns & Best Practices
When using or modifying this script, please consider the following security best practices:

Credentials Handling: The script prompts for user credentials (username and password) at runtime. It's crucial to run this script in a secure environment where input remains confidential. Avoid using the script in public or shared spaces where others can see your screen.

Environment Limitations: In certain environments, like QtConsole, the getpass function (used for secure password input) may not conceal password input. If you encounter such an issue, consider running the script in a standard command-line interface where password masking is supported.

Source Code Storage: If you store or share this script, ensure that no sensitive information (like your personal credentials) is included in the source code.

Website Terms of Service: Always use web scraping and automation scripts in compliance with the website's terms of service. Unauthorized or excessive use of automation can lead to account suspension or other penalties.

Script Execution: Be cautious about running scripts obtained from open sources. Always review the code and understand its functionality before executing it.

Usage
To run the script, ensure you have Python installed along with the necessary packages (selenium, webdriver_manager). Execute the script in a terminal or command prompt, and follow the on-screen instructions to log in and start the coupon clipping process.
