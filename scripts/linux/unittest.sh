RUNDIR=`pwd`
cd `dirname $0`
MYDIR=`pwd`
ROOT=${MYDIR}/../..
ENV=.env.36
TEST=${ROOT}/test
FILES="ut_tredge.py"
cd ${ROOT}
for FILE in ${FILES}
do
    echo Running ${FILE}
    ${ROOT}/${ENV}/bin/python3 ${TEST}/${FILE} -b
done
cd ${RUNDIR}
