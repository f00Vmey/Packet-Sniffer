from scapy.all import IP, ICMP, sr1
import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def traceroute(destination, max_hops=30, timeout=2):
    print(f"{Fore.GREEN}Tracing route to {destination}...\n")
    for ttl in range(1, max_hops + 1):
        # Create the packet: IP + ICMP
        packet = IP(dst=destination, ttl=ttl) / ICMP()
        
        # Send the packet and get the response
        start_time = time.time()
        reply = sr1(packet, timeout=timeout, verbose=0)
        end_time = time.time()

        if reply is None:
            print(f"{Fore.YELLOW}{ttl}\tRequest Timed Out")
        else:
            rtt = (end_time - start_time) * 1000  # Round-trip time in milliseconds
            # Show the hop's information in green
            print(f"{Fore.GREEN}{ttl}\t{reply.src}\t{rtt:.2f} ms")

        # Exit if the destination is reached
        if reply and reply.src == destination:
            print(f"{Fore.RED}Destination {destination} reached at hop {ttl}")
            break

# Example usage
destination = input(f"{Fore.WHITE}Enter value (IP/Domain)$: ")
traceroute(destination)

# Wait for user to press Enter before exiting
input(f"{Fore.WHITE}\nPress Enter to continue...")
