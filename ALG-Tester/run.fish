#!/usr/bin/fish

set range 4
set round 1024

function do_a_test
    # not process safe!
    set size $argv[1]
    #    echo "Testing for size = $size." > /dev/fd/2
    ./makedata --size $size | grep '[0-9]' > data.tmp
    set answer (awk 'NR==3' data.tmp)
    set challenge (./tested < data.tmp | tee /tmp/.r.stdout | grep '[0-9]')
    set ret $status

    if test $ret != 0
        set stdout (cat /tmp/.r.stdout)
        echo "Error occurred with stdout `$stdout`."
        exit 2
    end
    
    echo "$challenge/$answer"
end

for _ in (seq $round)
    for i in (seq $range)
        do_a_test $i
        # Beaten wmy used srand(time()) so I have to wait
        sleep 0.05
    end
end

rm -f data.tmp
