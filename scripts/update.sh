#!/bin/bash
# Update the PHY 494 Assignment Repository with new
# homeworks and data.
#
# Oliver Beckstein 2016, placed into the public domain

progname="$0"

function die () {
    local msg="$1" err=${2:-1}
    echo "ERROR: ${msg}"
    exit $err
}

echo "updating repository... git pull"
git pull

topdir="$(git rev-parse --show-toplevel)" || die "Failed to get rootdir"
cd "${topdir}" || die "Failed to get to the git root dir ${rootdir}"

echo "creating subdirectories (if any are missing)"
for adir in assignment_[0-9][0-9]; do
    for subdir in Grade Submission Work; do
	newdir="${adir}/${subdir}"
	test -d "${newdir}" || \
	    { mkdir "${newdir}" && echo "created ${newdir}"; }
    done    
done

