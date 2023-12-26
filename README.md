# Simple Port Scanner

This is a simple port scanner written in Python that allows you to scan ports on a target machine. The script utilizes multi-threading to improve the scanning speed and checks if a connection can be established on each port within a specified timeout.

## Usage

### Prerequisites

- Python 3.x

### How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/simple-port-scanner.git
    cd simple-port-scanner
    ```

2. Run the scanner:

    ```bash
    python port_scanner.py <target>
    ```

    Replace `<target>` with the target IP address or hostname.

## Features

- Scans ports in the range from 1 to 65535.
- Multi-threaded for faster scanning.
- Displays open ports on the target.

## Script Overview

### Modules

- `argparse`: Used for parsing command line arguments.
- `socket`: Provides low-level networking interface.
- `threading`: Enables multi-threading support.
- `datetime`: Handles date and time operations.

### Constants

- `MAX_PORT`: The maximum port number to scan.
- `TIMEOUT`: Timeout value for attempting a connection to a port.

### Functions

1. **`scan_port(target, port)`**
    - Scans a specific port on the target machine.
    - Creates a TCP socket and attempts to connect to the specified port.
    - Prints a message if the port is open.

2. **`scan_target(target)`**
    - Initiates the scanning process for all ports on the target.
    - Creates a list of threads, each responsible for scanning a specific port.
    - Displays scanning information, such as the target and start time.
    - Waits for all threads to finish.

3. **`main()`**
    - Parses command line arguments using `argparse`.
    - Resolves the target's IP address from the provided hostname.
    - Calls `scan_target` to start the scanning process.

### Entry Point

The program's entry point checks if the script is being run directly (not imported as a module) and then calls the `main` function.

Feel free to use and modify this simple port scanner for your needs. If you encounter any issues or have suggestions for improvements, please let me know. Happy scanning!
