#!/usr/bin/env python

import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Mass res file renamer for android projects, your success may vary")
    parser.add_argument('--path', required=False, help="the path to the android project if not in the current working directory, recommending this should be run at the lowest level (app/src/main)")
    parser.add_argument('--old', '-o', required=True, help="the name of the res file (such as 'ic_action.png' to rename")
    parser.add_argument('--new', '-n', required=True, help="the NEW name of the res file")
    parser.add_argument('--git', '-g', required=False, help="rename file with git (default action is `mv <old> <new>`)", action='store_true', dest='use_git')

    args = parser.parse_args()
    #print(args)

    search_path = "."
    old_file = args.old
    new_file = args.new

    if args.path:
        search_path = args.path

    for dir_name, sub_dir_list, file_list in os.walk(search_path):
        if dir_name.find('res') > -1:
            #print("Found res directory of %s") % dir_name
            for f in file_list:
                if f == old_file:
                    cmd = []
                    if args.use_git:
                        cmd.append("git")
                        cmd.append("mv")
                    else:
                        cmd.append("mv")
                    cmd.append(os.path.join(dir_name, old_file))
                    cmd.append(os.path.join(dir_name, new_file))

                    result = subprocess.call(cmd)
                    if result == 0:
                        print("Renamed\n\t%s => %s") % (os.path.join(dir_name, old_file), os.path.join(dir_name, new_file))
                    else:
                        print("FAILURE!!!\n\t%s => %s") % (os.path.join(dir_name, old_file), os.path.join(dir_name, new_file))
                        sys.exit(-1)


if __name__ == "__main__":
    main()
