#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
/**
 * infinite_while - loops the program inifinately
 *
 * Return: returns exit status
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates 5 zombie processes
 *
 * Return: 0 on success
 */
int main(void)
{
	int child_pid;
	int i;
	int ret;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	ret = infinite_while();
	return (ret);
}
