script=$0
folder=$1
logfile=${script}.out.${folder}

dropnull(){
     file1=$1
     file2=$2
     file1out=${file1}.noNull
     file2out=${file2}.noNull
     
     > $file1out
     > $file2out
     
     paste -d, $file1 $file2 | while read line
     do
        if !(echo $line | grep "null") > /dev/null 2>> /dev/null
        then
             echo $line | cut -d, -f1 >> $file1out
             echo $line | cut -d, -f2 >> $file2out
        fi
     done
}

if [ $# -lt 1 ]
then
     echo 
     echo "Usage:" $0 "data-file-folder-name"
     echo
     exit 1
fi

exec > $logfile 2>> $logfile

echo "==========================================="
echo "DB RT vs SQL Exec Time"
echo "==========================================="
file1=$folder/datadbrt.txt
file2=$folder/datasqlexec1.txt
dropnull $file1 $file2
covar01.py --xfile ${file1}.noNull --yfile ${file2}.noNull

echo
echo "==========================================="
echo "Log Synch vs SQL Exec Time"
echo "==========================================="
file1=$folder/datalogsync.txt
file2=$folder/datasqlexec1.txt
dropnull $file1 $file2
covar01.py --xfile ${file1}.noNull --yfile ${file2}.noNull

echo
echo "==========================================="
echo "Cell Read vs SQL Exec Time"
echo "==========================================="
file1=$folder/datacellread.txt
file2=$folder/datasqlexec1.txt
dropnull $file1 $file2
covar01.py --xfile ${file1}.noNull --yfile ${file2}.noNull

echo
echo "==========================================="
echo "Process Limit vs SQL Exec Time"
echo "==========================================="
file1=$folder/dataprocesslimit.txt
file2=$folder/datasqlexec1.txt
dropnull $file1 $file2
covar01.py --xfile ${file1}.noNull --yfile ${file2}.noNull

echo
echo "==========================================="
echo "Buffer Hit vs SQL Exec Time"
echo "==========================================="
file1=$folder/databufferhit.txt
file2=$folder/datasqlexec1.txt
dropnull $file1 $file2
covar01.py --xfile ${file1}.noNull --yfile ${file2}.noNull

# SYNTAX
#exec > $logfile 2>> $logfile
#covar01.py --xfile $folder/datadbrt.txt --yfile $folder/datasqlexec1.txt
#covar01.py --xfile $folder/datalogsync.txt --yfile $folder/datasqlexec1.txt
#covar01.py --xfile $folder/datacellread.txt --yfile $folder/datasqlexec1.txt
#covar01.py --xfile $folder/dataprocesslimit.txt --yfile $folder/datasqlexec1.txt
#covar01.py --xfile $folder/databufferhit.txt --yfile $folder/datasqlexec1.txt
