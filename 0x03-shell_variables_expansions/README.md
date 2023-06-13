alias ls=rm *:creates an alias names ls to perform rm *
echo "hello $USER": prints hello user where user is the current linux user
printev:lists environment variables
set: lists all local variables and environment variables and functions
echo $((POWER/DIVIDE)): prints the results of POWER/DIVIDE
echo $((BREATH**LOVE)):displays the result of BREATH to the power LOVE
printf "%d\n" "((2#$BINARY))": converts binary to decimal
echo {a..z}{a..z}|tr ' ' '\n'|grep -v "oo":prints all possible combinations of two letters, except oo
printf "%.2f\n" $NUM:prints anumber with two decimal places followed by a new line
