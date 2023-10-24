import time
import os

# Define the file path to the text file containing usernames, usernames.txt would be replaced by sessions-X
text_file_path = 'usernames.txt'

# Define a list of unauthorized usernames, would change these based on the email addresses
unauthorized_users = ['user1', 'user2', 'user3']

# Function to parse usernames from the text file and return them in a list
def parse_usernames(file_path):
    user_list = []
    with open(file_path, 'r') as file:
        for line in file:
            username = line.strip()
            user_list.append(username)
    return user_list

# Function to check for unauthorized users and restart SSH service
def check_and_restart_ssh(user_list, unauthorized_users):
    for user in user_list:
        if user in unauthorized_users:
            time.sleep(360)  # Wait for 6 minutes

            # Restart SSH service using the 'service' command (we may need root privileges)
            os.system('sudo service ssh restart')

# Main script
while True:
    user_list = parse_usernames(text_file_path) # Need to figure out a way to check specific text files as they come in, this only parses through 1 specific file
    check_and_restart_ssh(user_list, unauthorized_users)
    time.sleep(60)  # Check every 60 seconds (adjust as needed)
