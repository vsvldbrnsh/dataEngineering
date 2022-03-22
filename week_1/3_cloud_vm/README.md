

1. Generate ssh key (https://cloud.google.com/compute/docs/connect/create-ssh-keys):
   * ssh-keygen -t rsa -f gpc -C vsvld -b 2048
2. add it Computer Engine -> Metadata -> SSH KEYS
3. create a VM intance in GCS account:
   * Computer Engine -> VM Instances -> Create an instance
4. instance:start
5. connect via ssh to instance:
   * ssh -i ~/.ssh/gpc vsvld@34.116.197.153  
6. instance:
   * download anaconda (wget from source)
   * sudo apt-get update
   * sudo apt-get install docker.io
7. create a config file in ~/.ssh/
   * cd ~/.ssh/
   * touch config
   * vim config -> fulfill the file (Host de-cz)
8. ssh de-zc
9. instance: