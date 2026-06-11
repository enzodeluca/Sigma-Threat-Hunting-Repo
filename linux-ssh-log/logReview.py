# Review attempted login attempts and parse out those that failed. 
# This is based on genLogs.py update keywords as necessary

# Basic log file check for failed login attempts

log_file_path = "/home/enzodeluca/Projects/Python/Cybersec/ssh_mock.log" # Change this to your file location

failed_attempts = {}

with open(log_file_path, "r") as file:
    for line in file:
        # Look for failed logins
        if "Failed password" in line:
            words = line.split()

            if "from" in words:
                ip_index = words.index("from")+1
                ip_address = words[ip_index]

                if ip_address in failed_attempts:
                    failed_attempts[ip_address]+=1
                else:
                    failed_attempts[ip_address] = 1

print("----DETECTION REPORT----")
for ip, count in failed_attempts.items():
    print(f"IP Address {ip} attempted to brute-force {count} times.")
if count > 5:
        print(f"[CRITICAL ALERT] Threshold exceeded! Automating firewall block for IP: {ip}")
