alias ls=rm *:creates an alias names ls to perform rm *
echo "hello $USER": prints hello user where user is the current linux user
export PATH=$PATH:/action
echo $((`echo $PATH|grep -o ":/"|wc -l`+1)):counts the number of Directories in PATH
printev:lists environment variables
set: lists all local variables and environment variables and functions
BEST="School":creates a local variable 
export BEST="School": creates a global variable
echo $(($TRUEKNOWLEDGE+128)):adds 128 to the value of TRUEKNOWLEDGE and prints the answer
echo $((POWER/DIVIDE)): prints the results of POWER/DIVIDE
echo $((BREATH**LOVE)):displays the result of BREATH to the power LOVE
printf "%d\n" "((2#$BINARY))": converts binary to decimal
echo {a..z}{a..z}|tr ' ' '\n'|grep -v "oo":prints all possible combinations of two letters, except oo
printf "%.2f\n" $NUM:prints anumber with two decimal places followed by a new line
