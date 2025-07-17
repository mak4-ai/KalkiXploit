# KalkiXploit 💀

**Advanced Python-based Exploit Builder & Delivery Framework**

> Developed by Makbing (Makrand Ingale)

---

## 🌟 Features

- ✅ Bash, Python, and PowerShell reverse shell payloads
- ✅ Advanced encoders: Base64, XOR, ROT13
- ✅ Delivery methods: HTTP server, SMTP mailer
- ✅ Listener support: Netcat auto-launch
- ✅ EXE payload generation (PyInstaller)
- ✅ Interactive CLI with beautiful banners
- ✅ Runs like fsociety with `./kalkixploit` command

---

## 🧠 What Can It Do?

KalkiXploit lets you **create**, **encode**, **deliver**, and **listen** for reverse shell payloads with a full attack chain—great for practicing ethical hacking and red teaming in your lab.

---

## ⚙️ Setup Instructions

### 🐍 Requirements

- Python 3.x
- `pyinstaller` (`pip install pyinstaller`)
- `netcat` (pre-installed on Kali)
- SMTP server (for email delivery)

### 📦 Install

```bash
git clone https://github.com/yourusername/KalkiXploit.git
cd KalkiXploit
chmod +x kalkixploit
pip install -r requirements.txt
