for sub in www mail ftp dev staging test api admin blog shop cdn app portal vpn autodiscover cpanel webmail
    set result (dig +short $sub.fifthace.net)
    if test -n "$result"
        echo "$sub.fifthace.net -> $result"
    end
end
