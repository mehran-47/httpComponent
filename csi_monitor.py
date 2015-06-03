#!/usr/bin/env python3
from subprocess import call
from multiprocessing import Process
import os, time

if __name__ == '__main__':
    pidTokill, component_pid, http_pid = (-1, -1, -1)
    if os.path.exists('/opt/SA_stats/csi_monitor'):
        print('CSI monitor is already running')
        with open('/opt/SA_stats/csi_monitor') as cm: pidTokill = str(cm.read()).rsplit('\n')[0]        
        call(['kill', '-9', pidTokill])
    component_name = str(os.environ.get('SA_AMF_COMPONENT_NAME'))
    with open('/tmp/'+component_name+'.pid', 'r') as compPIDf : component_pid = str(compPIDf.readline())
    with open('/opt/SA_stats/pid', 'r') as pidf: http_pid = str(pidf.readline())
    with open('/opt/SA_stats/csi_monitor', 'w') as csiMf: csiMf.write(str(os.getpid()))
    component_pid = component_pid.rsplit('\n')[0]
    http_pid = http_pid.rsplit('\n')[0]
    try:
        while os.path.exists('/proc/'+component_pid):
            if os.path.exists('/tmp/csi_assigned') and not os.path.exists('/proc/'+http_pid):
                Process(target=call, args=(['/opt/httpComponent/start_http_sneaky'],)).start()
                time.sleep(1)
                with open('/opt/SA_stats/pid', 'r') as pidf: http_pid = str(pidf.readline())
            if not os.path.exists('/tmp/csi_assigned') and os.path.exists('/proc/'+http_pid):
                call(['/opt/httpComponent/end_http_sneaky'])
            time.sleep(3)
    except KeyboardInterrupt:
        os.remove('/opt/SA_stats/csi_monitor')