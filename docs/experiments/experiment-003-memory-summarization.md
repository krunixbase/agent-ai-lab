# Experiment 003 — Memory Summarization

## Objective
Evaluate whether the agent can maintain a coherent long-term context by summarizing memory when it grows too large. 
The goal is to prevent context overflow while preserving essential information.

---

## Scope
This experiment focuses on:
- detecting when memory exceeds a size threshold
- generating a summary using the LLM
- replacing detailed entries with a compact summary
- ensuring the agent still performs correctly after summarization

---

## Setup
1. Use the existing `Memory` class.
2. Add a simple threshold, e.g. 5–10 entries.
3. When the threshold is exceeded:
   - concatenate memory entries
   - send them to the LLM with a summarization prompt
   - store the summary as a new memory entry
   - clear older entries

4. Use `OpenAIPipeline` for summarization.

---

## Test Procedure

### Step 1 — Fill memory
Send 10–15 user messages such as:

- tell me something about space
- what is the capital of Japan?
- explain how photosynthesis works
- summarize the last message
- repeat the word banana 5 times

### Step 2 — Trigger summarization
Memory should exceed the threshold and produce a summary like:

- Summary: The user asked about space, Japan, photosynthesis, and text transformations.


### Step 3 — Continue interaction
Ask:

what did I ask you earlier?

Expected behavior:
- agent uses the summary
- responds with a high-level recollection

---

## Expected Memory Trace

Before summarization:

[entry1, entry2, entry3, ... entry10]

After summarization:

[summary_entry, entry11, entry12, ...]

---

## Success Criteria
- summarization triggers automatically
- summary is coherent and captures key topics
- agent continues to answer correctly using summarized memory
- no loss of essential context

---

## Notes
This experiment prepares the system for:
- long conversations
- multi-agent shared memory
- persistent memory backends
