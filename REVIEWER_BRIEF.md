# Code Review Exercise — Fraud Risk Scoring Service

## Scenario
You're a ML platform engineer reviewing a PR from a teammate that adds a
new fraud-risk model and ships it as a containerized FastAPI service. Treat this
repository as the full diff of that PR — everything in it is "new" and up for
review, from the training script to the Dockerfile.

## How the session runs
This is a live exercise, done on a shared screen with your interviewer — not a
take-home. Roughly:
1. **~15-20 min, on your own:** read through the repo and jot down what stands
   out. Bullet points are fine — you don't need polished prose, just enough to
   talk through afterward. Thinking out loud as you go is welcome but not
   required.
2. **~30 min, together:** walk your interviewer through what you found. They'll
   ask follow-up questions, push on a few points, and may point you toward
   areas you didn't get to.

## What to produce
Comments as if this were a real pull request:
- Group them by severity: **blocker**, **major**, **minor**, **nit**.
- For each: what's wrong, why it matters (concretely — what breaks, when, and
  for whom), and what you'd change instead.
- Flag anything you're unsure about too — reasoning quality matters more than
  raw hit rate, and you're not expected to find everything in 15-20 minutes.

## Scope
Everything is fair game: environment/dependency management, containerization,
the ML training pipeline, model registry/versioning, the serving code, test
coverage, how the service is deployed (the Helm chart), and general coding
practices.

## Ground rules
- No answer key is given to you — work through it as you would a real PR.
- **This is a read-only review.** Do not install dependencies, run the
  training script, start the server, build the Docker image, or render/install
  the Helm chart — review it exactly as you would a diff on GitHub, by reading
  the code. You don't need a working local environment to do this exercise,
  and nothing here is meant to be verified by execution.
- **No AI coding assistants.** Don't run this repo through Claude Code,
  Cursor, Copilot, ChatGPT, or similar tools — the point of the exercise is
  your own reasoning. If you're screen-sharing from an editor with a built-in
  assistant, leave it closed for the duration of the exercise.
- It's fine — expected, even — if you don't get through everything. Depth on a
  few findings beats a shallow pass over all of them.
