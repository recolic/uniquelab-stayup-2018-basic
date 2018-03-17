#!/usr/bin/fish

function give_chance
    iptables -D INPUT -p tcp -m tcp --dport 25565 -j DROP
    echo 'window begin'
    sleep (random choice 0.25 0.28 0.3 0.33 0.36 0.4 0.45)
    iptables -A INPUT -p tcp -m tcp --dport 25565 -j DROP
    echo 'window end'
end

function _clean_up
    iptables -D INPUT -p tcp -m tcp --dport 25565 -j DROP
end

echo 'Don"t forget to check if iptables record is cleared!'
trap _clean_up SIGINT
_clean_up
iptables -A INPUT -p tcp -m tcp --dport 25565 -j DROP
while true
    sleep (random 20 40)
    #sleep 1
    give_chance
end

