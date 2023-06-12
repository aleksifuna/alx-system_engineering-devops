echo "Hello, World":prints Hello, world to the standard output
echo "\"(Ôo)'": Displays a confused smiley "(Ôo)'
cat /etc/passwd: Displays the content of the /etc/passwd file
cat /etc/passwd /etc/hosts : displays the content of the two files
tail -n 10 /etc/passwd:displays the last 10 lines of the file /etc/passwd
head -n 10 /etc/passwd:displays the first 10 lines of the file /etc/passwd
head -n 3 iacta|tail -n 1:displays the content of line 3 in aicta file
ls -la>ls_cwd_content:outputs the output of ls -la into file ls_cwd_content
tail -n 1 iacta >>iacta: duplicates the last line of the file iacta
find . -name "*.js" -type f -delete: deletes only files with .js exetension ignoring directories
find . -type d -print |wc -l: counts the number of directories and subdirecotries in a given parent dir
cat list|sort|uniq: prints the contents of the file cat in a sorted format and only uniq items
grep root /etc/passwd: displays the lines containing the pattern "root" in /etc/passwd
grep bin /etc/passwd: displays the number of lines containing bin in /etc/passwd
grep -v bin /etc/passwd: Displays all the lines in the file /etc/password that do not contain the word bin
grep '^[[:upper:]]' /etc/ssh/sshd_config:displays lines starting with alphabets in the file /etc/ssh/sshd_config
