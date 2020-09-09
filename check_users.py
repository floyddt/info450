def check_users(current_users, new_users):
    pass
    # YOUR CODE HERE
    current_users = [user.lower() for user in current_users]

    for new_us in new_users:
        if new_us in current_users:
            print("Sorry, {} is taken. Please enter a new username. :)".format(new_us))
        else:
            print("Nice, {} is available.".format(new_us))
                
if __name__ == "__main__":
    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)