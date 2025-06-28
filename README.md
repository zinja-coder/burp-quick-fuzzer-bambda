# Burp Quick Fuzzer - Custom Repeater Action (Bambda Script)

**Quick Fuzzer** is a Burp Suite Bambda script for Custom Repeater Action that lets you instantly fuzz parameter insertion points with a basic set of payloads — without needing a to leave repeater tab.

## Why?
- During lots of my application security engagments, client asks me not to perform automatic scann and intruder fuzzing but still they want to manually cover common payloads. This is the solution for such scenarios where I can automate my small manual payload testing with one click solution.

## Features
- Sends a small list of fuzzing payloads - You can add/remove yours payloads.
- Fast, scriptable, and useful for quick checks during manual testing.
- Modify as Per Need - Add/remove payloads and checks as per requirements
- You can modify the delay between requests as well.

## Usage

https://github.com/user-attachments/assets/f37399fe-9459-407d-9493-6da9b0f91c91

https://github.com/user-attachments/assets/b8fb43fd-9121-429b-8735-09a00018edc7

1. Clone this repo.
2. Open Burp Suite.
3. Navigate to **Extender → Bambda Scripts**.
4. Click **"Load"**, select `quick-fuzzer.bambda`.
5. Set Location as `Custom Action` and `Repeater`, see the video
6. Select a request in **Repeater** context.
7. Run the script to send all payloads and view responses.

## Add Delay

https://github.com/user-attachments/assets/5e3cccd4-2da3-4390-b6b3-34217651ff0c

## Add/Remove Payloads

https://github.com/user-attachments/assets/be76b0f2-4a07-4b00-a901-53414d099b6f

## Payloads Included - Modifiable

- SQLI
- XSS
- SSTI
- JSON Injection
- LDAP Injection
- Path Traversal
- NOSQLI
- Command Injection
- Special Character Allowed or Not
- String Format Payloads
- Business Logic Payloads
- Input Length
- Invalid Emails
- Invalid Date
- Invalid Time
- Negative Values
- Empty Values

> You can customize or extend the payload list directly in the script.
> 
> You can add/remove attacks types as well, i.e commenting out the payloads for invalid date will not perform that check.
> 
> When you can run scan and fuzz, comment out the technical payloads and quickly test for non-technical payloads like invalid emails.
> 
> Note: This is not replacement of intruder/scanner, it is just a custom action for repeater to solve very specific issue of automation of manual test cases. Read the script before running and check if it matches your use case.
>
> It is not new ground breaking tool or anything like that.

