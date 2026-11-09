# Anna: start here

This is a practice repository. Nothing here affects the real project, so try every button.

Your job in Homeroom is to be the teacher who approves new courses. Homeroom proposes a course, a reviewer called Gitar checks its format, and **you decide whether it goes in**. You never have to use AI. Gitar's comment is a checklist you can read or skip.

You do everything in your web browser on github.com. You don't need to install anything.

## Step 1: Accept the invitation (2 minutes)

1. Sign in at https://github.com with your account (`aelinkowski9`).
2. Open https://github.com/jrwhite00/cnh-dryrun/invitations and click **Accept invitation**. You can also click the button in the email from GitHub.
3. If GitHub asks you to set up two-factor authentication, do it with your phone. It takes about 5 minutes.
4. Come back to https://github.com/jrwhite00/cnh-dryrun. You'll see a list of files, including this one. That means it worked.

## Words you'll see

| Word | What it means |
|---|---|
| Repository, or repo | The project's folder on GitHub. Ours holds the app and your concept table. |
| Pull request | A proposed change that waits for approval. Nothing changes until someone presses Merge. |
| Gitar | A reviewer that reads each pull request and leaves a comment. It never edits course files or merges. |
| Topic | Gitar's word for a concept in your table, such as containers. Same thing. |
| Approve | Your sign-off that the change is right. |
| Merge | Puts the change into the project. Homeroom uses it from then on. |
| Branch | A side copy where a proposed change waits. You can ignore branches. |

## What the files look like

Everything you'll work on is in the `curriculum` folder. Open it and look around. `curriculum/README.md` explains the layout.

Each **course** is one short file:

```
course: Computer Science I
state: Texas
standard: Texas TEKS, Computer Science I
teaches: programming-basics, data-and-databases
added by: Homeroom, after a student confirmed the match
```

- **course** and **state**: the class, as the student named it.
- **standard**: where the course comes from, such as a state standard.
- **teaches**: what a student knows after the course, at most 4 topics. Each must match a topic in the concept table, spelled the same way.
- **added by**: who proposed it.

Each **concept** is a file too:

```
concept: Containers
definition: A way to package a program with everything it needs so it runs the same on any computer.
technical words: Docker, container image, registry, container runtime
```

## Reviewing a course pull request

1. Click the **Pull requests** tab at the top of the repo, or open the link below.
2. Read the title. It names the course, for example "Add course: Computer Science I (Texas)".
3. On the **Conversation** tab, find Gitar's comment that starts **"This course looks ready…"** or **"This course is not ready…"**. That one is written for you. Gitar also posts a programmer-style review marked "Approved" or "Bug". Skip that one.
4. Click the **Files changed** tab to see the course file.
5. Ask the questions only a teacher can answer:
   - Does this course really teach each listed topic?
   - Is the standard right?
   - Is there anything about a real person? There never should be.
6. Decide, using one of the three paths below.
7. **Never tick an "Apply fix" box** in a Gitar comment. It fixes only part of the problem, and the decision is yours.

### If it looks right: approve, then merge

1. On **Files changed**, click the green **Review changes** button at the top right. It may say **Submit review** instead.
2. Choose **Approve**, write a short note such as "Checked against the concept table", and click **Submit review**.
3. Go back to **Conversation**, scroll down, click **Merge pull request**, then **Confirm merge**.

### If it needs a fix: edit, then approve

1. On **Files changed**, click the three dots on the file's header and choose **Edit file**.
2. Change the lines, for example remove a topic or fill in the standard.
3. Click **Commit changes…**, keep "Commit directly to the … branch", and click **Commit changes**.
4. Wait 2 to 3 minutes. Gitar checks the file again and posts a new comment.
5. Approve and merge, as above.

### If the match is wrong: close it

Click **Close pull request** at the bottom of **Conversation**, with a one-line comment saying why. Nothing changes.

## Adding a course by hand

Use this if the automatic pull requests aren't ready tomorrow. James will tell you.

1. Open the repo, then the `curriculum` folder, then `courses`.
2. Click **Add file**, then **Create new file**.
3. Name the file with the state and course in lowercase, joined by hyphens, ending in `.yaml`. For example: `utah-computer-programming-3.yaml`.
4. Type the five lines, following the example above, with `added by: Anna`.
5. Click **Commit changes…**, choose **Create a new branch for this commit and start a pull request**, then click **Propose changes**, then **Create pull request**.
6. Wait for Gitar's comment and fix anything it finds. GitHub won't let you approve your own pull request, so ask James to approve it, or merge it yourself.

## Practice now

19 practice pull requests are waiting. **Open [PRACTICE.md](PRACTICE.md) and work through it in order.** It takes about 1½ hours, in four rounds:

1. Warm-up: correct courses to approve and merge.
2. Gitar finds a problem and you fix the file.
3. Gitar says "ready", but there's a teaching mistake only you can spot.
4. You add a course yourself.

Answers are in [ANSWERS.md](ANSWERS.md), so try each round before you look. It's a throwaway repo, so nothing breaks.

## Tomorrow

- At 11:00 James sends you an invitation to the real repository. Accept it the same way.
- Course pull requests arrive when a student, or a judge, types a course Homeroom doesn't know. James will tell you when one is waiting.
- In the demo you'll say a few lines about this. James will give them to you.

If something looks wrong, ask James. Nothing on a pull request affects Homeroom until you press Merge, and a merge can be undone.
