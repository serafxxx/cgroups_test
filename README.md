# Cgroups test

Test project to demonstrate cgroups django module functionality

## Installation
Be sure to have python2.7 and virtualenv installed. `cgroups` under `/sys/fs`

    git clone ...
    cd cgroups_test

Create virtual environment for the project

    virtualenv venv

**Important!** From this point lets use root user to make things simple. Cgroups will allow not root user in case
corresponding user folders in `sys/fs/cgroup` already created. Not a big deal but don't think its
related to the test.

    sudo su   

Activate virtual environment

    source venv/bin/activate
    
Install dependencies

    pip install -R requirements.txt
    
Run tests
    
    python ./manage.py test
    
Start debug server 

    python manage.py runserver 0.0.0.0:8000

Now you can try it in your browser. 

## Troubleshooting
Server should be accessible via network. To find out its ip you can try

    ip addr
    
Then type its ip:8000 in the browser. If it still fails maybe you'll need to disable your default firewall

    systemctl disable firewalld

Doublecheck you're runnung your server as root. 


## In a wild
For the production will suggest to use nginx along with gunicorn and some supervisor. 
And need to do something with rights because its a bad idea to run server as root. Actually it depends on
how and where you're going to use that api.


## API usage

Create/list cgroup
 
    $ curl http://192.168.1.98:8000/cgapi/cgroups/gr1
    {"name":"gr1","cpu_limit":100,"memory_limit":8796093022207,"pids":[]}

Add process (by PID) into the group

    $ curl -X PUT http://192.168.1.98:8000/cgapi/cgroups/gr1/pids/12998
    {"name":"gr1","cpu_limit":100,"memory_limit":8796093022207,"pids":[12998]} 
