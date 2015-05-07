#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main( int argc, char *argv[] ){
	int ret_code;
   if( argc == 3 ){
      printf("The first argument is %s\nThe second argument is %s\n", argv[1], argv[2]);
      int changed_num = (int) strtol(argv[2], (char **)NULL, 10);
	  printf("%d\n", changed_num);
      ret_code = system("echo \"C can be a pain, daww!\"");
      printf("%s\n", getenv("SAFHTTPATT"));
   }
   else if( argc > 2 ){
      printf("Too many arguments supplied.\n");
   }
   else{
      printf("Two arguments expected.\n");
   }
   return 0;
}