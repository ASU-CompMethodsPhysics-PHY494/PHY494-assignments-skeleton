#!/bin/bash
# Update the PHY 494 Assignment Repository with new
# homeworks and data.
#
# Oliver Beckstein 2016-2018 placed into the public domain

# With GitHub template repositories one needs to use --allow-unrelated-histories
# at least once. https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template

progname="$0"
REMOTE_NAME="skeleton"
REMOTE_URL="https://github.com/ASU-CompMethodsPhysics-PHY494/PHY494-assignments-skeleton.git"

function die () {
    local msg="$1" err=${2:-1}
    echo "ERROR: ${msg}"
    exit $err
}

# first time
# 1. set remote repo
# 2. merge histories between student (template) and remote skeleton

if ! git remote get-url ${NAME} >/dev/null 2>&1; then
    echo "Adding remote repository '${NAME}'."
    git remote add ${REMOTE_NAME} ${REMOTE_URL}

    echo "Merging histories for the first time..."
    git pull --allow-unrelated-histories ${REMOTE_NAME} master || \
	die "Failed to merge histories. Contact the instructor and TA with a screen shot of ALL output from running $0" $?
fi    
    

echo "updating repository... git pull from ${REMOTE_NAME}"
git pull ${REMOTE_NAME} master || die "Failed to pull from ${REMOTE_NAME}. Ask your instructor/TA for help."

topdir="$(git rev-parse --show-toplevel)" || die "Failed to get rootdir"
cd "${topdir}" || die "Failed to get to the git root dir ${rootdir}"

echo "creating subdirectories (if any are missing)"
for adir in assignment_[0-9][0-9] project_[1-9]; do
    test -d "${adir}" || continue
    for subdir in Grade Submission Work; do
	newdir="${adir}/${subdir}"
	test -d "${newdir}" || \
	    { mkdir "${newdir}" && echo "created ${newdir}"; }
    done    
done

