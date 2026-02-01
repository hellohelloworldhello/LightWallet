# LightWallet

LightWallet is a lightweight, command-line interface tool for managing Ethereum wallets. It provides a suite of features for generating new wallets, restoring existing ones via seed phrases, and monitoring balances directly from the terminal.
Core Features

    Wallet Generation: Create 12-word BIP39 mnemonics and derive Ethereum addresses/private keys locally.

    Wallet Restoration: Import existing 12 or 24-word seed phrases to recover access to Ethereum accounts.

    Balance Monitoring: Real-time balance checking using the Cloudflare Ethereum RPC gateway.

    Local Storage: Automatically logs generated addresses, private keys, and mnemonics to local .txt files for easy reference.

    Wallet Management: View all saved addresses or delete specific entries directly through the CLI menu.

#Installation

The tool requires Python 3.x and the following libraries for cryptographic derivation and blockchain interaction:

pip install bip_utils requests web3

# Usage

Run the main script to enter the command interface:

python LightWallet.py

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
Technical Architecture

The tool utilizes the BIP44 hierarchical deterministic (HD) wallet standard to derive keys.

    Mnemonic Generation: BIP39 standard.

    Key Derivation: BIP32/BIP44 standard using the path m/44'/60'/0'/0/0.

    Blockchain Communication: JSON-RPC over HTTPS.

The balance verification logic follows this process:

    The script reads saved addresses from addresses.txt.

    It sends a eth_getBalance request to the RPC node.

    The response (in Hexadecimal Wei) is converted to human-readable Ether.

