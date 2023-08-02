# Task 2 Bash

## script:
```
!/bin/bash

function CheckError(){
if (($?==0)); then
echo "successfull command"
else
echo "error in $1 file"
fi
}

function CreateLogs(){
ps -f -u > ./process.log 2> ./process.error
CheckError process.error

free -h > ./memory.log 2> ./memory.error
CheckError memory.error

df -h | awk '{print $1,$5,$6}' > ./disk.log 2> ./disk.error
CheckError disk.error
}

function CompressFiles(){
if [[ -f process.log && -f memory.log && -f disk.log && -f /var/log/dmesg ]]; then
echo "files existed"
tar -czvf logs.tar.gz process.log memory.log disk.log /var/log/dmesg
echo "files compressed"
else
CheckError /var/log/dmesg
fi
}

function Send(){ 
read -p "enter username: " user_name
read -p "enter ip: " ip
read -p "enter path: " path
rsync -avz --ignore-existing logs.tar.gz $user_name@$ip:$path
echo "the file has been sent"
}

#call functions
CreateLogs
CompressFiles
Send
```
