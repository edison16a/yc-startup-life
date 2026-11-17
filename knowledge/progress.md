# Progress log

| Stage | Status | Notes |
|---|---|---|
| 0 Setup | done | dataset fetched (6,399 companies), companies.csv built, name features computed for all names |
| 1 Research every company | done | 6,398 researched at depth 2, 1 marked unresearchable with a reason; calibration sample 663 of 663 |
| 2 Advice corpus and YC facts | done | 41 advice notes, 19 applicant accounts |
| 3 Derive knowledge | done | six knowledge files and eight tables, rebuilt after the completeness pass |
| 4 Finalize skills and backtest | done | evaluator, creator and name creator finalized against 6,398 records; backtest on six companies in knowledge/backtest.md; evaluator SKILL.md got calibration rules from it |
| 5 Verify and finish | done | final audit 2 passed (middle 9.4 percent); check_complete.py exits 0 |

## Log

- Pilot and early waves: shared web search budget forced a rule of at most a few shards per wave and no depth 2 record without the required searches; records written without searches were downgraded and redone.
- Audits 1 to 17 and the first final audit failed the 10 percent bar (1.3 to 42 percent, final audit middle 11.2). Cause: records written before prompt lesson 10 left database reported rounds in notes instead of rounds.
- Gate fix: check_complete.py now requires knowledge/audit_log.md to end with the exact line AUDIT RESULT: PASS. An earlier substring test passed falsely because the log header quoted the phrase.
- Backtest: six companies run as if at their batch date. The evaluator was too pessimistic about niche sounding B2B companies, missed slow profitable paths and pivots. Rules added to the evaluator skill; yc_overlap.py gained --exclude so a backtest does not see its own outcome.
- Completeness pass: older records with empty rounds and database mentions were re-searched (about 2,157 records in 31 shards of 8 and 120 shards of 16). Each added round rests on a named database or outlet and says so in notes. Funding rounds recorded went up to 8,297.
- Final audit 2: 36 fresh records, 245 fields, strict 36.7 percent, middle 9.4 percent, lenient 0.4 percent. The margin is thin and the sample small; see the caveats in knowledge/audit_log.md.
- Raise calculator added to the report Funding tab, README rewritten as the Will I Raise skill.
