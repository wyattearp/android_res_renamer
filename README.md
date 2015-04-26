# android_res_renamer
A simple res file renamer for android projects. I built this because I grew tired of manually renaming every stupid file I ever had to download as a package from the various sites that will build icon/img files of the associated resolutions and provide them to you in a zip ... but not allow you to change the name.

Additionally, there are a terrible questions like this on [stackoverflow](http://stackoverflow.com/questions/28405152/rename-multiple-res-drawable-png-files-in-eclipse) ... and I just couldn't let that stand with use the old ```mc``` tool, especially in the new days of git repos. Why this isn't part of Android Studio or any other IDE is beyond me or it took more than 10 minutes to find (the approximate time it took to write this tool).

Usage
=====
This tool assumes that you have some sort of ```<app_src_dir>/res/*``` structure setup (like you get from most zip files) and will recurse and rename the associated files. If you're working in an existing application, you can specify the directory path to the app/src/<product> directory and it will do the same thing. If you want to use a ```git mv``` command so that you can basically rename something "safely" within an IDE, you can pass the ```-g``` flag to change from the standard ```mv <old> <new>```.

As with anything, your mileage may certainly vary.
