# Play Movies As XScreensaver Screen Saver

## xscreensaver-movies

This is a Python script that will play video files as a screen saver in 
xscreensaver.  The videos are played in random order and do not repeat
until all pf the files have been played.

File types supported: .mov .mp4 .mkv .mpg .avi

RPM package files are provided on the [releases page](https://github.com/dlk3/xscreensaver-movies/releases) in this repository.

To install manually on Fedora 30 Linux:
1. Make sure that you have the "mpv" package from [RPMFusion](https://rpmfusion.org/) installed.
3. Put the `xscreensaver-movies` script file in `/usr/libexec/xscreensaver/` and make sure it is executable.
4. Put `xscreensaver-movies.conf` in `/usr/share/xscreensaver/hacks.conf.d/` and make sure that it is readable by all users.
5. Put `xscreensaver-movies.xml` in `/usr/share/xscreensaver/config/` and make sure that it is readable by all users.
6. Become root and run the command `/usr/sbin/update-xscreensaver-hacks`.  If successful, this script will run without any output.
7. Configure xscreensaver to use the `Play Movies` screen saver.  Set the list of file paths that contain the video files you want to play in the `Settings` for the `Play Movies` screen saver.  (The `xscreensaver` application on Fedora 30 provides the configuration GUI.  From the command line the command that runs this GUI is `xscreensaver-demo`.)
