#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main (int argc, char * argv[]){ 
 
    pid_t pid; 
    pid = fork(); 
 
    if (pid<0){ 
        fprintf (stderr,"Il y a une erreur \n"); 
        exit(EXIT_FAILURE); 
    } 
    else if (pid == 0){ 
     printf("Je suis le fils, mon pid est: %d, celui de mon père: %d \n",getpid(), getppid()); 
        exit(EXIT_SUCCESS); 
    } 
    else { 
        printf("Je suis le père, mon pid est: %d, celui de mon fils: %d \n",getpid(), pid); 
        int fin = wait(0); 
        printf ("Mon fils se termine: son pid %d \n",fin); 
        exit (EXIT_SUCCESS); 
    }
}
