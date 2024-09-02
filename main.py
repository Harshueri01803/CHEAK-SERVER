import time
import os
import threading

class MyHandler:
    def do_GET(self):
        return "THE LEGeND AARAV HERE^^"

def execute_server():
    PORT = 4000
    print(f"Server running at http://localhost:{PORT}")

def send_messages():
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    def liness():
        print('\u001b[37m' + '---------------------------------------------------')

    cls()

    # Read local files
    with open('Tukun.txt', 'r') as file:
        tokens = file.readlines()

    with open('Convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('File.txt', 'r') as file:
        text_file_path = file.read().strip()

    with open(text_file_path, 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)
    max_tokens = len(tokens)  # Use all tokens

    with open('Tata.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('Time.txt', 'r') as file:
        speed = int(file.read().strip())

    liness()

    # Simulate sending messages
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                token = tokens[token_index].strip()

                message = messages[message_index].strip()

                # Print message instead of sending it
                print(f"[+] Message {message_index + 1} of Convo {convo_id} sent by Token {token_index + 1}: {haters_name} {message}")
                liness()
                liness()
                time.sleep(speed)

            print("[+] All messages sent. Restarting the process...")
        except Exception as e:
            print(f"[!] An error occurred: {e}")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    send_messages()

if __name__ == '__main__':
    main()
