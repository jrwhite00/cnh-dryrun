# Anna: practice workbook

Read [START_HERE.md](START_HERE.md) first. This workbook is the hands-on part: 19 practice pull requests, in order, with what to look for in each.

- **Time:** about 1½ hours. You can stop between rounds and come back.
- **Nothing breaks.** This is a throwaway repo. Merge, edit and close as much as you like.
- **Answers:** [ANSWERS.md](ANSWERS.md) has what James would do for each one. Try each round first, then check.

## Before you start (5 minutes)

1. Open the concept table in a second browser tab and keep it open. It's the five files in [curriculum/concepts](curriculum/concepts):

   | Topic, spelled exactly like this | What it means |
   |---|---|
   | `programming-basics` | Writing instructions with variables, loops and functions |
   | `data-and-databases` | Storing information so programs can save it and look it up |
   | `networking-basics` | How computers find each other and send messages over the internet |
   | `linux-command-line` | Typing commands into a terminal |
   | `containers` | Packaging a program so it runs the same on any computer |

   No other topics exist. A course can only use these five, spelled exactly as above.

2. Open the [list of pull requests](https://github.com/jrwhite00/cnh-dryrun/pulls) in a third tab.

## The checklist for every course

For every pull request, check all five before you decide:

1. **Topics exist.** Every topic after `teaches:` is one of the five above, spelled exactly the same, including the hyphens.
2. **Four topics at most.** Five or more means the match was too generous.
3. **Each topic is really taught.** Would a student who passed this class actually know this topic? This is the question only you can answer. Gitar can't.
4. **The standard is right.** `standard:` is filled in and matches the course and the state. A Utah course shouldn't name a Texas standard.
5. **No real people.** No student names, schools, ages or emails anywhere, including the `added by:` line.

Then pick one of three outcomes:

| If… | Do this |
|---|---|
| All five checks pass | **Approve, then merge** |
| One or more lines need changing, and the course itself is a real match | **Edit the file, wait for Gitar, then approve and merge** |
| The course is the wrong match, or a person's details are in it | **Close it** with a one-line comment saying why |

**Don't trust the pull request's description, and don't trust Gitar blindly.** Both are written by machines. The description always says "contains no student data", even when that's false. Gitar checks spelling and format, but it can't tell whether a robotics class really teaches networking.

## Round 1: warm-up, approve and merge (about 25 minutes)

These are all correct. The goal is to get fast at the click path: read Gitar's comment, open **Files changed**, run the checklist, **Review changes**, **Approve**, **Submit review**, then **Merge pull request** and **Confirm merge**.

| Done | Pull request | Course | Look at |
|---|---|---|---|
| ☐ | [#2](https://github.com/jrwhite00/cnh-dryrun/pull/2) | Computer Science I (Texas) | The example from START_HERE. Go slowly on this one. |
| ☐ | [#4](https://github.com/jrwhite00/cnh-dryrun/pull/4) | Web Development 2 (Utah) | Does a web class with JavaScript count as programming? |
| ☐ | [#5](https://github.com/jrwhite00/cnh-dryrun/pull/5) | Database Development (Utah) | The only course with just one topic. That's fine. |
| ☐ | [#6](https://github.com/jrwhite00/cnh-dryrun/pull/6) | Data Analytics (Utah) | Two topics |
| ☐ | [#7](https://github.com/jrwhite00/cnh-dryrun/pull/7) | Game Development Fundamentals 1 (Utah) | One topic |
| ☐ | [#8](https://github.com/jrwhite00/cnh-dryrun/pull/8) | Robotics 2 (Utah) | One topic |
| ☐ | [#9](https://github.com/jrwhite00/cnh-dryrun/pull/9) | Computer Science II (Texas) | Compare it with #2 |
| ☐ | [#10](https://github.com/jrwhite00/cnh-dryrun/pull/10) | Computer Science III (Texas) | Same pattern as #9 |
| ☐ | [#11](https://github.com/jrwhite00/cnh-dryrun/pull/11) | Computer Science Discoveries | No state, because it's a national curriculum. Is the standard line still fine? |

By the end you should be able to approve and merge one in under 2 minutes.

## Round 2: Gitar finds a problem, you fix it (about 30 minutes)

Gitar's comment on each of these starts with **"This course is not ready…"** and quotes the line. For each one:

1. Read Gitar's comment. Decide whether you agree. You might fix it differently from what it suggests.
2. On **Files changed**, click the three dots on the file's header, then **Edit file**.
3. Change only the lines that need it. Click **Commit changes…**, keep "Commit directly to the … branch", and click **Commit changes**.
4. Wait 2 to 3 minutes, then refresh **Conversation**. Gitar posts a new comment.
5. If it now says the course looks ready, and you agree, approve and merge.

Never tick an **Apply fix** box. Make the change yourself.

| Done | Pull request | Course | The problem, in a few words |
|---|---|---|---|
| ☐ | [#16](https://github.com/jrwhite00/cnh-dryrun/pull/16) | Fundamentals of Computer Science (Texas) | A spelling mistake. Easiest one, so start here. |
| ☐ | [#17](https://github.com/jrwhite00/cnh-dryrun/pull/17) | Intro to Python Summer Camp | The standard is empty. A summer camp has no state standard, so what would you write? |
| ☐ | [#18](https://github.com/jrwhite00/cnh-dryrun/pull/18) | AP Computer Science Principles | Five topics. Which two don't belong? |
| ☐ | [#19](https://github.com/jrwhite00/cnh-dryrun/pull/19) | Intro to Cloud Computing | A topic that isn't in our table |
| ☐ | [#3](https://github.com/jrwhite00/cnh-dryrun/pull/3) | Full-Stack Coding Bootcamp | All of the above at once. Save it for last in this round. |

## Round 3: Gitar says "ready", but is it? (about 20 minutes)

This is the most important round, because it's the part of the job only a teacher can do. On each of these, Gitar says the course looks ready, because the format is fine. But each one has a teaching mistake. Find it before you approve.

| Done | Pull request | Course | Hint |
|---|---|---|---|
| ☐ | [#12](https://github.com/jrwhite00/cnh-dryrun/pull/12) | Digital Literacy (Utah) | Read the description's reason for each topic. Is "file management" the same as a terminal? |
| ☐ | [#13](https://github.com/jrwhite00/cnh-dryrun/pull/13) | Robotics 1 (Utah) | Does a robot talking to its remote control teach how the internet works? |
| ☐ | [#14](https://github.com/jrwhite00/cnh-dryrun/pull/14) | Game Development Fundamentals 2 (Utah) | Re-read what "containers" means in the concept table. |
| ☐ | [#15](https://github.com/jrwhite00/cnh-dryrun/pull/15) | Computer Science I (Utah) | Read the `standard:` line carefully, next to the `state:` line. |
| ☐ | [#20](https://github.com/jrwhite00/cnh-dryrun/pull/20) | Computer Programming 2 Honors (Utah) | Read every line, including `added by:`. Then re-read the description's promise about student data. |

For #20, Gitar should spot the problem, but don't count on it. If a pull request ever has a real student's details in it, **close it and tell James**. Don't fix it by editing, because the old version stays visible in the pull request's history.

## Round 4: add a course yourself (about 10 minutes)

Follow "Adding a course by hand" in [START_HERE.md](START_HERE.md) with this course:

- File name: `ap-computer-science-a.yaml`
- Course: AP Computer Science A
- State: none, a national course
- Standard: College Board AP Computer Science A course and exam description
- Teaches: your call. Pick from the five topics, up to four.
- Added by: Anna

Then wait for Gitar's comment and fix anything it finds. GitHub won't let you approve your own pull request, so merge it yourself.

## When something goes wrong

| What you see | What to do |
|---|---|
| No **Review changes** button | Look for **Submit review** in the same place, at the top right of **Files changed**. |
| The **Merge pull request** button is grey | Scroll up. Usually a check is still running. Wait a minute and refresh. |
| Gitar hasn't commented after 5 minutes | Refresh the page. If it's still missing, carry on without it, since your review is what counts. |
| You merged something by mistake | Nothing's broken. Tell James, and he'll undo it. |
| You're not sure | Close the pull request with a comment saying what you're unsure about. Closing is always safe. |

## After you're done

Message James with:

- How many you approved, fixed and closed
- Anything that was confusing in this workbook or in START_HERE
- Any topic you wished existed. The concept table is yours, so new topics come from you.
