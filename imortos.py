




import os

# Execute 'whoami' command and store the result in a variable
whoami_result = os.popen('whoami').read().strip()

# Execute 'ip a' command and store the result in a variable
ip_result = os.popen('ip a').read().strip()

# Execute 'lshw -short' command and store the result in a variable
lshw_result = os.popen('lshw -short').read().strip()

# Open a text file in write mode
with open('/home/roguione/Desktop/bash_results.txt', 'w') as f:
    # Write the results to the file
    f.write(f"Result of 'whoami' command:\n{whoami_result}\n\n")
    f.write(f"Result of 'ip a' command:\n{ip_result}\n\n")
    f.write(f"Result of 'lshw -short' command:\n{lshw_result}\n\n")

# Print a message indicating the results have been written to the file
print("Results written to /home/roguione/Desktop/bash_results.txt")
