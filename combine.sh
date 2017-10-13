#!/bin/bash                                                                                                  #
# File: combine.sh                                                                                           #
# Author: Maggie Schweihs                                                                                    #
# Class: DS730, Fall 2017                                                                                    #      
# Purpose: After running a MapReduce job in the cloud (AWS), we are left with multiple part-##### files.     #
# This script is designed to run after the AWS S3 bucket is synced to an empty folder on a Linux machine     #
# (Ubuntu Server 16.04 LTS)                                                                                  #
# For Info on AWS S3 Sync utility: http://docs.aws.amazon.com/cli/latest/reference/s3/sync.html              #                                                                                #
#                                                                                                            #
# Caveat: Only the part-##### files from one job should be in the folder. Files other than part-##### are ok.#
# Create a new folder for each job!                                                                          #
#                                                                                                            #
# Usage: Specify all options -d <directory> -o <output_dir> -f <filename>                                    #
# where -d is the directory containing the part-##### files,                                                 #
# -o is the directory to contain the output file,                                                            #
# and -f is the filename of the output file.                                                                 #
############################################################################################################## 

usage ()
{
  echo ''
  echo 'Usage : Script -d <directory> -o <output_dir> -f <filename>i -h <help>'
  echo ''
  echo 'Please enter the directory in which the files are located, the output directory '
  echo 'and the filename of the output file.'
  exit
}

#-d, -o, -f are required, h is optional
while getopts ":d:o:f:h" opt; do
    case "$opt" in 
        d )            #specify directory of files to combine
                       DIRECTORY=${OPTARG}
                       if [[ "$DIRECTORY" = "" ]]; then
                       echo "Please enter the directory containing part* files"
                       usage
                       exit 0
                       fi
                       ;;
        o )            #specify output directory
                       OUTDIR=${OPTARG}
		                   if [[ "$OUTDIR" = "" ]]; then
                       echo "Please enter the output directory."
                       usage
                       exit 0
                       fi
                       ;;
        f )            #specify output filename
                       FILENAME=${OPTARG}
                       if [[ "$FILENAME" = "" ]]; then
                       echo "Please enter a filename."                       
                       usage
                       exit 0
                       fi
                       ;;
         h | * )      #display help
                       usage
                       exit 0
                       ;; 
    esac
done
#do work
cat $DIRECTORY/part* > $OUTDIR/$FILENAME
#human-like sort
sort -g $OUTDIR/$FILENAME -o $OUTDIR/$FILENAME
#Check if the file exists!
if [ -s $OUTDIR/$FILENAME ]; then
    echo "File created: $OUTDIR/$FILENAME"
elif ![ -s $OUTDIR/$FILENAME ]; then
    echo "Something went wrong!"
fi 
exit