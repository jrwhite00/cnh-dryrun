# Anna: everything you do today, step by step

This one page covers your whole day at the hackathon on Monday, Nov 9. Read it top to bottom once, then follow it part by part. If you get stuck anywhere, see [Part 10](#part-10-when-something-goes-wrong). If that doesn't help, ask James.

**If an AI assistant is helping you,** give it this whole page, and make sure it reads [Part 11](#part-11-for-annas-ai-assistant) first. Part 11 says what it may help with and what only you can do.

**Running late? It's after 11:00 and the concept table doesn't exist yet. Go straight to [Part 5](#part-5-write-the-concept-table-1100-to-1200).** Skip the practice. You've already joined the real repo.

**Your job in one sentence:** you write Homeroom's concept table, then you're the teacher who decides which courses go into it.

**Why it matters:** Homeroom turns the classes a student has taken into a personal KubeCon schedule. Your concept table is the bridge between school classes and conference talks. Without it, Homeroom can't do anything. You never use AI for any of this. That's the point of your role, and it's part of what we tell the judges.

## Your day at a glance

| When | What you do | Where | Part |
|---|---|---|---|
| Now, before 11:00 | Set up your GitHub account | github.com | [1](#part-1-set-up-your-github-account-10-minutes) |
| Before 11:00, if there's time | Practice reviewing courses | the practice repo | [2](#part-2-learn-the-words-and-the-buttons-15-minutes) and [3](#part-3-practice-about-1-hours) |
| 11:00 | Join the real repo. Already done: you're a member. | the real repo | [4](#part-4-join-the-real-repo-already-done) |
| 11:00 to 12:00, **or as soon as you can** | **Write the concept table. This is the most important job of the day.** | the real repo | [5](#part-5-write-the-concept-table-1100-to-1200) |
| Right after | Write a sixth concept for "keeping a site up under load" | the real repo | [6](#part-6-a-sixth-concept-keeping-a-site-up-under-load) |
| After your concepts merge | Check the AI's tags on five talks | with James | [7](#part-7-check-the-ais-tags-on-five-talks-15-minutes) |
| Afternoon, until 16:15 | Review course pull requests as they arrive | the real repo | [8](#part-8-review-real-course-pull-requests-afternoon) |
| Before 17:30 | Rehearse your demo lines twice with James | at the venue | [9](#part-9-the-demo-1730) |
| 17:30 | The demo | on stage, or at a judges' table | [9](#part-9-the-demo-1730) |
| 18:30 | Winners are announced | | |

**Venue:** The Shop Workspace, 350 E 400 S, Salt Lake City. All times are Mountain Time.

**Two repos, don't mix them up:**

| | Practice repo | Real repo |
|---|---|---|
| Address | https://github.com/jrwhite00/cnh-dryrun (this one) | **https://github.com/jrwhite00/homeroom** |
| What it's for | Trying every button. Nothing here matters. | The actual hackathon project. Judges see everything. |
| Concept table | Already filled in with placeholders. **Don't copy them.** | Empty until you write it in Part 5 |
| Other pull requests | Only practice courses | Lots of James's code pull requests. Ignore all of them except "Add course: …" and your own concepts. |

## Rules that never change

1. **No AI in your content or your decisions.** You write every word of every concept, and you make every course decision. An AI assistant may help you find buttons and check spelling (Part 11), but it never writes your words or decides for you. Gitar's comments are a checklist you can read, but the decision is yours.
2. **No real people.** No student names, ages, schools or emails, anywhere, ever. If you see one, close the pull request and tell James.
3. **Never tick an "Apply fix" box** in a Gitar comment.
4. **You can't approve your own pull request.** GitHub doesn't allow it. James approves yours, and you approve Homeroom's.
5. **Nothing changes until someone presses Merge, and a merge can be undone.** You can't break anything for good.

---

## Part 1: Set up your GitHub account (10 minutes)

Skip any step you've already done.

1. Go to https://github.com and sign in as `aelinkowski9`.
2. If GitHub asks you to set up two-factor authentication, do it with your phone. It takes about 5 minutes.
3. Open https://github.com/jrwhite00/cnh-dryrun/invitations and click **Accept invitation**.
4. Open https://github.com/jrwhite00/cnh-dryrun. If you see a list of files, including `START_HERE.md`, it worked.
5. Optional: open https://github.com/settings/notifications and make sure **Email** is ticked under "Participating, @mentions and custom". That way GitHub emails you when you're asked to review something.

## Part 2: Learn the words and the buttons (15 minutes)

### Words you'll see

| Word | What it means |
|---|---|
| Repository, or repo | The project's folder on GitHub |
| Pull request, or PR | A proposed change that waits for approval. Nothing changes until someone presses Merge. |
| Gitar | A robot reviewer that reads each pull request and leaves comments. It never edits course files or merges. |
| Concept, or topic | One idea in your table, such as containers. Gitar says "topic", and it means the same thing. |
| Approve | Your sign-off that the change is right |
| Merge | Puts the change into the project. Homeroom uses it from then on. |
| Close | Rejects the pull request. Nothing changes. |
| Branch | A side copy where a proposed change waits. You can ignore branches. |
| Commit | Saving a change on GitHub |

### What the files look like

Everything you'll work on is in the `curriculum` folder, in two sub-folders.

**A concept**, in `curriculum/concepts/`. You write these. This example is a practice placeholder, written by AI. It shows the shape only, so never reuse its words.

```
concept: Containers
definition: A way to package a program with everything it needs so it runs the same on any computer.
technical words: Docker, container image, registry, container runtime
```

- **concept:** the name, in plain words.
- **definition:** one sentence a 15-year-old would understand.
- **technical words:** the words a conference speaker would use for this idea, separated by commas. Homeroom searches the talks with these. Part 5 explains how both lines are used.

**A course**, in `curriculum/courses/`. Homeroom proposes these and you approve them.

```
course: Computer Science I
state: Texas
standard: Texas TEKS, Computer Science I
teaches: programming-basics, data-and-databases
added by: Homeroom, after a student confirmed the match
```

- **course** and **state:** the class, as the student named it.
- **standard:** where the course comes from, such as a state standard.
- **teaches:** what a student knows after the course. At most 4 topics, each spelled exactly like a concept file's name, without `.yaml`.
- **added by:** who proposed it.

### The four button paths

You'll use these all day. Come back here whenever a step says "approve and merge" and so on.

**A. Approve, then merge**

1. Open the pull request and click the **Files changed** tab.
2. Click the green **Review changes** button at the top right. It may say **Submit review** instead.
3. Choose **Approve**, write a short note such as "Checked against the concept table", and click **Submit review**.
4. Click the **Conversation** tab, scroll to the bottom, click **Merge pull request**, then **Confirm merge**.
5. The pull request turns purple and says **Merged**. Done.

**B. Edit the file, then approve and merge**

1. On **Files changed**, click the **⋯** (three dots) on the right of the file's header bar, then **Edit file**.
2. Change only the lines that need it.
3. Click the green **Commit changes…** button. Keep "Commit directly to the … branch" selected, and click **Commit changes**.
4. Wait 2 to 3 minutes, then refresh the page. Gitar checks the file again and posts a new comment.
5. If the new comment says the course looks ready, and you agree, follow path A.

**C. Close it**

1. On **Conversation**, scroll to the bottom.
2. Type a one-line reason in the comment box, for example "Wrong match: Utah course with a Texas standard".
3. Click **Close with comment**. Nothing changes in the project.

**D. Create a new file and propose it**

1. Open the repo's main page. Click into the folder you want, such as `curriculum`, then `concepts` or `courses`.
2. Click **Add file** at the top right, then **Create new file**.
3. Type the file name in the box at the top, ending in `.yaml`. Use lowercase with hyphens, no spaces.
4. Type the lines into the big box.
5. Click **Commit changes…**, choose **Create a new branch for this commit and start a pull request**, then click **Propose changes**.
6. On the next page, click **Create pull request**.
7. Message James with the link from your browser's address bar. He approves it, then you or he merges it with path A, step 4.

### How to read Gitar's comments

Gitar posts two kinds of comment on each course pull request:

- **The one for you** starts with **"This course looks ready…"** or **"This course is not ready…"**. Read this one.
- **A programmer-style review**, in a grey box with a label such as **Approved**, **Changes requested**, **Bug** or **Blocked**. Skip it, because it's written for programmers. If it says something that worries you, ask James.

Gitar checks spelling, the topic count, that the standard is filled in, and personal details. **It can't tell whether a class really teaches a topic.** That part is yours.

## Part 3: Practice (about 1½ hours)

Do this in the practice repo before 11:00 if you can. If time is short, do Round 1 and Round 3. You can stop between rounds.

19 practice course pull requests are waiting at https://github.com/jrwhite00/cnh-dryrun/pulls. Keep two more tabs open while you work:

- **The practice concept list**, at https://github.com/jrwhite00/cnh-dryrun/tree/main/curriculum/concepts. It has five concepts: `programming-basics`, `data-and-databases`, `networking-basics`, `linux-command-line` and `containers`. Their wording is an AI-written placeholder for practice only. **Never copy it into the real repo.**

- **This page**, for the button paths.

### The checklist for every course

Check all five before you decide:

1. **Topics exist.** Every topic after `teaches:` is one of the concepts above, spelled exactly the same, hyphens included.
2. **Four topics at most.** Five or more means the match was too generous.
3. **Each topic is really taught.** Would a student who passed this class actually know this? Only you can answer this one.
4. **The standard is right.** `standard:` is filled in and fits the course and the state. A Utah course shouldn't name a Texas standard.
5. **No real people.** No student names, schools, ages or emails, including on the `added by:` line.

Then decide:

| If… | Do this |
|---|---|
| All five checks pass | Path A: approve, then merge |
| Some lines need changing, but the course is a real match | Path B: edit, then approve and merge |
| It's the wrong match, or a person's details are in it | Path C: close it |

**Don't trust the pull request's description.** It's written by a machine and always says "contains no student data", even when that's false.

### Round 1: warm-up, approve and merge (about 25 minutes)

All of these are correct. Use path A on each one until it takes you under 2 minutes.

| Done | Pull request | Course | Look at |
|---|---|---|---|
| ☐ | [#2](https://github.com/jrwhite00/cnh-dryrun/pull/2) | Computer Science I (Texas) | Go slowly on this first one |
| ☐ | [#4](https://github.com/jrwhite00/cnh-dryrun/pull/4) | Web Development 2 (Utah) | Does a web class with JavaScript count as programming? |
| ☐ | [#5](https://github.com/jrwhite00/cnh-dryrun/pull/5) | Database Development (Utah) | Just one topic, which is fine |
| ☐ | [#6](https://github.com/jrwhite00/cnh-dryrun/pull/6) | Data Analytics (Utah) | Two topics |
| ☐ | [#7](https://github.com/jrwhite00/cnh-dryrun/pull/7) | Game Development Fundamentals 1 (Utah) | One topic |
| ☐ | [#8](https://github.com/jrwhite00/cnh-dryrun/pull/8) | Robotics 2 (Utah) | One topic |
| ☐ | [#9](https://github.com/jrwhite00/cnh-dryrun/pull/9) | Computer Science II (Texas) | Compare it with #2 |
| ☐ | [#10](https://github.com/jrwhite00/cnh-dryrun/pull/10) | Computer Science III (Texas) | Same pattern as #9 |
| ☐ | [#11](https://github.com/jrwhite00/cnh-dryrun/pull/11) | Computer Science Discoveries | No state, because it's a national curriculum. Is the standard still fine? |

<details>
<summary>Answers for Round 1 (open after you've tried)</summary>

All nine: approve and merge as they are. On #11, "none, a nationwide curriculum" is a fine `state:` line, and Code.org's curriculum is a reasonable `standard:`.

</details>

### Round 2: Gitar finds a problem, you fix it (about 30 minutes)

Gitar's comment on each of these starts with "This course is not ready…" and quotes the problem line. Decide whether you agree, then use path B. Your fix may differ from Gitar's suggestion.

| Done | Pull request | Course | The problem, in a few words |
|---|---|---|---|
| ☐ | [#16](https://github.com/jrwhite00/cnh-dryrun/pull/16) | Fundamentals of Computer Science (Texas) | A spelling mistake. Start here. |
| ☐ | [#17](https://github.com/jrwhite00/cnh-dryrun/pull/17) | Intro to Python Summer Camp | No standard. A camp has no state standard, so what would you write? |
| ☐ | [#18](https://github.com/jrwhite00/cnh-dryrun/pull/18) | AP Computer Science Principles | Five topics. Which two don't belong? |
| ☐ | [#19](https://github.com/jrwhite00/cnh-dryrun/pull/19) | Intro to Cloud Computing | A topic that isn't in the table |
| ☐ | [#3](https://github.com/jrwhite00/cnh-dryrun/pull/3) | Full-Stack Coding Bootcamp | All of the above at once. Do it last. |

<details>
<summary>Answers for Round 2 (open after you've tried)</summary>

| Pull request | Fix |
|---|---|
| #16 | `programing-basics` becomes `programming-basics`. It was missing an "m". |
| #17 | Fill in the standard, for example `standard: none, summer camp`. Your call. |
| #18 | Remove `linux-command-line` and `containers`, because the AP framework teaches neither. Keep `programming-basics, networking-basics, data-and-databases`. |
| #19 | Remove `kubernetes`, since there's no such topic. Keep `containers, linux-command-line`. If you think we need a Kubernetes concept, tell James. Adding a concept is a separate decision. |
| #3 | Cut to four topics, drop `kubernetes`, and fill in the standard, for example `standard: none, private bootcamp`. A sensible four: `programming-basics, data-and-databases, networking-basics, linux-command-line`. |

</details>

### Round 3: Gitar says "ready", but is it? (about 20 minutes)

This is the most important round. On each of these, Gitar says the course looks ready, because the format is fine. But each has a teaching mistake. Find it before you approve.

| Done | Pull request | Course | Hint |
|---|---|---|---|
| ☐ | [#12](https://github.com/jrwhite00/cnh-dryrun/pull/12) | Digital Literacy (Utah) | Is "file management" the same as typing commands in a terminal? |
| ☐ | [#13](https://github.com/jrwhite00/cnh-dryrun/pull/13) | Robotics 1 (Utah) | Does a robot talking to its remote control teach how the internet works? |
| ☐ | [#14](https://github.com/jrwhite00/cnh-dryrun/pull/14) | Game Development Fundamentals 2 (Utah) | Re-read what "containers" means. |
| ☐ | [#15](https://github.com/jrwhite00/cnh-dryrun/pull/15) | Computer Science I (Utah) | Read `standard:` next to `state:`. |
| ☐ | [#20](https://github.com/jrwhite00/cnh-dryrun/pull/20) | Computer Programming 2 Honors (Utah) | Read every line, including `added by:`. |

<details>
<summary>Answers for Round 3 (open after you've tried)</summary>

| Pull request | The mistake | What to do |
|---|---|---|
| #12 | `linux-command-line`. File management in Digital Literacy means folders on Windows or a Mac. | Path B: `teaches: networking-basics`, then merge |
| #13 | `networking-basics`. A robot and its controller aren't the internet. | Path B: `teaches: programming-basics`, then merge |
| #14 | `containers`. Sharing a finished game isn't packaging a program in a container. | Path B: `teaches: programming-basics`, then merge |
| #15 | A Texas standard on a Utah course. The student probably picked the wrong match. | Path C: close, with "Utah course with a Texas standard, wrong match" |
| #20 | `added by:` names a student, her grade and her school. | Path C: close it and tell James. Don't edit it, because the name stays visible in the pull request's history. |

</details>

### Round 4: create a course yourself (about 10 minutes)

Use path D, in the `curriculum/courses` folder:

- File name: `ap-computer-science-a.yaml`
- Lines:
  ```
  course: AP Computer Science A
  state: none, a national course
  standard: College Board AP Computer Science A course and exam description
  teaches: (your choice, up to four of the five topics)
  added by: Anna
  ```

Wait for Gitar's comment and fix anything it finds. In the practice repo you can merge it yourself, without James's approval.

<details>
<summary>Answer for Round 4</summary>

`teaches: programming-basics, data-and-databases` is a good choice, since AP Computer Science A is mostly Java programming plus arrays and lists. `programming-basics` alone is also fine.

</details>

---

## Part 4: Join the real repo (already done)

You're already a member of the real repo. To check:

1. Open **https://github.com/jrwhite00/homeroom**.
2. You should see folders such as `backend`, `frontend` and `deploy`. There's no `curriculum` folder yet, because you create it in Part 5.
3. Bookmark it. From now on, everything you do is in this repo, not the practice one.

If GitHub shows "404" instead, open https://github.com/jrwhite00/homeroom/invitations, click **Accept invitation**, and try again.

## Part 5: Write the concept table (11:00 to 12:00)

**Nothing else in Homeroom works until this is done**, so start right after Part 4. Two finished features are waiting on your concepts right now: question translation (James's pull request #4) and talk tagging (#6).

### What you're writing

Six concept files, in this order. The first is the one Part 6 describes; the other five have fixed names, which the plan and the courses already use:

| Order | File name, exactly |
|---|---|
| 1 | The scaling concept from [Part 6](#part-6-a-sixth-concept-keeping-a-site-up-under-load). The demo depends on it most, so write it first. |
| 2 | `containers.yaml` |
| 3 | `programming-basics.yaml` |
| 4 | `networking-basics.yaml` |
| 5 | `data-and-databases.yaml` |
| 6 | `linux-command-line.yaml` |

Each one takes 5 to 10 minutes. Good enough beats polished.

### Rules for writing them

- **Every word must be yours.** Don't copy from the practice repo, from this page, or from anything AI wrote, not even a short phrase. If you notice you've written something you saw elsewhere, rewrite it. Your words are what the project's "a teacher wrote this" claim rests on.
- **Three lines per file:** `concept:`, `definition:` and `technical words:`, exactly as in Part 2.
- **How Homeroom uses your two lines.** This is why the wording matters:
  1. A student types a question in plain words, such as "how do big websites stay up when everyone visits?"
  2. Homeroom compares the question with **your definitions** and picks the closest concept, or up to three close ones.
  3. Homeroom then searches all 600 KubeCon talks using that concept's **technical words**.
- So **the definition** should sound the way a student would describe the idea: one plain sentence a high school junior would understand, in everyday words. No jargon here.
- And **the technical words** should be what a conference speaker would put in a talk title: tools, jargon and product names. Aim for 5 to 10 per concept, separated by commas. This is where the jargon goes.
- Spelling and the colon after each label matter. `technical words:` with a space, not `technical-words:`. A colon inside your sentence is fine.

### Steps, for each file

Do this once per file, in the order of the table. Each file is its own pull request.

1. Open the real repo's main page.
2. Click **Add file**, then **Create new file**.
3. In the name box, type the whole path: `curriculum/concepts/programming-basics.yaml`. Each `/` you type turns the text before it into a folder, so this creates the folders too.
4. Type your three lines in the big box.
5. Read it once more:
   - The file name is spelled exactly as in the table.
   - The three labels are spelled exactly `concept:`, `definition:` and `technical words:`. **Check "definition" letter by letter.** A misspelled label makes Homeroom treat that line as empty.
6. Click **Commit changes…**. A box opens with two choices. **Choose the second one, "Create a new branch for this commit and start a pull request".** Never choose "Commit directly to the main branch": that skips review and leaves no pull request for the judges. Then click **Propose changes**, then **Create pull request**.
7. Message James: "Concept PR ready: programming-basics" plus the link from your address bar.
8. Start the next file straight away. Don't wait for James.

James approves and merges each one. Gitar may comment on them. Read it if you like, but concepts are yours, so ignore anything you disagree with.

### Fixing a concept that's already in the repo

If a concept is already in the real repo but needs changing, for example `programming-basics.yaml`:

1. Open it: the real repo, then `curriculum`, then `concepts`, then the file.
2. Click the **pencil** icon at the top right of the file.
3. Make your changes.
4. Click **Commit changes…**, choose **Create a new branch for this commit and start a pull request**, then **Propose changes**, then **Create pull request**.
5. Message James the link.

**You're done with Part 5 when** the real repo's `curriculum/concepts` folder on its main page shows all six files, and each one arrived through a pull request.

## Part 6: A sixth concept: keeping a site up under load

**The demo needs this one.** In the demo, Maya asks how big websites stay up. James tested that question against the practice concepts, and it matched "data and databases" and found database talks, not scaling talks. None of the five concepts is about keeping a website working when lots of people use it at once.

1. Decide whether it's a real, teachable idea for these students. If you think it isn't, tell James now, because the demo's search example depends on it.
2. If yes, choose the file name yourself: lowercase words joined by hyphens, ending in `.yaml`, for example `scaling-and-reliability.yaml`. Homeroom accepts any name in that pattern.
3. Write it exactly as in Part 5, as one more pull request. Make the definition sound like a student asking about busy websites. Put the scaling jargon a KubeCon speaker would use in the technical words.
4. Tell James the file name when you message him the link.
5. After it merges, James runs Maya's question again to check it now finds scaling talks. If it doesn't, he'll show you what it matched, and you can reword the definition with path B.

## Part 7: Check the AI's tags on five talks (15 minutes)

Once your concepts are merged, James runs a tool that has AI read all 600 talks and tag each one with the concepts it assumes the audience already knows. For example, a talk might assume `containers`. You're the human check on the AI.

1. James sends you five talks, each with the concepts the AI tagged and a one-sentence reason.
2. For each talk, read the title and the reason, then answer: **is each tag right, and is any concept missing?**
3. Reply to James with one line per talk: "OK", or what's wrong, for example "Talk 3: doesn't really need containers".
4. That's it. James decides what to change in the tool. You don't edit anything.

## Part 8: Review real course pull requests (afternoon)

### How you'll know one is waiting

- GitHub emails you "review requested", if James has set that up, or James messages you.
- You can also check the real repo's **Pull requests** tab every 20 to 30 minutes.
- Course pull requests are titled **"Add course: <Course> (<State>)"**. Ignore every other pull request, because those are James's code.

They only start arriving after your concepts are merged, and after Homeroom can open them or someone opens one by hand. For the first while there may be nothing to review. That's expected.

### For each one

1. Run the five-point checklist from Part 3.
2. Choose path A, B or C, the same as in practice.
3. Do it within about 15 minutes if you can. A merged course is what makes Homeroom work for that student.
4. If you're unsure, ask James rather than guessing. Closing is always safe.

### During judging

A judge might type in their own first programming class (the "bonus scene"). That opens a course pull request for you live. Review it exactly the same way, while the judge watches if they want to. It's a chance to show your role.

## Part 9: The demo (17:30)

The demo runs about three minutes, with ten scenes. James does most of the talking and drives the screen. **You speak in four places.** Say the lines naturally. They don't need to be word for word.

Rehearse twice before 17:30: once together at full length, and once with the 60-second version against a timer.

| Scene | About when | What's on screen when you start | You say |
|---|---|---|---|
| **2. Meet Maya** | 0:15, right after James's opening | Homeroom's start screen. Pick Utah, tick three classes, press the button. | "Maya is a junior in Utah. She's taken Exploring Computer Science, Computer Science Principles and Programming 1. That's all Homeroom needs to know about her." |
| **3. Her week** | 0:30 | Maya's week in three groups. Click the highlighted "one step away" talk to open it. | "Four talks she can follow today. Thirty-one aren't for her yet, and that's fine. The nine in the middle are where she grows. This one needs containers, so Homeroom sends her to a beginner talk first, or to a project booth with a question to ask." |
| **8. Gitar** | 2:15, after James's part of this scene | A course pull request that a student's course opened | "Gitar also guards the curriculum. When a student types a course we don't know, Homeroom opens a pull request like this one. Gitar checks it against my concept table, and then I decide. AI suggests, Gitar checks, a teacher decides." |
| **10. The close** | 2:50 | The closing card | "Swap Utah for any state, a college transcript or a grad program. Every student who has never been to a conference can walk in knowing which rooms they belong in." Then James says the last line. |

Notes:
- Maya is a made-up student. Say her name. It's not a real person.
- The numbers in scene 3 (four, thirty-one, nine) may change on the day. James will tell you if they do.
- **Shorter versions:** in the 90-second and 60-second versions, you only say scenes 3 and 10. James picks the version at check-in.
- **At a judges' table**, rather than on stage: James gives the 60-second version, then judges click around. Be ready to say the scene 8 line and show a course pull request if a judge asks how courses get added.

## Part 10: When something goes wrong

| What you see | What to do |
|---|---|
| No **Review changes** button | Look for **Submit review** in the same place, at the top right of **Files changed**. |
| You can't approve: "You can't approve your own pull request" | That's your own pull request. Message James to approve it. |
| The **Merge pull request** button is grey | Scroll up, because a check is probably still running. Wait a minute and refresh. If it's still grey after 5 minutes, ask James. |
| Gitar hasn't commented after 5 minutes | Refresh. If it's still missing, carry on without it, since your review is what counts. |
| A Gitar comment has an **Apply fix** box | Don't tick it. Make the change yourself with path B. |
| "File already exists" when creating a file | Someone has already made it. Tell James. Don't pick a new name. |
| A file name is spelled wrong after merging | Tell James. It's a 1-minute fix. |
| You merged something by mistake | Nothing's broken. Tell James, and he'll undo it. |
| You see a real person's name, school or email | Close the pull request (path C) and tell James straight away. |
| You're not sure | Ask James. Closing a course pull request is always safe. |
| GitHub asks you to sign in again, or for a code | Use your phone's two-factor app, as in Part 1. |

## Part 11: For Anna's AI assistant

This part is written to the AI assistant helping Anna. Anna, read it too, so you know what to expect from it.

### Your role

You're helping Anna, a teacher, do her part of a hackathon project called Homeroom, using this page as the plan. Her part is Parts 5 to 9: write a concept table, review course pull requests, check five AI tags, and speak in the demo.

The project's story, told to judges, is that **the concept table and every course decision are written and made by a teacher without AI**. Your help must keep that true. If you write her words or make her decisions, the project's central claim becomes false.

### You may

- Walk her through any button path in Part 2, one click at a time, and explain GitHub screens and error messages.
- Tell her which part of this page comes next, and keep track of what she has finished.
- Check what she has written **for format only**, then tell her what to fix without fixing it yourself:
  - the file name is lowercase with hyphens, ends in `.yaml`, and sits in `curriculum/concepts/` or `curriculum/courses/`;
  - each line starts with the right label and a colon (`concept:`, `definition:`, `technical words:`, or the five course labels);
  - every slug after `teaches:` matches a concept file's name exactly;
  - there are at most 4 slugs after `teaches:`.
- Read a course pull request with her and point at the five-point checklist in Part 3. You may report factual mismatches, such as "the state line says Utah but the standard says Texas" or "this slug has no concept file".
- Remind her of the rules at the top of this page when she's about to break one.
- Explain what a technical term means, if she asks.

### You must not

- **Write, suggest or reword any concept's name, definition or technical words.** Don't offer a list of words "to choose from" either. If she asks, say that the plan requires her own words, and point her to Part 5's guidance.
- **Decide whether a course teaches a concept, or whether to approve, edit or close.** You can lay out the checklist. She answers question 3, "Is each topic really taught?", herself.
- Approve, merge, close, edit or commit anything on her behalf, even if you have access to her account or the GitHub CLI.
- Tick any "Apply fix" box, or tell her to.
- Touch any pull request or file outside `curriculum/` in `jrwhite00/homeroom`. Those belong to James.
- Copy anything from the practice repo `jrwhite00/cnh-dryrun` into the real repo.
- Put any real person's details into any file.

### Facts you need

| Fact | Value |
|---|---|
| Real repo | https://github.com/jrwhite00/homeroom |
| Practice repo | https://github.com/jrwhite00/cnh-dryrun. Practice only, and its concepts are placeholders. |
| Anna's GitHub account | `aelinkowski9` |
| Concept files | `curriculum/concepts/<slug>.yaml`, three lines: `concept:`, `definition:`, `technical words:` (comma-separated) |
| Course files | `curriculum/courses/<slug>.yaml`, five lines: `course:`, `state:`, `standard:`, `teaches:` (comma-separated slugs, at most 4), `added by:` |
| File format | Plain `name: value` lines, read line by line rather than as strict YAML. A colon inside a value is fine. |
| The five planned concept slugs | `programming-basics`, `data-and-databases`, `networking-basics`, `linux-command-line`, `containers` |
| The sixth concept | About keeping a website working under heavy use. Anna chooses its slug (Part 6). |
| How Homeroom uses concepts | It matches a student's question against the definitions by meaning, then searches talks with the matched concept's technical words. |
| Who approves Anna's own pull requests | James (GitHub won't let her approve her own) |
| Who approves course pull requests | Anna |
| "Maya" | A made-up student in the demo script only. A student's name inside any course or concept file is always a reason to close the pull request. |
| Schedule | Build 11:00 to 17:30, feature freeze 16:15, demos 17:30, winners 18:30, Mountain Time |
| When unsure | Tell Anna to ask James. Never guess on her behalf. |
