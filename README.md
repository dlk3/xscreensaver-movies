# Play Movies As XScreensaver Screen Saver

## xscreensaver-movies

This is a Python script that will play video files as a screen saver in 
xscreensaver.  The videos are played in random order and do not repeat
until all pf the files have been played.

File types supported: .mov .mp4 .mkv .mpg .avi

RPM package files are provided on the [releases page](https://github.com/dlk3/xscreensaver-movies/releases) in this repository.

After installing the RPM you must configure xscreensaver to use the "Play Movies" screen saver and set the path where the movies can be found.  That path is a comma-seperated list of directories set in the "Settings" of the "Play Movies" screen saver.  Be careful.  Due to the way that the xscreensaver application stories parameters, a long list of directories can be mangled to the point where it doesn't work properly.  To prevent this make sure that the list of directories contains no spaces, i.e., `/Videos/directory1,/directory2,/video_directury`
