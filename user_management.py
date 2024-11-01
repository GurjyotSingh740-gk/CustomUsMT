import subprocess
import sys

def add_user(username, password):
    """Add a new user to the system."""
    subprocess.run(['sudo', 'useradd', username])
    subprocess.run(['sudo', 'chpasswd'], input=f'{username}:{password}'.encode())
    print(f"User '{username}' added successfully.")

def delete_user(username):
    """Delete a user from the system."""
    subprocess.run(['sudo', 'userdel', username])
    print(f"User '{username}' deleted successfully.")

def add_group(groupname):
    """Create a new group."""
    subprocess.run(['sudo', 'groupadd', groupname])
    print(f"Group '{groupname}' created successfully.")

def delete_group(groupname):
    """Delete a group from the system."""
    subprocess.run(['sudo', 'groupdel', groupname])
    print(f"Group '{groupname}' deleted successfully.")

def add_user_to_group(username, groupname):
    """Add a user to a specified group."""
    subprocess.run(['sudo', 'usermod', '-aG', groupname, username])
    print(f"User '{username}' added to group '{groupname}'.")

def set_permissions(filepath, permissions, owner, group):
    """Set file permissions and ownership."""
    subprocess.run(['sudo', 'chmod', permissions, filepath])
    subprocess.run(['sudo', 'chown', f"{owner}:{group}", filepath])
    print(f"Permissions for '{filepath}' updated successfully.")

def set_acl(filepath, username, permissions):
    """Set ACL for a specified user on a file or directory."""
    subprocess.run(['sudo', 'setfacl', '-m', f'u:{username}:{permissions}', filepath])
    print(f"ACL for user '{username}' on '{filepath}' set to '{permissions}'.")

def view_acl(filepath):
    """View ACL for a specified file or directory."""
    result = subprocess.run(['getfacl', filepath], capture_output=True, text=True)
    print(f"ACL for '{filepath}':\n{result.stdout}")

def print_options():
    """Print available options for the user."""
    print("Options:")
    print("1. Add User")
    print("2. Delete User")
    print("3. Add Group")
    print("4. Delete Group")
    print("5. Add User to Group")
    print("6. Set Permissions")
    print("7. Set ACL")
    print("8. View ACL")
    print("9. Exit")

def main():
    print("Welcome to the User Management Tool!")
    print_options()

    while True:
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            print("This option allows you to add a new user to the system.")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_user(username, password)
        elif choice == '2':
            print("This option allows you to delete an existing user from the system.")
            username = input("Enter username to delete: ")
            delete_user(username)
        elif choice == '3':
            print("This option allows you to create a new group in the system.")
            groupname = input("Enter group name: ")
            add_group(groupname)
        elif choice == '4':
            print("This option allows you to delete an existing group from the system.")
            groupname = input("Enter group name to delete: ")
            delete_group(groupname)
        elif choice == '5':
            print("This option allows you to add an existing user to a specified group.")
            username = input("Enter username: ")
            groupname = input("Enter group name: ")
            add_user_to_group(username, groupname)
        elif choice == '6':
            print("This option allows you to set permissions for a specified file.")
            filepath = input("Enter file path: ")
            print("Permissions are specified using three digits:")
            print("User: 7=rwx, 6=rw-, 5=r--, 4=r--, 3=rw-, 2=w-, 1=x, 0=---")
            permissions = input("Enter permissions (e.g., 755): ")
            owner = input("Enter owner (username): ")
            group = input("Enter group (groupname): ")
            set_permissions(filepath, permissions, owner, group)
        elif choice == '7':
            print("This option allows you to set Access Control List (ACL) for a specified user.")
            filepath = input("Enter file path for ACL: ")
            username = input("Enter username to set ACL: ")
            permissions = input("Enter ACL permissions (e.g., rwx): ")
            set_acl(filepath, username, permissions)
        elif choice == '8':
            print("This option allows you to view the Access Control List (ACL) for a specified file.")
            filepath = input("Enter file path to view ACL: ")
            view_acl(filepath)
        elif choice == '9':
            print("Exiting the tool.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

        print_options()

if __name__ == "__main__":
    main()
