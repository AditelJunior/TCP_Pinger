# P2P system using TCP protocol
This is a TCP-based ping and pong program implemented in Python. It allows clients to send ping messages to the server, which responds with a pong message. Additionally, clients can perform various operations such as sending files, visualizing images, CSV files, and JSON files, as well as broadcasting files to multiple clients. The program provides a menu for selecting these options.

## How to Run
Start the server by running the server.py script.
Run the client.py script to start a client.
The client will display a menu with available options. Enter the corresponding number for the desired operation.
Follow the prompts and enter the required information, such as file paths or server IP and port.
The program will execute the selected operation and display the results or status messages.
Features
- 1. Send Ping
Allows the client to send a ping message to the server.
The server responds with a pong message.
- 2. Send File
Enables the client to send a file to the server.
Supports various file types, including images, CSV files, and JSON files.
The client enters the file path, and the file is sent to the server.
- 3. Visualize Image
Allows the client to visualize an image file.
The client enters the image file path, and the program displays the image using matplotlib.
- 4. Visualize CSV
Enables the client to visualize a CSV file.
The client enters the CSV file path, and the program prints the CSV data row by row.
- 5. Visualize JSON
Allows the client to visualize a JSON file.
The client enters the JSON file path, and the program prints the JSON data in a formatted manner.
- 6. Broadcast File
Enables the client to broadcast a file to multiple clients.
The client enters the file path, and the file is sent to all connected clients.
- 7. Exit
Allows the client to exit the program.
Dependencies
## The program requires the following dependencies:
```
matplotlib
```
- for visualizing images
```
pandas
```
- for visualizing CSV files
Install these dependencies using pip install matplotlib pandas before running the program.

## Author
This program was written by Adilet Aitmatov(12230114).
