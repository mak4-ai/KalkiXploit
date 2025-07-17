import subprocess
import sys

def start_netcat_listener(lhost: str, lport: int):
    """
    Start a netcat listener to catch reverse shells.
    Requires netcat (nc) installed on your system.
    """
    print(f" Starting Netcat listener on {lhost}:{lport} ...")
    print("[ℹ] Waiting for connection... Press CTRL+C to stop.")
    try:
        # Launch netcat in a subprocess
        # '-lvp' means: listen verbosely on a port
        subprocess.run(["nc", "-lvnp", str(lport)])
    except FileNotFoundError:
        print(" Netcat is not installed! Install with: apt install netcat-traditional")
    except KeyboardInterrupt:
        print("\n[ℹ] Listener stopped by user.")
    except Exception as e:
        print(f" Failed to start listener: {e}")

# Optional: quick test if run directly
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <LHOST> <LPORT>")
        sys.exit(1)
    start_netcat_listener(sys.argv[1], int(sys.argv[2]))
