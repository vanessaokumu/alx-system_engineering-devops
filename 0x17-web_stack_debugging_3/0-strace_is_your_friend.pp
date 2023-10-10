# Using strace, find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet

ps aux | grep apache
sudo strace -p <apache_pid> -o /tmp/strace_output.txt
