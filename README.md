# Play Movies As XScreensaver Screensavers

## xscreensaver-movies

This is a Python script that will play movie files as screensavers in 
xscreensaver.  The movies are played in random order and do not repeat
until all movies have been played.

To install on Fedora 30 Linux:
1. Make sure that you have the "mpv" package from [RPMFusion](https://rpmfusion.org/) installed
2. Put the xscreensaver-movies script file in /usr/libexec/xscreensaver/ and make sure it is executable
3. Put the paths containing the movies you want to use into the "movie_paths" array variable in the xscreensaver-movies script file
4. Edit the ~/.xscreensaver file and add the following line at the end of the "programs:" list found in that file:<br />`"Play My Movies" xscreensaver-movies \n\`
5. Configure your xscreensaver to use the "Play My Movies" screensaver
