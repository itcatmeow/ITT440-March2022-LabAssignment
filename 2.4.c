#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void childTask(){
        char name[20];
        printf("Please enter your name:");
        scanf("%s", name);
        printf("Your name is %s\n", name);
}
void parentTask(){
        printf("Job is done");
}

int main()
{
        for(int i=0; i<4; i++)  {
                pid_t pid = fork();
                if (pid == 0){
                        childTask();
                }
                else {
                        parentTask();
                        wait(NULL);
                        exit(0);
                }
        }

        return EXIT_SUCCESS;
}
