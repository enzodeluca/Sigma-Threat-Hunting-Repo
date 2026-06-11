import random
import time

# A few fake IP addresses (one malicious attacker, two safe users)
attacker_ip = "192.168.1.150"
user_ips = ["10.0.0.42", "10.0.0.55"]
usernames = ["root", "admin", "user1", "test", "guest"]

print("Generating mock security log file...")

with open("ssh_mock.log", "w") as f:
    # Let's generate 50 log lines
    for _ in range(100):
        timestamp = time.strftime("%b %d %H:%M:%S")
        
        if random.random() < 0.3:
            ip = random.choice(user_ips)
            f.write(f"{timestamp} myserver sshd[12345]: Accepted password for user john_doe from {ip} port 54321 ssh2\n")
        
        else:
            user = random.choice(usernames)
            f.write(f"{timestamp} myserver sshd[12345]: Failed password for invalid user {user} from {attacker_ip} port 33211 ssh2\n")

print("Done! 'ssh_mock.log' has been created successfully.")
