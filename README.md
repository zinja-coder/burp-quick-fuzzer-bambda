# Burp Quick Fuzzer - Custom Repeater Action (Bambda Script)

**Quick Fuzzer** is a Burp Suite Bambda script for Custom Repeater Action that lets you instantly fuzz parameter insertion points with a basic set of payloads — without needing a to leave repeater tab.

## Why?
- During lots of my web application engagments, client asks me not to perform automatic scann and intruder fuzzing but still they want to manually cover common payloads. This is the solution for such scenarios where I can automate my small manual payload testing with one click solution.

## 🔧 Features
- Sends a small list of fuzzing payloads - You can add/remove yours payloads.
- Fast, scriptable, and useful for quick checks during manual testing.
- Zero setup — just drop it in and run from Burp!

## 🚀 Usage

1. Open Burp Suite.
2. Navigate to **Extender → Bambda Scripts**.
3. Click **"Load"**, select `quick-fuzzer.bambda`.
4. Select a request in **Repeater** context.
5. Run the script to send all payloads and view responses.

## 📦 Payloads Included

- SQLI
- XSS
- SSTI
- Command Injection
- Business Logic Payloads
- Invalid Date
- Invalid Time
- Negative Values
- Empty Values

> You can customize or extend the payload list directly in the script.
> You can add/remove attacks types as well, i.e commenting out the payloads for invalid date will not perform that check.

