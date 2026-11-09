---
title: "Fix lint failures"
description: "Push a fix when CI fails only on ruff"
type: automation
when: "CI fails on a PR and the failing step is ruff"
actions: "Fix the reported errors and push a commit to the PR branch, then post a one-line summary"
---

Lint errors in a hackathon are noise. Fix them and say what changed.
