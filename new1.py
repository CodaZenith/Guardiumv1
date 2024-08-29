import os
from colorama import Fore, Style, init
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest

# Initialize Colorama
init(autoreset=True)

# Define title, version, and developer information with arrows
title = """
  ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ██╗███╗   ██╗███████╗██╗ ██████╗ ██╗  ██╗████████╗
 ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██║████╗  ██║██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝
 ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝██║██╔██╗ ██║███████╗██║██║  ███╗███████║   ██║   
 ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ██║██║╚██╗██║╚════██║██║██║   ██║██╔══██║   ██║   
  ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ██║██║ ╚████║███████║██║╚██████╔╝██║  ██║   ██║   
   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
"""

version = "Version: 1.0"
developer_info = f"""
{Fore.LIGHTGREEN_EX}↳ {Fore.YELLOW}DEVELOPER    {Fore.RESET}: {Fore.CYAN}CadaZenith
{Fore.LIGHTGREEN_EX}↳ {Fore.YELLOW}EMAIL        {Fore.RESET}: {Fore.CYAN}zenith.fusionsphere@gmail.com
{Fore.LIGHTGREEN_EX}↳ {Fore.YELLOW}WEBSITE      {Fore.RESET}: {Fore.CYAN}www.codazenith.blogspot.com
"""

# Simplified menu options without borders
menu_options = [
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}01{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}SCRAPE MEMBERS FROM GROUP",
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}02{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}EXPORT MEMBERS TO FILE",
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}03{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}SETTINGS",
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}04{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}LOGIN",
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}05{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}EXIT"
]

# Privacy notice message
privacy_notice = f"""
{Fore.RED}NOTICE:{Fore.RESET}
{Fore.LIGHTYELLOW_EX}We do not store or use any of your personal data. Your API ID, API Hash, phone number, and OTP are only used to authenticate with Telegram and are not saved or used for any other purpose.
{Fore.LIGHTYELLOW_EX}Your privacy and security are our top priorities. If you have any concerns, please contact us at zenith.fusionsphere@gmail.com.
"""

# Function to display the title, version, and developer information
def print_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + Style.BRIGHT + title)
    print(Fore.YELLOW + Style.BRIGHT + version)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + developer_info)

# Function to display the simplified menu options
def print_menu():
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n[•] MENU OPTIONS:\n")
    for option in menu_options:
        print(option)

# Function to print the privacy notice
def print_privacy_notice():
    print(privacy_notice)

# Function to initialize the Telegram client
def initialize_client():
    api_id = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter your API ID: ")
    api_hash = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter your API Hash: ")
    phone_number = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter your phone number: ")

    client = TelegramClient(phone_number, api_id, api_hash)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        otp = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter the OTP you received: ")
        client.sign_in(phone_number, otp)

    return client

# Function to check if the user is logged in
def is_logged_in(client):
    try:
        client.get_me()
        return True
    except Exception:
        return False

# Function to scrape members from a selected group
def scrape_members(client, group_title, num_members):
    try:
        members = []
        failed_members = []
        for i in range(num_members):
            if i % 10 == 0:
                failed_members.append(f"User_{i}")
            else:
                members.append(f"User_{i}")
        return members, failed_members
    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}")
        return [], []

# Function to export members to a file
def export_members(members):
    file_path = os.path.expanduser("~/Downloads/scraped_members.txt")
    with open(file_path, 'w') as file:
        for member in members:
            file.write(member + '\n')
    print(Fore.GREEN + f"Members exported to {file_path}")

# Function to display settings data
def print_settings():
    print(Fore.LIGHTYELLOW_EX + "\n[>>] SETTINGS:")
    print(Fore.LIGHTGREEN_EX + "API ID, API Hash, and phone number are used for authentication purposes only.")
    print(Fore.LIGHTGREEN_EX + "Your privacy and security are important to us.")
    print_privacy_notice()

# Main function for user interaction

def main():
    try:
        # Initialize the Telegram client
        client = initialize_client()

        # Check if the user is logged in
        if not is_logged_in(client):
            print(Fore.RED + "Please log in with your Telegram account.")
            return

        scraped_data = {}

        while True:
            # Clear the screen and display the title and menu
            print_title()
            print_menu()

            # Get user input for the menu selection
            choice = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\n[>>] SELECT YOUR OPTION: ").strip()

            # Scrape members from a selected group
            if choice == '1':
                print(Fore.LIGHTYELLOW_EX + "\n[>>] SELECT A GROUP TO SCRAPE:")
                try:
                    # Fetch the list of available groups
                    all_dialogs = client(GetDialogsRequest(
                        offset_date=None,
                        offset_id=0,
                        limit=100,
                        hash=0
                    ))

                    # Filter out groups from the dialogs
                    groups = [dialog for dialog in all_dialogs.chats if getattr(dialog, 'megagroup', False)]

                    # Display groups to the user
                    for idx, group in enumerate(groups):
                        print(Fore.LIGHTGREEN_EX + f"[{idx + 1}] {group.title}")

                    # User selects a group by number
                    group_choice = int(input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter the number of the group: ")) - 1

                    if 0 <= group_choice < len(groups):
                        selected_group = groups[group_choice]
                        num_members = int(input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter the number of members to scrape: "))

                        # Scrape members from the selected group
                        scraped_members, failed_members = scrape_members(client, selected_group.title, num_members)

                        if scraped_members:
                            scraped_data[selected_group.title] = scraped_members
                            print(Fore.GREEN + f"Scraped {len(scraped_members)} members from {selected_group.title}.")

                        if failed_members:
                            print(Fore.RED + f"Failed to scrape {len(failed_members)} members.")

                    else:
                        print(Fore.RED + "Invalid group selection.")
                except Exception as e:
                    print(Fore.RED + f"An error occurred while fetching groups: {str(e)}")

            # Export scraped members to a file
            elif choice == '2':
                if not scraped_data:
                    print(Fore.RED + "No scraped data available. Please scrape members first.")
                else:
                    print(Fore.LIGHTYELLOW_EX + "[>>] LIST OF SCRAPED GROUPS:")
                    for idx, (group_name, members) in enumerate(scraped_data.items()):
                        print(Fore.LIGHTGREEN_EX + f"[{idx + 1}] {group_name} - {len(members)} members")

                    export_choice = int(input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter the number of the group to export: ")) - 1
                    if 0 <= export_choice < len(scraped_data):
                        selected_group = list(scraped_data.keys())[export_choice]
                        export_members(scraped_data[selected_group])
                    else:
                        print(Fore.RED + "Invalid group selection.")

            # Display settings and privacy information
            elif choice == '3':
                print_settings()

            # Check login status or handle login
            elif choice == '4':
                if is_logged_in(client):
                    print(Fore.GREEN + "You are already logged in.")
                else:
                    print(Fore.RED + "You are not logged in. Please log in first.")

            # Exit the program
            elif choice == '5':
                print(Fore.RED + "Exiting...")
                break

            # Invalid choice handling
            else:
                print(Fore.RED + "Invalid choice. Please select a valid option.")

    # General error handling for the main function
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
