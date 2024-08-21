# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pywhatkit as kit
import argparse
import pandas as pd
from datetime import datetime, timedelta

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def send_messages_from_csv(csv_file, experiment, msg, wait_time=10):
    # Read the CSV file
    contacts = pd.read_csv(csv_file)
    print(f'\nContacts:\n{contacts}')

    # Iterate over each contact
    for index, row in contacts.iterrows():
        phone = "+55" + str(row['telefone']).replace(" ", "")
        print(f'index:  {index}, phone: {phone}\n')

        # Calculate the time to send the message
        now = datetime.now() + timedelta(minutes=1)
        current_hour = now.hour
        minute_of_send = now.minute

        # Send the message
        kit.sendwhatmsg(phone, experiment + msg, current_hour, minute_of_send, wait_time, True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    parser = argparse.ArgumentParser(description='Send WhatsApp messages from a CSV file.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file with contacts')
    parser.add_argument('experiment', type=str, help='Experiment prefix for the message')
    parser.add_argument('msg', type=str, help='Message to send')
    parser.add_argument('--wait_time', type=int, default=20, help='Wait time between messages (default: 10 seconds)')

    args = parser.parse_args()

    print(f'file, {args.csv_file}')
    print(f'file, {args.experiment}')
    print(f'file, {args.msg}')
    print(f'file, {args.wait_time}')

    send_messages_from_csv(args.csv_file, args.experiment, args.msg, args.wait_time)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
