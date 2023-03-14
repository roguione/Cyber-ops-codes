import os
import datetime

# Set the log directory path
log_dir = "/home/roguione/Log_files"

# Create directory for log files if it doesn't exist
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# Get today's date in YYYY-MM-DD format
today = datetime.date.today().strftime("%Y-%m-%d")

# Set the log filename to include today's date
log_file = os.path.join(log_dir, "mylog_{}.txt".format(today))

# Write a message to the log file
with open(log_file, "a") as f:
    f.write("This is a log message for {}\n".format(today))

