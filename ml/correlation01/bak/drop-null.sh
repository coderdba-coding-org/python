#file1=databufferhit.txt
#file2=datacellread.txt

file1=datalogsync.txt
file2=datasqlexec1.txt

file1out=${file1}.noNull
file2out=${file2}.noNull

> $file1out
> $file2out

paste -d, $file1 $file2 | while read line
do
   if !(echo $line | grep "null")
   then
        echo $line | cut -d, -f1 >> $file1out
        echo $line | cut -d, -f2 >> $file2out
   fi
done


