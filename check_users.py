def check_users(current_users, new_users):
    pass
    # YOUR CODE HERE
    new_list = []
    current_users = [user.lower() for user in current_users]
    for new_us in new_users:
        if new_us in current_users:
            print("Sorry this username is taken. Please enter a new username. :)")
        else:
            print("Nice, username is available.")    
if __name__ == "__main__":
    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)