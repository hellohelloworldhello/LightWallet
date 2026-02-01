<img width="769" height="218" alt="image" src="https://github.com/user-attachments/assets/b118f87b-27d8-4bec-b8d2-9a4cc50c8796" />


                                                                                    

LightWallet is a lightweight, command-line interface tool for managing Ethereum wallets. It provides a suite of features for generating new wallets, restoring existing ones via seed phrases, and monitoring balances directly from the terminal.
Core Features

    Wallet Generation: Create 12-word BIP39 mnemonics and derive Ethereum addresses/private keys locally.

    Wallet Restoration: Import existing 12 or 24-word seed phrases to recover access to Ethereum accounts.

    Balance Monitoring: Real-time balance checking using the Cloudflare Ethereum RPC gateway.

    Local Storage: Automatically logs generated addresses, private keys, and mnemonics to local .txt files for easy reference.

    Wallet Management: View all saved addresses or delete specific entries directly through the CLI menu.

# Installation
### Installation

LightWalletCLI requires **Python 3.x** and specific **C++ components** to handle cryptographic functions.

---

#### 1. Install C++ Build Tools (Windows Only)
The libraries `web3` and `bip-utils` often require C++ compilation during installation. If you encounter errors regarding "Microsoft Visual C++" or "Build Tools," you must install the following:

* Download the **[Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)**.
* During installation, select **Desktop development with C++**.
* Restart your computer once finished.

#### 2. Install Python Dependencies
Use the `python -m` flag to ensure libraries are installed correctly even if your system PATH is not fully configured:

```bash
python -m pip install --upgrade pip
python -m pip install requests bip-utils web3
```

#### 3. Verification
Verify the installation by running this command in your terminal:

```bash
python -c "import web3; import bip_utils; import requests; print('Setup Successful')"
```

---

### Running the Tool
Put all the TXT files AND the LightWalletCLI.py in the same folder, navigate to your project folder and launch the application:

```bash
python LightWalletCLI.py
```

Done!

# Usage

Use the commands below

# Commands

Once the tool is running, use the following flags to navigate the features:
Command	Action
-c	Create a brand new Ethereum wallet
-r	Restore a wallet using a 12/24 word seed phrase
-b	Balance check for all saved addresses
-a	All saved addresses display
-d	Delete a specific saved wallet from local files
-w	Withdraw interface (simulated network connection)
-h	Help menu to show all commands
-q	Quit the application

# Technical Architecture

The tool utilizes the BIP44 hierarchical deterministic (HD) wallet standard to derive keys.

    Mnemonic Generation: BIP39 standard.

    Key Derivation: BIP32/BIP44 standard using the path m/44'/60'/0'/0/0.

    Blockchain Communication: JSON-RPC over HTTPS.

The balance verification logic follows this process:

    The script reads saved addresses from addresses.txt.

    It sends a eth_getBalance request to the RPC node.

    The response (in Hexadecimal Wei) is converted to human-readable Ether.

