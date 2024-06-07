#password manager program
#command line interface
#postgresql backend 
#venv\Scripts\activate
#python connect.py

import sys, string, random, argparse
import python_functions

print("Password Manager\n'-insert URL uname pwd' to add a record,\n'-update URL uname pwd' to update and exisiting record\n'-delete URL' to delete an existing record\n'-list' to see all existing records. ")
print("")
parser = argparse.ArgumentParser(prog='Password Manager')

def generate_password():
    password_length = random.randint(20, 40)
    #define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    integers = string.digits
    special_characters = string.punctuation
    password = ''.join(random.choices(lowercase_letters + uppercase_letters + integers + special_characters, k=password_length))
    return password

# parse command-line arguments
parser.add_argument('-insert', dest='insert', nargs='+', help='Insert a new record')
parser.add_argument('-update', dest='update', nargs='+', help='Update a new record')
parser.add_argument('-delete', dest='delete', nargs=1, metavar=('URL'), help='Delete a new record')
parser.add_argument('-list', dest='list', action='store_true', help='List all records')

args = parser.parse_args()

if args.insert:
    if len(args.insert) == 2:
        password = generate_password()
        print("A random password has been generated.")
        python_functions.insert_record(args.insert[0], args.insert[1], password)
    elif len(args.insert) == 3:
        python_functions.insert_record(args.insert[0], args.insert[1], args.insert[2])
    else:
        print("Please only provide either 'URL username password' or 'URL username'")

elif args.update:
    if len(args.update) == 2:
        password = generate_password()
        print("A random password has been generated.")
        python_functions.update_record(args.update[0], args.update[1], password)
    elif len(args.update) == 3:
        python_functions.update_record(args.update[0], args.update[1], args.update[2])
    else:
        print("Please only provide either 'URL username password' or 'URL username'")
    
elif args.delete:
    python_functions.delete_record(args.delete)

elif args.list:
    python_functions.list_records()

elif len(sys.argv) != 4 and len(sys.argv) != 5:
    print("Please enter a URL, username and/or password only.")
    sys.exit(1)    

    
if args.insert or args.update:
    print(" \nYour details are:")
    url = sys.argv[2]
    python_functions.get_record(url)

