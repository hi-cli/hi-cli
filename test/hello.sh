#/usr/bin/env bash

echo "working directory: $PWD"
source "${HI_CLI_HOME}/test/external.sh"

function main()
{
    a=1
    b=2
    echo "hello world $((a + b))"
    ret_val=$(external_fucntion)
    echo "call ${ret_val}" 
    echo "end" 
}
main