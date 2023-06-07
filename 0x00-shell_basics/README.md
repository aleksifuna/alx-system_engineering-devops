pwd-prints the absolute path name of the current working directory
ls-Displays the contents list of your current directory
cd ~-changes the working directory to the users home directory
ls -l -Displays current directory contents in a long format
ls -la- Displays current directory contents, including hidden files in long format
ls -aln- displays current directory contents in long format with user and group IDs displayed numerically. will also list hidden files
mkdir /tmp/my_first_directory- creates a directory in /tmp directory
mv tmp/betty tmp/my_first_directory- moves the file betty from /tmp to /tmp/my_first_directory
rm /tmp/my_first_directory/betty- deletes the file betty in my_first_directory folder
rm -r /tmp/my_first_directory- deletes the directory /tmp/my_first_directory
cd --changes the working directory to the previous one
ls -la . .. /boot- lidtd sll files in the current directory and the parent of the working directory and the /boot directory in long format including hidden ones
file tmp/iamafile-prints the type of file
ln -s /bin/ls __ls__- creates a symbolic link to /bin/ls
cp -u *html ..-copies html files to parent directory and only does to new files
mv [[:UPPER:]]* /tmp/u- moves all files starting with upper case to /tmp/u
rm *~-remove all files that end with ~
mkdir welcome welcome/to/school-create folders welcome,welcome/to and welcome/to/school
ls -Ap1 | sort -dk1.1 | tr n , | sed s/,$/n/- lists all the files and directories of the current directory, separated by commas
