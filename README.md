# Assignments for PHY494


Submission of homework is now to your *private GitHub
repository*. Follow the link provided to you by the instructor in
order for the repository to be set up: It will have the name
*ASU-CompMethodsPhysics-PHY494/assignments-2019-YourGitHubUsername*
and will only be visible to you and the instructor/TA. Follow the
instructions below to submit homework.

`git clone` your assignment repository (you only need to do this once)
and run the script `scripts/update.sh` (replace `YourGitHubUsername`
with your GitHub username):
```
repo="assignments-2019-YourGitHubUsername"
git clone https://github.com/ASU-CompMethodsPhysics-PHY494/${repo}.git
cd ${repo}
bash ./scripts/update.sh 
```

New homework assignments will be added during the semester. Run
`update.sh` to get a new assignment:
```
repo="assignments-2019-YourGitHubUsername"
cd ${repo}
bash ./scripts/update.sh 
```

For each `assignment_NN` the script should create three subdirectories
`assignment_??/Submission`, `assignment_??/Grade`, and
`assignment_??/Work`. (If the script fails, file an issue in the
[Issue Tracker for
PHY494-assignments-skeleton](https://github.com/ASU-CompMethodsPhysics-PHY494/PHY494-assignments-skeleton/issues)
and just create the directories manually.

* The **Submission** directory will contain **your homework**.
* The **Grade** directory will contain comments from the
  TA/instructor.
* You can use the **Work** directory to store scratch files and
  alternative attempts that should not be graded.

Commit and push a PDF, text file or Jupyter notebook inside the
**`assignment_NN/Submission`** directory and **name it `hwNN.ipynb`
(or `hwNN.pdf`)** (where *NN* is the assignment number).  Follow the
instructions in each assignment. Homeworks must be submitted according
to the above scheme, be legible and intelligible, and on time (commit
date) or may be returned ungraded with 0 points.

* There is also a **tex** directory: it is not relevant for your
  homework because it contains the
  [LaTeX](https://www.latex-project.org/) sources that were used to
  create the assignment PDF file. You may use it to typeset your
  answer if you like, but you are *not required* to do so.



