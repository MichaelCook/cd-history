cd-history
==========

Maintain a history of directories we've cd'ed into.

Like the command history of many shells but for tracks the directories we've
visited.

Add to your ~/.bashrc, for example:

   cd () { local cmd; cmd="$(cd-history "$@")" || return; eval "$cmd"; }
   cdh () { cd-history --list | less -S +G "$@"; }

Then use "cd" as you would normally, plus:

* `cdh` - See the list of directories in your history.

* `cd %foo` - change to a directory in your history ending with "foo".
There must be exactly one match.  If there are more than one match, you'll be
shown a list of the matches.

* `cd %foo%` - change to a diretory containing "foo" anywhere in the pathname.

* `cd 4` - change to directory number 4.

* `cd -4` - change to the 4th directory from the bottom of the list.

* `cd -` - same as `cd -1`.  Any number of dashes may be given to indicate how
many directories back.  `cd ----` is the same as `cd -4`.

* `cd` - change to $HOME.
