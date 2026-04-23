from auth import verify_master_password
from storage import add_password, get_password, delete_password
from utils import generate_password

def menu():
    print("\n==== Password Manager ====")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Delete Password")
    print("4. Generate Strong Password")
    print("5. Exit")

def main():
    if not verify_master_password():
        print("❌ Wrong Master Password")
        return

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            site = input("Enter site: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(site, username, password)
            print("✅ Password saved!")

        elif choice == "2":
            site = input("Enter site: ")
            username, password = get_password(site)
            if username:
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("❌ Not found")

        elif choice == "3":
            site = input("Enter site: ")
            if delete_password(site):
                print("🗑 Deleted")
            else:
                print("❌ Not found")

        elif choice == "4":
            length = int(input("Enter length: "))
            print("Generated Password:", generate_password(length))

        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()