# Password_Manager
🔐 PassManager - Secure Password Management Tool

📌 Description
I developed PassManager as a Python-based tool to securely store and manage user credentials. This project focuses on protecting sensitive information by encrypting passwords before storing them. The goal is to ensure secure data handling and prevent unauthorized access using basic cybersecurity techniques.

🚀 Features
I can add and store passwords securely 🔒
I can retrieve saved credentials 👁️
Passwords are encrypted before storage
Prevents storing data in plain text
Simple CLI-based interface

🛠️ Technologies Used
Python
cryptography library (Fernet)
JSON (for data storage)
getpass (for hidden password input)

📂 Project Structure
PassManager/
│── passmanager.py # Main program
│── vault.json # Encrypted password storage
│── key.key # Encryption key

⚙️ Installation & Setup
Install Python from official website

Install required library
pip install cryptography

▶️ How to Run
python passmanager.py

🖥️ Usage
I run the program
I choose an option:
1 → Add Password
2 → View Password
3 → Exit
I enter site name, username, and password
The tool securely stores and retrieves data
