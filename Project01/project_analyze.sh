#!/bin/bash


select choice in "extensionCount" "deletingTmpFiles" "mergeLog" "compileErrorLog" "deleteEmptyFile" "exitTheScript"; do
case "$choice" in
     extensionCount) echo "$choice"; find ~/CS1XA3 -type f | sed -e 's/.*\.//' | sort | uniq -c | sort -n | grep -Ei '(sh|py|html|hs|js|css)$'
     break;;
     deletingTmpFiles) echo "$choice"; git ls-files ~/CS1XA3 --exclude-standard --others | grep '\.tmp$' | xargs git rm
     break;;
     mergeLog) echo "$choice" ;  git log --oneline --merges | cut -d '' -f 1 | tee  merge.log
     break;;
     compileErrorLog) echo "$choice"; for i in `find ~/CS1XA3 -name '*.py' -or -name '*.hs'`  ; do
                                          if $i ; then
                                          true

                                          else
                                               if [[ -e "compile_fail.log" ]];then
                                               echo "$i" >> compile_fail.log
                                               fi
                                          fi
                                      done
     break;;
     deleteEmptyFile) echo "$choice" ; find ~/CS1XA3 -name "*.py" -type f -delete
     break;;
     exitTheScript) exit
esac
done
