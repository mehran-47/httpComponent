#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <lttng/tracef.h>

int main( int argc, char *argv[] ){
    if( argc == 3 ){
        int component_module_pid = (int) strtol(argv[1], (char **)NULL, 10);
        int type_num = (int) strtol(argv[2], (char **)NULL, 10);
        if(type_num){
                tracef("{'type':'csi_assignment', 'CSI':'%s', 'component':'%s' , 'HAState':'Active', 'PID':%d}", getenv("SAFHTTPATT"), getenv("SA_AMF_COMPONENT_NAME"), component_module_pid);
                printf("{'type':'csi_assignment', 'CSI':'%s', 'component':'%s' , 'HAState':'Active', 'PID':%d}\n", getenv("SAFHTTPATT"), getenv("SA_AMF_COMPONENT_NAME"), component_module_pid);
            }else{
                tracef("{'type':'dispatch_remove', 'CSI':'%s', 'component':'%s' , 'HAState':'Active', 'PID':%d}", getenv("SAFHTTPATT"), getenv("SA_AMF_COMPONENT_NAME"), component_module_pid);
                printf("{'type':'dispatch_remove', 'CSI':'%s', 'component':'%s' , 'HAState':'Active', 'PID':%d}\n", getenv("SAFHTTPATT"), getenv("SA_AMF_COMPONENT_NAME"), component_module_pid);
            }
    }else{
        printf("usage: 'send_trace.o <PID> <type>'\n");
    }
    return 0;
}

/*
1 : csi_assignment
0 : dispatch_remove
*/