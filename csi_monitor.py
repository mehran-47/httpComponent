#!/usr/bin/env python3
from subprocess import call
import os, time

if __name__ == '__main__':
    component_name = str(os.environ.get('SA_AMF_COMPONENT_NAME'))
    component_pid = -1
    http_pid = -1
    with open('/tmp/'+component_name+'.pid', 'r') as compPIDf : component_pid = compPIDf.read()
    with open('/opt/SA_stats/pid', 'r') as pidf: component_pid = pidf.read()
    while os.path.exists('/proc/'+component_pid):
        if os.path.exists('/tmp/csi_assigned') and not os.path.exists('/proc/'+http_pid):
            call(['/opt/httpComponent/start_http_sneaky','&'])
        elif not os.path.exists('/tmp/csi_assigned') and os.path.exists('/proc/'+http_pid):
            call(['/opt/httpComponent/end_http_sneaky','&'])
        time.sleep(3)