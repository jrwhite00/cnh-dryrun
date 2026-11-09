# Practice answers

What James would do with each pull request in [PRACTICE.md](PRACTICE.md). Where you chose differently on a teaching question, you're probably right. These are suggestions, not rules.

## Round 1: approve and merge

#2, #4, #5, #6, #7, #8, #9, #10, #11: approve and merge as they are.

On #11, "none, a nationwide curriculum" is a fine `state:` line, and Code.org's curriculum is a reasonable `standard:`.

## Round 2: edit, then merge

| Pull request | Fix |
|---|---|
| #16 Fundamentals of Computer Science | `programing-basics` → `programming-basics` (it was missing an "m") |
| #17 Intro to Python Summer Camp | Fill in the standard, for example `standard: none, summer camp`. Your call. |
| #18 AP Computer Science Principles | Remove `linux-command-line` and `containers`. The AP framework doesn't teach either. Keep `programming-basics, networking-basics, data-and-databases`. |
| #19 Intro to Cloud Computing | Remove `kubernetes`, since there's no such topic. Keep `containers, linux-command-line`. If you think we need a Kubernetes topic, tell James, because adding a topic is a separate decision. |
| #3 Full-Stack Coding Bootcamp | Cut to four topics, drop `kubernetes`, and fill in the standard, for example `standard: none, private bootcamp`. A sensible four: `programming-basics, data-and-databases, networking-basics, linux-command-line`. |

## Round 3: the traps

| Pull request | The mistake | What to do |
|---|---|---|
| #12 Digital Literacy | `linux-command-line`. "File management" in Digital Literacy means folders on Windows or a Mac, not typing commands. | Edit: `teaches: networking-basics`, then approve and merge |
| #13 Robotics 1 | `networking-basics`. A robot and its controller aren't the internet. | Edit: `teaches: programming-basics`, then approve and merge |
| #14 Game Development Fundamentals 2 | `containers`. Sharing a finished game isn't the same as packaging a program with a container tool. | Edit: `teaches: programming-basics`, then approve and merge |
| #15 Computer Science I (Utah) | The standard is Texas TEKS, but the state is Utah. Utah has no course by that name in our standards, so the student probably picked the wrong match. | Close it, with a comment such as "Utah course with a Texas standard, wrong match" |
| #20 Computer Programming 2 Honors | `added by:` names a student, her grade and her school, even though the description says it has no student data. | Close it and tell James. Don't edit, because the name stays in the history. |

## Round 4

`ap-computer-science-a.yaml` is a good choice with `teaches: programming-basics, data-and-databases`, since AP Computer Science A is mostly Java programming plus arrays and lists. `programming-basics` alone is also fine.
