# Assignments for PHY494


Submission of homework is now to your *private GitHub
repository*. Follow the link provided to you by the instructor in
order for the repository to be set up: It will have the name
*ASU-CompMethodsPhysics-PHY494/assignments-2017-YourGitHubUsername*
and will only be visible to you and the instructor/TA. Follow the
instructions below to submit homework.

`git clone` your assignment repository (you only need to do this once)
and run the script `scripts/update.sh` (replace `YourGitHubUsername`
with your GitHub username):
```
repo="assignments-2017-YourGitHubUsername"
git clone https://github.com/ASU-CompMethodsPhysics-PHY494/${repo}.git
cd ${repo}
bash ./scripts/update.sh 
```

For each `assignment_NN` it should create three subdirectories
`assignment_??/Submission`, `assignment_??/Grade`, and
`assignment_??/Work`. (If the script fails, file an issue in the
[Issue Tracker for PHY494-assignments-skeleton](https://github.com/ASU-CompMethodsPhysics-PHY494/PHY494-assignments-skeleton/issues)
and just create the directories manually.

* The **Submission** directory will contain your homework.
* The **Grade** directory will contain comments from the
  TA/instructor.
* You can use the **Work** directory to store scratch files and
  alternative attempts that should not be graded.

Commit and push a PDF, text file or Jupyter notebook inside the
**`assignment_NN/Submission`** directory and **name it `hwNN.ipynb` (or
`hwNN.pdf`)** (where *NN* is the assignment number).  Homeworks must
be submitted according to the above scheme, be legible and
intelligible or may otherwise be returned ungraded with 0 points.



