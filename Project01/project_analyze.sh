
#!/bin/bash

cd ..

select choice in "extensionCount" "deletingTmpFiles"; do
case "$choice" in
     extensionCount) echo "$choice"; find ~/CS1XA3 -type f | sed -e 's/.*\.//' | sort | uniq -c | sort -n | grep -Ei '(sh|py|html|hs|js|css)$'
     break;;
    deletingTmpFiles) echo "$choice"; git ls-files . --exclude-standard --others | grep '\.tmp$' | xargs git rm
    break;;
esac
done


