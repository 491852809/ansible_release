#!/bin/bash
grep "#Record history operation" /etc/profile
if [ $? -eq 1 ];then
cat>> /etc/profile <<'EOF'
#Record history operation
USER_IP=`who -u am i 2>/dev/null |awk '{print $NF}' |sed -e 's/[()]//g'`
LOGNAME=`who -u am i |awk '{print (}'`
HISTDIR=~/.history
if [ -z $USER_IP ]
then
       USER_IP=`hostname`
   fi
   
   if [ ! -d $HISTDIR ]
   then
           mkdir -p $HISTDIR
               chmod 755 $HISTDIR
           fi
           
           if [ ! -d $HISTDIR/${LOGNAME} ]
           then
                   mkdir -p $HISTDIR/${LOGNAME}
                       chmod 750 $HISTDIR/${LOGNAME}
                   fi
                   
                   export HISTSIZE=100000
                   
                   DT=`date +"%Y%m"`
                   export HISTFILE="$HISTDIR/${LOGNAME}/${USER_IP}.history.$DT"
                   export HISTTIMEFORMAT="[%Y.%m.%d %H:%M:%S]"
                   chmod 600 $HISTDIR/${LOGNAME}/*.history* 2>/dev/null)
EOF
else
echo "Record history operation is OK"
fi
