import psutil
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_interface_name():
    interfaces = psutil.net_if_addrs()
    print(Fore.WHITE + "Available network interfaces:")
    for index, interface in enumerate(interfaces):
        print(f"{index + 1}::{interface}")
    
    try:
        choice = int(input("Interface numb$: ")) - 1
        if choice < 0 or choice >= len(interfaces):
            print(Fore.RED + "Invalid choice. Exiting..." + Style.RESET_ALL)
            exit()
        interface_name = list(interfaces.keys())[choice]
        print(Fore.YELLOW + f"Using interface: {interface_name}" + Style.RESET_ALL)
        return interface_name
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
        exit()

def test_bandwidth(interface):
    net_io = psutil.net_io_counters(pernic=True)
    if interface not in net_io:
        print(Fore.RED + f"Interface {interface} not found." + Style.RESET_ALL)
        return

    bytes_sent = net_io[interface].bytes_sent
    bytes_recv = net_io[interface].bytes_recv

    print(Fore.YELLOW + f"Monitoring interface: {interface}...\n" + Style.RESET_ALL)

    while True:
        try:
            new_net_io = psutil.net_io_counters(pernic=True)
            new_bytes_sent = new_net_io[interface].bytes_sent
            new_bytes_recv = new_net_io[interface].bytes_recv

            sent_speed = new_bytes_sent - bytes_sent
            recv_speed = new_bytes_recv - bytes_recv

            # Update previous values for the next iteration
            bytes_sent = new_bytes_sent
            bytes_recv = new_bytes_recv

            # If no bytes sent or received, display in red
            if sent_speed == 0 or recv_speed == 0:
                print(Fore.RED + f"No data sent/received for interface {interface}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"Sent: {sent_speed / 1024:.2f} KB/s | Received: {recv_speed / 1024:.2f} KB/s" + Style.RESET_ALL)

            time.sleep(1)  # Pause for 1 second before checking again
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nExiting bandwidth test..." + Style.RESET_ALL)
            break

if __name__ == "__main__":
    interface_name = get_interface_name()
    test_bandwidth(interface_name)
