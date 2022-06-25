#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<unistd.h>

int getPIN() {
        srand(getpid() + getppid());
        int secret;
        printf("Enter a Number: ");
        scanf("%d", &secret);
        return secret;
}

int main(void) {
        int fd[2];
        int temp = 0;
        pipe(fd);
        pid_t pid = fork();

        void sigint_handler(int sig);

        if (signal(SIGINT, sigint_handler) == SIG_ERR)
        {
                perror("signal");
                exit(1);
        }

        if(pid > 0) {
                close(fd[1]);
                dup(fd[0]);

                int secretNumber;
                size_t readBytes = read(fd[0], &secretNumber, sizeof(secretNumber));

                printf("Resolving...\n");
                wait(NULL);
                printf("Number: %d\n", secretNumber);

                for (int i = 1; i <=secretNumber; i++)
                {
                        if (secretNumber % i == 0)
                        {
                                temp++;
                        }
                }
                if (temp == 2)
                {
                        printf("It is a prime number\n");
                }
                else
                {
                        printf("It is not a prime number\n");
                }
        }
        else if (pid == 0) {
                close(fd[0]);
                dup(fd[1]);

                int secret = getPIN();
                write(fd[1], &secret, sizeof(secret));
                exit(EXIT_SUCCESS);
        }

        return EXIT_SUCCESS;

}

void sigint_handler(int sig)
{
      printf("Interrupted");
}

