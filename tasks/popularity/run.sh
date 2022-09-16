#!/bin/bash
VERBOSE=$1
TIMELIMIT=2s
mkfifo iopipe0 iopipe1

if [[ $VERBOSE ]]
then
    timeout $TIMELIMIT <iopipe0 java -classpath solutions Popular | tee iopipe1 & <iopipe1 python3 tasks/popularity/run.py | tee iopipe0;
else
    timeout $TIMELIMIT <iopipe0 java -classpath solutions Popularity | python3 tasks/popularity/run.py > iopipe0;
fi
PASS=$?

rm iopipe0 iopipe1
exit $PASS
