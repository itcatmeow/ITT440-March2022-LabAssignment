#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

void func(int socket_desc)
{
        char buffer[1024];
        int n;
        for (;;)
        {
                bzero(buffer, sizeof(buffer));
                printf("Send to server: ");
                n=0;
                while ((buffer[n++] = getchar()) != '\n');
                write(socket_desc, buffer, sizeof(buffer));
                bzero(buffer, sizeof(buffer));
                read(socket_desc, buffer, sizeof(buffer));
                printf("\nServer says: %s", buffer);
        }
}
int main(int argc, char *argv[])
{
        int socket_desc;
        struct sockaddr_in server;
        char *message, server_reply[2000];


        socket_desc = socket(AF_INET, SOCK_STREAM, 0);
        if(socket_desc == -1)
        {
                printf("Could not create socket");
        }

        server.sin_addr.s_addr =inet_addr("192.168.56.105");
        server.sin_family = AF_INET;
        server.sin_port = htons(8888);

        if(connect(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0)
        {
                puts("connect error");
                return 1;
        }

        puts("Connected");

        func(socket_desc);
        close(socket_desc);
        return 0;
}

