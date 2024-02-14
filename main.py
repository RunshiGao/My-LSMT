from lsm_tree import LSMTree
def main():
    # Run the LSMTree interface.
    usage_msg = [
        ['Commands: ', 'Explanation'],
        ['put {key}', 'Store the key into the DB'],
        ['get {key}', 'Check if the key exist. Returns False if it doesnt exist'],
        ['file {filename}', 'Input keys from file'],
        ['\n\tConfiguration:', ''],
        ['help', 'Print the usage message'],
        ['exit', 'Quit the program.']
    ]

    db = LSMTree()
    # the interface
    while True:
        print('\nEnter a command below. Type "help" to see a list of commands.')
        # get the user's command
        cmd = input('$ ').lower().split(' ')
        if cmd[0] == 'put':
            key = cmd[1]
            db.put(key)
            print('Stored', key, " into the db")
        elif cmd[0] == 'get':
            key = cmd[1]
            found = db.get(key)
            msg = "Found key " + key if found else "Key not found"
            print(msg)
        elif cmd[0] == "file":
            filename = cmd[1]
            db.insert_keys_from_file(filename)
            print("Inserted keys from the file:"+filename)
        elif cmd[0] == 'print':
            db.print()
        elif cmd[0] == 'help':
            print_help(usage_msg)
        elif cmd[0] == 'exit':
            break
        else:
            print("Invalid command, please input again")


def print_help(usage_msg):
    for row in usage_msg:
        print("\t{: <30}{: <10}".format(*row))

if __name__ == "__main__":
    main()