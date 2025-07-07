# Importing required modules
import argparse
import subprocess
import shutil
import webbrowser
import os
import pyfiglet
from colorama import Fore, Style, init
from rich.console import Console
from rich.panel import Panel

# Initialize colorama and rich console
init(autoreset=True)
console = Console()

# Function to print the ASCII banner with credits
def print_banner():
    ascii_art = """
/***
 *    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
 *    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
 *    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
 *    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
 *    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
 *    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """
    subtitle = "+-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+\n|H|a|c|k|i|n|g| |f|o|r| |J|u|s|t|i|c|e|,|n|o|t| |C|h|a|o|s|\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
    credit = "Built by: Krish_foren6"

    console.print(Panel(ascii_art.strip(), style="bold magenta"))
    console.print(subtitle, style="bold cyan")
    console.print(credit, style="bold yellow")

# Tool download/help links for fallback if not installed
tool_links = {
    "nmap": "https://nmap.org/download.html",
    "assetfinder": "https://github.com/tomnomnom/assetfinder",
    "amass": "https://github.com/owasp-amass/amass",
    "gobuster": "https://github.com/OJ/gobuster",
    "dirsearch": "https://github.com/maurosoria/dirsearch",
    "subfinder": "https://github.com/projectdiscovery/subfinder",
    "sqlmap": "https://github.com/sqlmapproject/sqlmap",
    "sublist3r": "https://github.com/aboul3la/Sublist3r",
    "dnsdumpster": "https://dnsdumpster.com/",
    "whatweb": "https://github.com/urbanadventurer/WhatWeb",
    "dirb": "https://tools.kali.org/web-applications/dirb",
    "nikto": "https://github.com/sullo/nikto",
    "whois": "https://linux.die.net/man/1/whois",
    "dig": "https://linux.die.net/man/1/dig",
    "webanalyze": "https://github.com/rverton/webanalyze"
}

# Recon categories and their respective tools
categories = {
    "1": ("Subdomain Enumeration", [("assetfinder", "-h"), ("amass", "-h"), ("subfinder", "-h"), ("sublist3r", "-h")]),
    "2": ("DNS Recon", [("dnsdumpster", "--help"), ("whois", "--help"), ("dig", "-h")]),
    "3": ("Vulnerability Scanning", [("nmap", "-h"), ("sqlmap", "--help"), ("dirsearch", "--help"), ("gobuster", "-h"), ("dirb", "-h"), ("nikto", "-H")]),
    "4": ("Tech Stack Detection", [("whatweb", "-h"), ("webanalyze", "-h")]),
}

# Function to run selected tool with given arguments
def run_tool(tool_name, args):
    tool_path = shutil.which(tool_name)
    if tool_path:
        # Add technologies.json path for webanalyze
        if tool_name == "webanalyze":
            args = ["-apps", "/usr/local/share/webanalyze/technologies.json"] + args

        print(f"{Fore.GREEN}[✔] {tool_name} is installed at: {tool_path}")
        print(f"{Fore.CYAN}[*] Running: {tool_name} {' '.join(args)}\n")
        try:
            # Run the tool using Popen for live output (important for tools like amass)
            process = subprocess.Popen([tool_name] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Print output line-by-line in real time
            for line in process.stdout:
                print(line, end='')

            # Print errors after completion
            stderr = process.stderr.read()
            if stderr:
                print(f"{Fore.RED}[!] Error:\n{stderr}")

            # Ask user if they want to save output
            save = input("\n💾 Do you want to save this output? (y/n): ").lower()
            if save == 'y':
                format_choice = input("Choose format - (1) txt or (2) html: ").strip()
                filename = input("Enter filename (without extension): ").strip()
                
                # Rerun tool to capture output for saving
                process = subprocess.run([tool_name] + args, text=True, capture_output=True)
                if format_choice == '1':
                    with open(f"{filename}.txt", "w") as f:
                        f.write(process.stdout)
                    print(f"[+] Output saved to {filename}.txt")
                elif format_choice == '2':
                    with open(f"{filename}.html", "w") as f:
                        f.write(f"<pre>{process.stdout}</pre>")
                    print(f"[+] Output saved to {filename}.html")
                else:
                    print("[!] Invalid choice. Output not saved.")
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to run {tool_name}: {e}")
    else:
        # If tool not found, open its install page
        print(f"{Fore.RED}[✘] {tool_name} is not installed.")
        print(f"{Fore.YELLOW}[*] Opening install page...")
        webbrowser.open(tool_links.get(tool_name, "https://google.com"))

# Main program loop
def main():
    print_banner()
    while True:
        print("\n🔧 What type of recon do you want to perform?")
        for num, (title, _) in categories.items():
            print(f"{num}. {title}")
        choice = input("\nEnter the number of recon category (or 'q' to quit): ").strip()

        if choice == 'q':
            print("👋 Exiting. Bye!")
            break

        if choice not in categories:
            print("[!] Invalid choice. Try again.")
            continue

        category_name, tools = categories[choice]
        print(f"\n📂 Tools under {choice}. {category_name}:\n")
        for i, (tool, _) in enumerate(tools, 1):
            print(f"{i}. {tool}")

        tool_choice = input("\nEnter the number of tool you want to run (or 'b' to go back): ").strip()
        if tool_choice == 'b':
            continue

        if not tool_choice.isdigit() or not (1 <= int(tool_choice) <= len(tools)):
            print("[!] Invalid tool number. Try again.")
            continue

        selected_tool, help_flag = tools[int(tool_choice)-1]

        # Show basic help for selected tool
        print(f"\n📖 Showing help for: {selected_tool}\n")
        try:
            subprocess.run([selected_tool, help_flag])
        except Exception as e:
            print(f"[!] Failed to show help: {e}")

        # Launch tool with custom args
        print(f"\n🚀 Launching: {selected_tool}")
        print(f"[*] You can now run: {selected_tool} <your target>\n")
        extra_input = input(f"Enter full command args for {selected_tool} (e.g. -sV example.com): ")
        extra_args = extra_input.strip().split()
        run_tool(selected_tool, extra_args)

# Entry point
if __name__ == "__main__":
    main()
