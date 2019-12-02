# Play Movies As XScreensaver Screensavers

## xscreensaver-movies

This is a Python script that will play movie files as screensavers in 
xscreensaver.  The movies are played in random order and do not repeat
until all movies have been played.

To install on Fedora 30 Linux:
1. Make sure that you have the "mpv" package from [RPMFusion](https://rpmfusion.org/) installed.
2. Edit the `xscreensaver-movies` script file and set the list of file paths at the top of the script to the directories that contain the video clips you want to play.
3. Put the `xscreensaver-movies` script file in `/usr/libexec/xscreensaver/` and make sure it is executable.
4. Put `xscreensaver-movies.conf` in `/usr/share/xscreensaver/hacks.conf.d/` and make sure that it readable by all users.
5. Put `xscreensaver-movies.xml` in `/usr/share/xscreensaver/config/` and make sure that it readable by all users.
6. Become root and run the command `/usr/sbin/update-xscreensaver-hacks`.  If successful, this script will run without any output.
7. Configure your xscreensaver to use the "Play Movies" screensaver.
