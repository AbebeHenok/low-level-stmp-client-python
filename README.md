# Low-Level SMTP Client in Python

This project implements a **low-level SMTP email client** using Python sockets, demonstrating how email is sent over the network **without using high-level libraries like `smtplib`**.

The client:
- Establishes a TCP connection to an SMTP server
- Performs the SMTP handshake (`HELO`)
- Upgrades the connection using **STARTTLS**
- Authenticates using **AUTH PLAIN**
- Sends an email using raw SMTP commands

This project is intended for **educational and networking/security learning purposes**.

---

## Technologies Used
- Python 3
- TCP Sockets
- SMTP Protocol
- TLS (STARTTLS)
- Base64 Encoding

---

## Features
- Manual SMTP command handling
- TLS-encrypted communication
- SMTP authentication
- Message composition and delivery
- Clear visibility into server responses

---

## How to Run

1. Clone the repository
2. Install Python 3
3. Set environment variables (see below)
4. Run:
```bash
python smtp_client.py
