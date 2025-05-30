# 🚀 Turbo Intruder X-Forwarded-For Brute Force Bypass

This repository contains a custom Turbo Intruder script that leverages the `X-Forwarded-For` header to bypass IP-based brute force protections. It's inspired by a real-world exploitation of the Nibbleblog machine on Hack The Box.

## 📌 Use Case

Some web applications blacklist IP addresses after multiple failed login attempts. However, if the application trusts the `X-Forwarded-For` (XFF) header, this can be spoofed per request — allowing attackers to brute force credentials without being blocked.

This script automates:
- Cycling through a large wordlist (e.g. `rockyou.txt`)
- Generating spoofed IP addresses from `192.168.0.0` to `192.168.255.255`
- Sending requests with a unique `X-Forwarded-For` header for each password attempt

## 🛠 Requirements

- Burp Suite with [Turbo Intruder extension](https://github.com/portswigger/turbo-intruder)
- Python 3
- Wordlist (e.g. `rockyou.txt`)

## 🔧 Usage

1. Load Burp Suite → Extensions → Turbo Intruder.
2. Open `turbo_script.py` in Turbo Intruder.
3. Replace `target.endpoint` and headers as per your target.
4. Run the attack.

## 💡 Note

This script generates up to **65,536** spoofed IPs using the format `192.168.X.Y`, covering IPs from `192.168.0.0` to `192.168.255.255`.

## 🛡️ Disclaimer

This tool is for educational and authorized testing only. Do **not** use it against systems without explicit permission.

## 📖 Blog Reference

Full walkthrough and explanation in this blog: https://hackernoon.com/breaking-into-a-server-using-a-hello-world-page-and-a-fake-jpeg

---

Enjoy breaking things responsibly ⚔️

