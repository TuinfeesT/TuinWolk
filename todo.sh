#!/usr/bin/env sh
grep --color=always -H -n -R -E "TODO|XXX|FIXME" * | grep -v "todo.sh"
