"""
Midterm Practical Exam — Network Device Inventory Tool
Student: [your name]
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():

    print("\n=== Network Device Inventory===")
    print("1. Add a Device")
    print("2. View All Device")
    print("3. Count active and inactive Devices")
    print("4. Find Device by name")
    print("5. Exit")
    
    input("Select an option (1-5): ").strip()
   


def add_device(device_list):
    # ask for name, IP, status — build the string, add to the list 
    devices.insert(input("Device name: "))
    devices.insert(input("IP Address: "))
    devices.insert(input("Status: "))
    pass

def view_devices(device_list):
    # loop through and print every device — handle empty list
    pass

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_device(device_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        if choice == "1":
            add_device
        elif choice == "2":
            view_devices
        elif choice == "3":
            count_active_inactive
        elif choice == "4":
            find_device
        elif choice == "5":
            remove_device
        else:
            ValueError
            print("Input a valid Choices!")
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit

main()
    