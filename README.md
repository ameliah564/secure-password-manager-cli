---

# SECURE PASSWORD MANAGER

### `secure-password-manager-cli/README.md`

```md
# Secure Password Manager – Python CLI

## Overview
A command-line password manager built to practice handling sensitive data, database integration, and modular Python development.

This project was created as a personal learning exercise following online resources and extended to better understand security and system structure.

## Features

- Store credentials by URL and username  
- Update existing records  
- Delete credentials  
- List stored services  
- Secure password generator (20–40 chars, mixed charset)  
- PostgreSQL backend  
- CLI interface using argparse

## Architecture

- **CLI Layer (main.py)**  
  Handles user commands and validation

- **Logic Layer (python_functions.py)**  
  Business rules and password generation

- **Data Layer (connect.py)**  
  PostgreSQL connection and queries

## Security Considerations

- Parameterized SQL queries to reduce injection risk  
- No credentials stored in source code  
- Input validation on all commands  
- Strong random password generation

## Usage

```bash
python main.py -insert example.com user password
python main.py -update example.com user newpass
python main.py -delete example.com
python main.py -list
