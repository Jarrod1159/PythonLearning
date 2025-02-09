import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip_address, firewall_rules):
    ''' for loop to unpack the dictionary by using the items function
        for each of the IPS on our block list. It'll compare the randomly
        generated IP and see if they match
    '''
    for rule_ip, action in firewall_rules.items():
        if ip_address == rule_ip:
            return action
    return "allow"

def main():
    # Define firewall rules
    firewall_rules = {
#this is a arbitrary list of IPs that are blocked

        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    for _ in range(10):
        # Generate a random IP address
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP Address: {ip_address}, Action: {action}, Random Number: {random_number}")
if __name__ == "__main__":
    # Entry point of the script
    main()

