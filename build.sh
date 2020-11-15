
#!/bin/sh

content=$1

dt=`date`
echo $dt 


git add .
git commit -m "$dt commit $content"
git push origin master
