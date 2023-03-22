




#!/bin/bash

# Get current timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

# Define backup directory
backup_dir="/var/log/backups"

# Create backup directory if it doesn't exist
if [ ! -d "$backup_dir" ]; then
  mkdir "$backup_dir"
fi

# Compress syslog log file
syslog_file="/var/log/syslog"
syslog_size=$(du -h "$syslog_file" | awk '{print $1}')
zip_file="$backup_dir/syslog-$timestamp.zip"
zip -qj "$zip_file" "$syslog_file"
echo "Original size of $syslog_file: $syslog_size"
echo "Compressed size of $zip_file: $(du -h $zip_file | awk '{print $1}')"
> "$syslog_file"
echo "Contents of $syslog_file cleared."

# Compress wtmp log file
wtmp_file="/var/log/wtmp"
wtmp_size=$(du -h "$wtmp_file" | awk '{print $1}')
zip_file="$backup_dir/wtmp-$timestamp.zip"
zip -qj "$zip_file" "$wtmp_file"
echo "Original size of $wtmp_file: $wtmp_size"
echo "Compressed size of $zip_file: $(du -h $zip_file | awk '{print $1}')"
> "$wtmp_file"
echo "Contents of $wtmp_file cleared."

# Additional logs that can be cleared:
# /var/log/auth.log - tracks authentication events 
# /var/log/faillog - tracks failed login attempts
# /var/log/lastlog - tracks the last login for each user
# /var/log/dmesg - kernel ring buffer logs
# /var/log/apache2/access.log - tracks Apache HTTP server access
# /var/log/apache2/error.log - tracks Apache HTTP server errors

