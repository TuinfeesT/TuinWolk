#!/usr/bin/env sh
grep --color=always -H -n -R "TODO" * | grep -v "todo.sh"
