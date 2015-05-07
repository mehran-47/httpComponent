#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <lttng/tracef.h>

int main( int argc, char *argv[] ){
	int ret_code, component_module_pid=0;
   if( argc == 3 ){
      //printf("The first argument is %s\nThe second argument is %s\n", argv[1], argv[2]);
      int changed_num = (int) strtol(argv[2], (char **)NULL, 10);
	  printf("%d\n", changed_num);
      //printf("CSI name: %s\nComponent name:%s\n", getenv("SAFHTTPATT"), getenv("SA_AMF_COMPONENT_NAME"));
      FILE *fp = popen("/opt/httpComponent/simple_http.py 8080 &", "r");
      //fscanf(fp, "%d", &component_module_pid);
      //pclose(fp);
      printf("component_module_pid : %d\n", component_module_pid);
      tracef("{'type':'csi_assignment', 'CSI':'%s', 'component':'%s' , 'HAState':'Active', 'PID':%d}", getenv("SAFHTTPATT"), getenv("SA_AMF_COMPONENT_NAME"), component_module_pid);
   }
   else if( argc > 2 ){
      printf("Too many arguments supplied.\n");
   }
   else{
      printf("Two arguments expected.\n");
   }
   return 0;
}