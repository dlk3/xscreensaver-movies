# Play Movies As XScreensaver Screensavers

## xscreensaver-movies

This is a Python script that will play movie files as screensavers in 
xscreensaver.  The movies are played in random order and do not repeat
until all movies have been played.

To install on Fedora 30 Linux:
#Make sure that you have the "mpv" package from [RPMFusion](https://rpmfusion.org/) installed
#Put this the xscreensaver-movies script file in /usr/local/libexec/xscreensaver/
#Put the paths containing the movies you want to use into the "movie_paths" variable in the xscreensaver-,ovies script file
#Edit the ~/.xscreensaver file and add the following line at the end of the "programs:" list found in that file:
#:`"Play My Movies" xscreensaver-movies \n\`
#Configure your xscreensaver to use the "Play My Movies" screensaver
