import socket
import datetime

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0  # True if open, False if closed
    except socket.error:
        return False

def scan_range(host, start_port, end_port):
    print(f"\n{'='*45}")
    print(f"  Port Scanner")
    print(f"{'='*45}")
    print(f"  Host:   {host}")
    print(f"  Ports:  {start_port} - {end_port}")
    print(f"  Time:   {datetime.datetime.now()}")
    print(f"{'='*45}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"  [OPEN]   Port {port}")
            open_ports.append(port)
        else:
            print(f"  [closed] Port {port}")

    print(f"\n{'='*45}")
    print(f"  Scan complete. {len(open_ports)} open port(s) found.")
    if open_ports:
        print(f"  Open ports: {open_ports}")
    print(f"{'='*45}\n")

def main():
    print("\n⚠️  Only scan hosts you own or have permission to scan.\n")
    host = input("Enter host to scan (e.g. 127.0.0.1 for your own machine): ").strip()
    start = int(input("Start port (e.g. 1): "))
    end = int(input("End port (e.g. 100): "))
    scan_range(host, start, end)

if __name__ == "__main__":
    main()