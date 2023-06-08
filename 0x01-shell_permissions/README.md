su betty: switches te current user to the user betty
whoami: prints the effective username of the current user
groups $whoami: prints all the groups the current user is part of
chown betty hello: changes the owner of hello to user betty
chmod u+x hello:adds execute permission to the owner of the file hello
chmod ug+x,o+r hello:gives the owner and group owner execute permissions, gives others only read permission
