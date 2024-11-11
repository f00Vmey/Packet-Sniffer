from scapy.all import sniff
from datetime import datetime
import socket
from colorama import Fore, init

# Initialize colorama for colored output
init(autoreset=True)

# A dictionary to cache hostnames
hostname_cache = {}

def resolve_ip(ip):
    """Try to resolve IP to hostname and cache the result"""
    if ip in hostname_cache:
        return hostname_cache[ip]
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        hostname_cache[ip] = hostname
        return hostname
    except (socket.herror, socket.gaierror):
        hostname_cache[ip] = ip  # Cache the IP if resolution fails
        return ip

def packet_callback(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if packet.haslayer("IP"):
        src = packet["IP"].src
        dst = packet["IP"].dst
        proto = packet["IP"].proto

        # Resolve IPs to hostnames using the caching method
        src_host = resolve_ip(src)
        dst_host = resolve_ip(dst)

        # Display packet info with color
        if proto == 6:  # TCP protocol
            print(f"{Fore.GREEN}[{timestamp}] SRC: {src_host} -> DST: {dst_host} | Protocol: TCP")
        elif proto == 17:  # UDP protocol
            print(f"{Fore.YELLOW}[{timestamp}] SRC: {src_host} -> DST: {dst_host} | Protocol: UDP")
        else:
            print(f"{Fore.RED}[{timestamp}] SRC: {src_host} -> DST: {dst_host} | Protocol: {proto}")

# Start sniffing packets with some optimizations
print(Fore.GREEN + "Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0, count=0)
