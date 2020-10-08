
#!/bin/sh

dt=`date`
echo $dt 


git add .
git commit -m "$dt commit"
git push origin master