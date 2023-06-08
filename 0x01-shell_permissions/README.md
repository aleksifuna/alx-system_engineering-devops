su betty: switches te current user to the user betty
whoami: prints the effective username of the current user
groups $whoami: prints all the groups the current user is part of
chown betty hello: changes the owner of hello to user betty
chmod u+x hello:adds execute permission to the owner of the file hello
chmod ug+x,o+r hello:gives the owner and group owner execute permissions, gives others only read permission
chmod ugo+x:adds exectuion rights to owner,group owner and others on file hello
setfacl -m u::--- -m g::--- -m o::rwx: sets different permissions to different users
chmod 753 hello: sets the permissions to the file hello to 753
chmod --reference=olleh hello:sets the mode of hello to be the same as olleh
chmod a-x */:sets the mode of all subdirectories in the parent directory to have execute permissions
mkdir -m 751 my_dir: makes a directory called my_dir and assigns the mode 751 to it
chown :school hello: changes ownership group to school
chmod -R vincent:staff .:changes the owner and group owner to vincent and staff respectively for all files in the current working directory
