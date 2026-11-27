# G3-C-OVERLAP observation (implementation evidence only)

Direct native Start, exact new branch trial/gate-3-overlap-20261127. This is a preservation and provenance observation, not a new candidate or independent programme verdict. Project identity and exact bootstrap matched the manager-recorded canonical invocation; the direct Start menu selection was received in the invoking conversation. The precise native Start timestamp is for manager reconciliation, not inferred from chat or tool duration.

- Direct bootstrap: `7582695b082e0624438b70631ab2d77e5c199534` (tree `a39f7230e08213ff9972267bc35b23bf810e9a51`). Sole parent paused setup `b477562bcb98dd49c4a929ac5592109f29d2e5a1`; bootstrap diff is ledger only.
- Method `8c4a11205c3a3b6df13979a274841e7d8f3391c1`, entry `5af8187767977e16dbe1fc77d873f963ede82278`, private CAC 1.1.4 unchanged. Protected external binding attached and verified; clean checkout, exact ref/tree, assignment and verdict unchanged before and after attachment. No attachment commit, receipt or handoff.

## Exact retained lineage and observed diff scope

- Commit `4db61415012538f386ae3e128f54e11872bc82a2`, tree `4e9b2d8720b8b072c0dfe4034b14eb436a957778`, parent `25a511327b3ac9e03054322e3066498dc41a09ee`.
- Commit `c5f7a5d2485db0a97ee61ae5c93074067e43f555`, tree `47db5640d524a4217e7381cc7f3466a65fb4fe02`, parent `4db61415012538f386ae3e128f54e11872bc82a2`.
- Commit `a0b8dbe181441757973182389fa59abbf59b1c99`, tree `994b5c04481c4dde91d0340249303e800535b057`, parent `c5f7a5d2485db0a97ee61ae5c93074067e43f555`.
- Commit `b477562bcb98dd49c4a929ac5592109f29d2e5a1`, tree `fe54526a847bffdbcce15d883784bcdfadd76de3`, parent `a0b8dbe181441757973182389fa59abbf59b1c99`.
- Commit `7582695b082e0624438b70631ab2d77e5c199534`, tree `a39f7230e08213ff9972267bc35b23bf810e9a51`, parent `b477562bcb98dd49c4a929ac5592109f29d2e5a1`.

Original ref readback returned the exact terminal V; the new branch descends from V through S and B. Observed git diff --name-status:

- 4db61415 to 4db61415: A evidence/G3-C1.md, M normalizer.py, M tests/test_normalizer.py.
- 4db61415 to c5f7a5d2: M state/ledger.json.
- c5f7a5d2 to a0b8dbe1: A reviews/G3-C1.md, M state/ledger.json.
- a0b8dbe1 to b477562b: M AGENTS.md, M plans/active-execplan.md, M state/ledger.json.
- b477562b to 7582695b: M state/ledger.json.

## Retained blob identities

- `normalizer.py`: `0ae1c09ab70e2052c401ce25996feaf937564adf` at 4db61415, c5f7a5d2, a0b8dbe1, b477562b, 7582695b.
- `tests/test_normalizer.py`: `4ebde9ccdecf0de525cc09105f1e491e35f7789f` at 4db61415, c5f7a5d2, a0b8dbe1, b477562b, 7582695b.
- `.github/workflows/ci.yml`: `6a53244c1a271ecd5a18391bdffeb272fd68d9ee` at 4db61415, c5f7a5d2, a0b8dbe1, b477562b, 7582695b.
- `README.md`: `0300ed4216a0d615f355b2e94471379f172054eb` at 4db61415, c5f7a5d2, a0b8dbe1, b477562b, 7582695b.
- `evidence/G3-C1.md`: `5ee0f50f9a0af19bfa89bfc4a3bfbe1dcf33b7f5` at a0b8dbe1, b477562b, 7582695b.
- `reviews/G3-C1.md`: `f8986125149a0baa7e350cb1708d0b57b722f258` at a0b8dbe1, b477562b, 7582695b.

Actual candidate diff changes baseline list conversion to str.strip() followed by filtering empty strings; the generator/list preserve input order, duplicates, case and internal whitespace. Four added regressions cover trimming, blanks, duplicates/order and case/internal whitespace; three baseline tests remain. Original implementation evidence records baseline 3 passing, RED four failures, GREEN seven passing. Existing independent review also records seven passing tests and replayed RED. These are retained records, not new test results.

## Original CI and independent review reconciliation

Exact original ref: `refs/heads/trial/gate-3-hosted-editor-retry-c2-20261127`. Run 45961867457, attempt 1, required job Test normalizer (140381325150), completed/success. Workflow Fixture CI, push event, actual TESTED_SHA=4db61415012538f386ae3e128f54e11872bc82a2, TESTED_TREE=4e9b2d8720b8b072c0dfe4034b14eb436a957778; seven named tests passed, OK. Original log SHA-256 84a4131fe2d61365d3e048153587c5eaa49a637538af49ad63f2f00f47b66522, 14139 bytes. The complete CI object is equal in H, V and the fresh retained acceptance record. Independent review pins C/tree/H and original job/log and records scoped PASS; V is terminal with no successor. No new CI or logs were requested: accepted original evidence remains scoped to its original ref. The unchanged workflow itself filters to that original branch.

## Observed substantive subprocess intervals (UTC)

63 successful actual Git subprocesses. Sum of measured subprocess intervals: 0.756384 seconds. First start 2026-11-27T10:02:52.574573+00:00; last end 2026-11-27T10:02:53.583170+00:00. The enclosing range is not evidence of continuous work; each interval below is separate. Setup, binding, tool round trips, discussion and gaps are excluded. Original private records retain full exact commands, stdout, stderr and return codes.

| Git operation (checkout prefix omitted) | UTC start | UTC end | Exit |
|---|---|---|---|
| `ls-remote --exit-code https://github.com/JayDEmily/automatic-timer-trial-v1-c.git refs/heads/trial/gate-3-hosted-editor-retry-c2-20261127` | 2026-11-27T10:02:52.574573+00:00 | 2026-11-27T10:02:53.114805+00:00 | 0 |
| `show -s --format=%H %T %P 4db61415012538f386ae3e128f54e11872bc82a2` | 2026-11-27T10:02:53.121297+00:00 | 2026-11-27T10:02:53.125373+00:00 | 0 |
| `show --stat --format=fuller 4db61415012538f386ae3e128f54e11872bc82a2` | 2026-11-27T10:02:53.129573+00:00 | 2026-11-27T10:02:53.132853+00:00 | 0 |
| `show -s --format=%H %T %P c5f7a5d2485db0a97ee61ae5c93074067e43f555` | 2026-11-27T10:02:53.136607+00:00 | 2026-11-27T10:02:53.139683+00:00 | 0 |
| `show --stat --format=fuller c5f7a5d2485db0a97ee61ae5c93074067e43f555` | 2026-11-27T10:02:53.143410+00:00 | 2026-11-27T10:02:53.146442+00:00 | 0 |
| `show -s --format=%H %T %P a0b8dbe181441757973182389fa59abbf59b1c99` | 2026-11-27T10:02:53.150452+00:00 | 2026-11-27T10:02:53.153313+00:00 | 0 |
| `show --stat --format=fuller a0b8dbe181441757973182389fa59abbf59b1c99` | 2026-11-27T10:02:53.157223+00:00 | 2026-11-27T10:02:53.160756+00:00 | 0 |
| `show -s --format=%H %T %P b477562bcb98dd49c4a929ac5592109f29d2e5a1` | 2026-11-27T10:02:53.164825+00:00 | 2026-11-27T10:02:53.168155+00:00 | 0 |
| `show --stat --format=fuller b477562bcb98dd49c4a929ac5592109f29d2e5a1` | 2026-11-27T10:02:53.172225+00:00 | 2026-11-27T10:02:53.175559+00:00 | 0 |
| `show -s --format=%H %T %P 7582695b082e0624438b70631ab2d77e5c199534` | 2026-11-27T10:02:53.179157+00:00 | 2026-11-27T10:02:53.182360+00:00 | 0 |
| `show --stat --format=fuller 7582695b082e0624438b70631ab2d77e5c199534` | 2026-11-27T10:02:53.186331+00:00 | 2026-11-27T10:02:53.189989+00:00 | 0 |
| `rev-list --parents -n 1 c5f7a5d2485db0a97ee61ae5c93074067e43f555` | 2026-11-27T10:02:53.193774+00:00 | 2026-11-27T10:02:53.196899+00:00 | 0 |
| `rev-list --parents -n 1 a0b8dbe181441757973182389fa59abbf59b1c99` | 2026-11-27T10:02:53.200626+00:00 | 2026-11-27T10:02:53.203834+00:00 | 0 |
| `rev-list --parents -n 1 b477562bcb98dd49c4a929ac5592109f29d2e5a1` | 2026-11-27T10:02:53.207859+00:00 | 2026-11-27T10:02:53.211217+00:00 | 0 |
| `rev-parse 4db61415012538f386ae3e128f54e11872bc82a2^{tree}` | 2026-11-27T10:02:53.215337+00:00 | 2026-11-27T10:02:53.218679+00:00 | 0 |
| `diff --name-status 4db61415012538f386ae3e128f54e11872bc82a2^ 4db61415012538f386ae3e128f54e11872bc82a2` | 2026-11-27T10:02:53.222559+00:00 | 2026-11-27T10:02:53.226083+00:00 | 0 |
| `diff 4db61415012538f386ae3e128f54e11872bc82a2^ 4db61415012538f386ae3e128f54e11872bc82a2` | 2026-11-27T10:02:53.230047+00:00 | 2026-11-27T10:02:53.233824+00:00 | 0 |
| `diff --name-status 4db61415012538f386ae3e128f54e11872bc82a2 c5f7a5d2485db0a97ee61ae5c93074067e43f555` | 2026-11-27T10:02:53.237920+00:00 | 2026-11-27T10:02:53.241401+00:00 | 0 |
| `diff 4db61415012538f386ae3e128f54e11872bc82a2 c5f7a5d2485db0a97ee61ae5c93074067e43f555` | 2026-11-27T10:02:53.245922+00:00 | 2026-11-27T10:02:53.249644+00:00 | 0 |
| `diff --name-status c5f7a5d2485db0a97ee61ae5c93074067e43f555 a0b8dbe181441757973182389fa59abbf59b1c99` | 2026-11-27T10:02:53.253842+00:00 | 2026-11-27T10:02:53.257593+00:00 | 0 |
| `diff c5f7a5d2485db0a97ee61ae5c93074067e43f555 a0b8dbe181441757973182389fa59abbf59b1c99` | 2026-11-27T10:02:53.261756+00:00 | 2026-11-27T10:02:53.265639+00:00 | 0 |
| `diff --name-status a0b8dbe181441757973182389fa59abbf59b1c99 b477562bcb98dd49c4a929ac5592109f29d2e5a1` | 2026-11-27T10:02:53.269734+00:00 | 2026-11-27T10:02:53.273270+00:00 | 0 |
| `diff a0b8dbe181441757973182389fa59abbf59b1c99 b477562bcb98dd49c4a929ac5592109f29d2e5a1` | 2026-11-27T10:02:53.277294+00:00 | 2026-11-27T10:02:53.281806+00:00 | 0 |
| `diff --name-status b477562bcb98dd49c4a929ac5592109f29d2e5a1 7582695b082e0624438b70631ab2d77e5c199534` | 2026-11-27T10:02:53.286343+00:00 | 2026-11-27T10:02:53.289966+00:00 | 0 |
| `diff b477562bcb98dd49c4a929ac5592109f29d2e5a1 7582695b082e0624438b70631ab2d77e5c199534` | 2026-11-27T10:02:53.293931+00:00 | 2026-11-27T10:02:53.297393+00:00 | 0 |
| `rev-parse 4db61415012538f386ae3e128f54e11872bc82a2:normalizer.py` | 2026-11-27T10:02:53.302022+00:00 | 2026-11-27T10:02:53.305437+00:00 | 0 |
| `rev-parse c5f7a5d2485db0a97ee61ae5c93074067e43f555:normalizer.py` | 2026-11-27T10:02:53.309414+00:00 | 2026-11-27T10:02:53.312207+00:00 | 0 |
| `rev-parse a0b8dbe181441757973182389fa59abbf59b1c99:normalizer.py` | 2026-11-27T10:02:53.316192+00:00 | 2026-11-27T10:02:53.319386+00:00 | 0 |
| `rev-parse b477562bcb98dd49c4a929ac5592109f29d2e5a1:normalizer.py` | 2026-11-27T10:02:53.323328+00:00 | 2026-11-27T10:02:53.326742+00:00 | 0 |
| `rev-parse 7582695b082e0624438b70631ab2d77e5c199534:normalizer.py` | 2026-11-27T10:02:53.330638+00:00 | 2026-11-27T10:02:53.333828+00:00 | 0 |
| `show 4db61415012538f386ae3e128f54e11872bc82a2:normalizer.py` | 2026-11-27T10:02:53.337802+00:00 | 2026-11-27T10:02:53.341043+00:00 | 0 |
| `rev-parse 4db61415012538f386ae3e128f54e11872bc82a2:tests/test_normalizer.py` | 2026-11-27T10:02:53.344972+00:00 | 2026-11-27T10:02:53.348193+00:00 | 0 |
| `rev-parse c5f7a5d2485db0a97ee61ae5c93074067e43f555:tests/test_normalizer.py` | 2026-11-27T10:02:53.352052+00:00 | 2026-11-27T10:02:53.355517+00:00 | 0 |
| `rev-parse a0b8dbe181441757973182389fa59abbf59b1c99:tests/test_normalizer.py` | 2026-11-27T10:02:53.359563+00:00 | 2026-11-27T10:02:53.362872+00:00 | 0 |
| `rev-parse b477562bcb98dd49c4a929ac5592109f29d2e5a1:tests/test_normalizer.py` | 2026-11-27T10:02:53.366961+00:00 | 2026-11-27T10:02:53.370644+00:00 | 0 |
| `rev-parse 7582695b082e0624438b70631ab2d77e5c199534:tests/test_normalizer.py` | 2026-11-27T10:02:53.374628+00:00 | 2026-11-27T10:02:53.378030+00:00 | 0 |
| `show 4db61415012538f386ae3e128f54e11872bc82a2:tests/test_normalizer.py` | 2026-11-27T10:02:53.381892+00:00 | 2026-11-27T10:02:53.386013+00:00 | 0 |
| `rev-parse 4db61415012538f386ae3e128f54e11872bc82a2:.github/workflows/ci.yml` | 2026-11-27T10:02:53.389965+00:00 | 2026-11-27T10:02:53.393184+00:00 | 0 |
| `rev-parse c5f7a5d2485db0a97ee61ae5c93074067e43f555:.github/workflows/ci.yml` | 2026-11-27T10:02:53.396987+00:00 | 2026-11-27T10:02:53.400391+00:00 | 0 |
| `rev-parse a0b8dbe181441757973182389fa59abbf59b1c99:.github/workflows/ci.yml` | 2026-11-27T10:02:53.404634+00:00 | 2026-11-27T10:02:53.407873+00:00 | 0 |
| `rev-parse b477562bcb98dd49c4a929ac5592109f29d2e5a1:.github/workflows/ci.yml` | 2026-11-27T10:02:53.411790+00:00 | 2026-11-27T10:02:53.415025+00:00 | 0 |
| `rev-parse 7582695b082e0624438b70631ab2d77e5c199534:.github/workflows/ci.yml` | 2026-11-27T10:02:53.419023+00:00 | 2026-11-27T10:02:53.422799+00:00 | 0 |
| `show 4db61415012538f386ae3e128f54e11872bc82a2:.github/workflows/ci.yml` | 2026-11-27T10:02:53.427073+00:00 | 2026-11-27T10:02:53.430543+00:00 | 0 |
| `rev-parse 4db61415012538f386ae3e128f54e11872bc82a2:README.md` | 2026-11-27T10:02:53.434422+00:00 | 2026-11-27T10:02:53.437659+00:00 | 0 |
| `rev-parse c5f7a5d2485db0a97ee61ae5c93074067e43f555:README.md` | 2026-11-27T10:02:53.441503+00:00 | 2026-11-27T10:02:53.444579+00:00 | 0 |
| `rev-parse a0b8dbe181441757973182389fa59abbf59b1c99:README.md` | 2026-11-27T10:02:53.448359+00:00 | 2026-11-27T10:02:53.451703+00:00 | 0 |
| `rev-parse b477562bcb98dd49c4a929ac5592109f29d2e5a1:README.md` | 2026-11-27T10:02:53.455716+00:00 | 2026-11-27T10:02:53.459645+00:00 | 0 |
| `rev-parse 7582695b082e0624438b70631ab2d77e5c199534:README.md` | 2026-11-27T10:02:53.463479+00:00 | 2026-11-27T10:02:53.467733+00:00 | 0 |
| `show 4db61415012538f386ae3e128f54e11872bc82a2:README.md` | 2026-11-27T10:02:53.472024+00:00 | 2026-11-27T10:02:53.475801+00:00 | 0 |
| `rev-parse a0b8dbe181441757973182389fa59abbf59b1c99:evidence/G3-C1.md` | 2026-11-27T10:02:53.479901+00:00 | 2026-11-27T10:02:53.483822+00:00 | 0 |
| `rev-parse b477562bcb98dd49c4a929ac5592109f29d2e5a1:evidence/G3-C1.md` | 2026-11-27T10:02:53.487956+00:00 | 2026-11-27T10:02:53.491641+00:00 | 0 |
| `rev-parse 7582695b082e0624438b70631ab2d77e5c199534:evidence/G3-C1.md` | 2026-11-27T10:02:53.495473+00:00 | 2026-11-27T10:02:53.498570+00:00 | 0 |
| `show a0b8dbe181441757973182389fa59abbf59b1c99:evidence/G3-C1.md` | 2026-11-27T10:02:53.502399+00:00 | 2026-11-27T10:02:53.506045+00:00 | 0 |
| `rev-parse a0b8dbe181441757973182389fa59abbf59b1c99:reviews/G3-C1.md` | 2026-11-27T10:02:53.510271+00:00 | 2026-11-27T10:02:53.513941+00:00 | 0 |
| `rev-parse b477562bcb98dd49c4a929ac5592109f29d2e5a1:reviews/G3-C1.md` | 2026-11-27T10:02:53.518156+00:00 | 2026-11-27T10:02:53.521369+00:00 | 0 |
| `rev-parse 7582695b082e0624438b70631ab2d77e5c199534:reviews/G3-C1.md` | 2026-11-27T10:02:53.525139+00:00 | 2026-11-27T10:02:53.528387+00:00 | 0 |
| `show a0b8dbe181441757973182389fa59abbf59b1c99:reviews/G3-C1.md` | 2026-11-27T10:02:53.532484+00:00 | 2026-11-27T10:02:53.535978+00:00 | 0 |
| `show 4db61415012538f386ae3e128f54e11872bc82a2:plans/active-execplan.md` | 2026-11-27T10:02:53.540070+00:00 | 2026-11-27T10:02:53.543458+00:00 | 0 |
| `show c5f7a5d2485db0a97ee61ae5c93074067e43f555:plans/active-execplan.md` | 2026-11-27T10:02:53.547531+00:00 | 2026-11-27T10:02:53.551433+00:00 | 0 |
| `show a0b8dbe181441757973182389fa59abbf59b1c99:plans/active-execplan.md` | 2026-11-27T10:02:53.555594+00:00 | 2026-11-27T10:02:53.559489+00:00 | 0 |
| `show a0b8dbe181441757973182389fa59abbf59b1c99:state/ledger.json` | 2026-11-27T10:02:53.563699+00:00 | 2026-11-27T10:02:53.567486+00:00 | 0 |
| `show c5f7a5d2485db0a97ee61ae5c93074067e43f555:state/ledger.json` | 2026-11-27T10:02:53.571613+00:00 | 2026-11-27T10:02:53.575303+00:00 | 0 |
| `show 4db61415012538f386ae3e128f54e11872bc82a2:state/ledger.json` | 2026-11-27T10:02:53.579749+00:00 | 2026-11-27T10:02:53.583170+00:00 | 0 |

The programme manager must combine actual intervals across all four distinct workers with verified native Starts and actual first holds; this report alone cannot establish four-way overlap. Step 8 RETURN remains open. After separate publication of this report, pause the ledger, retain the original evidence pins and clear the assignment; no independent verdict or successor is authorised. The first pause and original publication/readback times are recorded separately.
