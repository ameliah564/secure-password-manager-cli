# Secure Password Manager – Python CLI
This is a simple command-line tool for securely storing and managing login credentials (URL, username, and password) using a PostgreSQL database. It lets users add, update, delete, and list saved records via an intuitive CLI interface, and includes a built-in password generator.

This project was created as a personal learning exercise to improve my understanding of security practices, Python scripting, database integration, and clean project structure.

## Built With:
Python – Core language for scripting and logic
argparse – CLI command parsing
PostgreSQL – Backend database for storing credential records
psycopg2 – Python PostgreSQL adapter
random / string – Password generation
Modular Python architecture – Separation of logic, CLI, and database layers

## Features
✔ Add new credentials to the database
✔ Update existing records
✔ Delete credentials
✔ List stored services
✔ Generate random, strong passwords
✔ Input validation to prevent bad entries
✔ Parameterized SQL queries to reduce injection risk

## Project Structure
secure-password-manager-cli/
├── main.py                # Entry point & CLI logic
├── python_functions.py    # Core application logic
├── connect.py             # PostgreSQL connection
├── create_tables.py       # Database setup
├── requirements.txt       # Dependencies
├── .gitignore             # Ignored files

## Usage
Before running, make sure you have:
- Python installed
- A running PostgreSQL instance
- A configured database for storing credentials
- Run the app
    - python main.py -insert example.com user123 mySecurePass
    - python main.py -update example.com user123 newPass
    - python main.py -delete example.com
    - python main.py -list

All operations are managed through command-line flags and arguments.

## Example
Add a new credential
python main.py -insert twitter.com alice myStr0ngP@ss

List all credentials
python main.py -list

Delete a credential
python main.py -delete twitter.com

## What I Learned
This project helped me:
- Understand how to structure Python applications
- Work with PostgreSQL from Python using psycopg2
- Design CLI tools that feel intuitive
- Generate strong, randomized passwords
- Think about security risks like SQL injection

## Future Improvements
This project could be expanded with:
- Secure encryption of stored passwords (e.g., using Fernet or AWS KMS)
- A master-password login system
- A web interface

## Contributions
This is a personal project.
