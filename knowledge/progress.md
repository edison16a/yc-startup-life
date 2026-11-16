# Progress log

Updated after every wave.

| Stage | Status | Notes |
|---|---|---|
| 0 Setup | done | dataset fetched (6,399 companies), companies.csv built, name features computed for all names |
| 1 Research every company (calibration sample first) | in progress | pilot wave done (48 records, shards cal_0001-0006); pilot records are shallow and lack branding, so they are queued for a redo after the first full waves |
| 2 Advice corpus and YC facts | not started | |
| 3 Derive knowledge | not started | now includes knowledge/naming.md |
| 4 Finalize skills and backtest | not started | three skills finalized: evaluator, creator, name creator |
| 5 Verify and finish | not started | |

## Log

- Pilot wave (6 agents, 8 companies each): about 2-4 minutes and 100-140k subagent tokens per shard. Agents used 4-5 of 14 tool calls per company and skipped outcome and competitor searches. Fix: the research prompt now lists required minimum searches, including a branding search.
- Branding added: `branding` block in the schema, `scripts/name_features.py`, `yc-name-creator` skill, brand as a required block in every evaluation.
- Parallel agents raised from 6 to 8.
