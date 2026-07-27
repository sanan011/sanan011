# Profile README — Setup & Customization Guide

This document covers everything that doesn't belong inline in `README.md`: the repository analysis behind the design decisions, the folder structure, every external dependency, installation steps, customization points, performance notes, and where to take this next.

---

## 1. Repository Analysis

Sanan's account (`sanan011`) currently has **34 non-fork public repositories**. Below is a ranked breakdown by relevance to the "Senior Backend Engineer — Java / Spring Boot / Microservices" positioning the README targets.

### Tier 1 — Pin these six

| # | Repository | Why it's Tier 1 |
|---|---|---|
| 1 | **`unibank-smartorder`** | The strongest single proof point on the account: a *delivered* microservices system (order/payment/notification) from a real internship, with 22 passing tests, 8/8 green CI checks, a tagged `v1.0.0` release, and full observability (Prometheus/Grafana). This is production discipline, not a tutorial project. |
| 2 | **`smartorder`** | The architectural ceiling of the account — Kafka, Eureka, Spring Cloud Gateway, Elasticsearch, MinIO, Zipkin tracing, a Next.js 14 storefront. Shown *alongside* `unibank-smartorder`, it tells a coherent story: ambitious R&D first, disciplined delivery second. |
| 3 | **`library-management-api`** | Currently active (last pushed today). Shows present-tense engineering, not just past work — evidence of an ongoing internship at DevJoint with graded architectural standards (DTOs, centralized exceptions, pagination, Swagger). |
| 4 | **`jwt-auth-api`** | A focused, single-purpose service. Auth/security work is disproportionately valued in backend hiring, and this repo demonstrates a real understanding of 401 vs. 403 semantics — a detail many portfolios get wrong. |
| 5 | **`least-privilege-advisor`** | The only non-Java, non-web project on the account, and it's a security-tooling CLI. This is what earns the "backend engineer with range" read rather than "Java-only bootcamp grad" — it costs nothing to include and adds real differentiation. |
| 6 | **`java-database-capstone`** | Rounds out the six with a data-modeling-focused project (Smart Clinic Management System), reinforcing the database/persistence side of the stack without repeating the microservices theme already covered above. |

### Tier 2 — Solid, not pin-worthy

- `Java-Tasks`, `My-Tasks` — core Java exercises; useful evidence of fundamentals but not differentiated enough to feature.
- `openwebrx-clone-project` / `OpenWebRX` — a frontend simulation of an SDR interface, tied to the TÜBİTAK BİLGEM internship. Good timeline context, not a backend showcase.
- `github-final-project` — a Git/GitHub fundamentals exercise (simple-interest calculator). Useful as a timeline marker, not a portfolio piece.
- `Hangman`, `musicPlayer` — small Java practice projects.
- `EduXpert`, `AspireLearn` — C# projects with no README/documentation; can't be evaluated for quality without more context, and undocumented repos rarely help a portfolio regardless of the code inside.

### Tier 3 — Coursework / early fundamentals (2024)

`AlgoMap-solutions`, `Access_Control_App`, `UserAccessControl`, `ProductManager`, `ProductMaster`, `PhoneBook`, `Turbo.az`, `Contact-Keeper`, `Basic-bank-app`, `ContactFileService`, `MyList`, `MyException`, `ExamHub`, `Currency-Converter-Web-App`, `Calculator-Program`, `Student-Registration-Form`, `TaskNest`, `Object-task` — C#, HTML/CSS/JS coursework from the Institute of Management Systems and the Cybernetics Academy fullstack course. These establish the starting point of the timeline but shouldn't be pinned or featured; they predate the backend specialization by roughly a year and would dilute the "senior backend engineer" positioning if surfaced prominently.

### Important: your current pinned repos don't match this positioning

As of this analysis, the six repos pinned on the profile are `Object-task`, `Student-Registration-Form`, `TaskNest`, `sanan011`, `AlgoMap-solutions`, and `Calculator-Program` — all Tier 3, all from 2024. None of them are Java, none involve Spring Boot, and none reflect the microservices/backend work that's actually your strongest material. **Repinning to the Tier 1 list above is the single highest-leverage change you can make** — it costs nothing and immediately changes what a visitor sees first.

To repin: go to your profile → **Customize your pins** → select the six Tier 1 repositories listed above.

---

## 2. Banner Recommendation

The README uses a **Capsule Render `waving` banner** in a navy-to-charcoal gradient (`#0A192F → #16213E → #1B2735`) with gold text (`#FFC947`). This isn't an arbitrary choice: it mirrors the dark-navy-and-gold theme already used in the Unibank internship report deck, so the profile reads as a consistent personal brand rather than a generic template palette.

If you'd rather commission a custom static banner instead of the generated one:
- Keep the same hex values (`#0A192F` background, `#FFC947` accent) so it stays consistent with the stats cards and trophy theme.
- 1500×400px is the safe size for both desktop and mobile GitHub rendering.
- Tools: [Canva](https://canva.com) (fastest), or [Figma](https://figma.com) if you want pixel-level control.
- Save it to `assets/banner.png` in this repo and replace the Capsule Render `<img>` at the top of `README.md` with `<img src="assets/banner.png" width="100%" />`.

---

## 3. Folder Structure

```
sanan011/                          (this repo — must match your username exactly)
├── README.md                      # The profile page itself
├── SETUP_GUIDE.md                 # This file — not shown on your profile
├── .github/
│   └── workflows/
│       ├── update-readme.yml      # Recent Activity + Latest Repositories
│       ├── snake.yml              # Contribution snake animation
│       └── metrics.yml            # Auto-generated metrics image
├── scripts/
│   └── update_readme.py           # Latest-repositories fetch + inject logic
└── assets/                        # Optional: custom banner/images if you
                                    # move off the generated Capsule Render one
```

The `output` branch referenced by the snake workflow is created automatically the first time `snake.yml` runs — you don't need to create it manually.

---

## 4. External Dependencies

Everything below is a hosted, free, no-signup service or a public GitHub Action. Nothing requires an API key except where noted.

| Service | Used for | Auth required? |
|---|---|---|
| [Capsule Render](https://github.com/kyechan99/capsule-render) | Header/footer banner | No |
| [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) | Animated typing text | No |
| [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) | Stats card, top languages | No |
| [github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) | Streak stats | No |
| [github-readme-activity-graph](https://github.com/Ashutosh00710/github-readme-activity-graph) | Contribution graph | No |
| [github-profile-trophy](https://github.com/ryo-ma/github-profile-trophy) | Trophy case | No |
| [Platane/snk](https://github.com/Platane/snk) | Snake contribution animation | No (Action, uses default `GITHUB_TOKEN`) |
| [lowlighter/metrics](https://github.com/lowlighter/metrics) | Auto-generated metrics image | Optional PAT (`METRICS_TOKEN`) for private-repo stats and extra plugins; public data works with the default token |
| [jamesgeorge007/github-activity-readme](https://github.com/jamesgeorge007/github-activity-readme) | Recent Activity section | No |
| [komarev.com/ghpvc](https://github.com/antonkomarev/github-profile-views-counter) | Profile view counter | No |
| [quotes-github-readme](https://github.com/PiyushSuthar/quotes-github-readme) | Developer quote | No |
| [skillicons.dev](https://skillicons.dev) | Tech stack icon rows | No |
| [Shields.io](https://shields.io) | Individual badges (RabbitMQ, Kafka, JWT, etc.) | No |
| [requests](https://pypi.org/project/requests/) (Python) | Used by `scripts/update_readme.py` | No |

---

## 5. Installation Steps

1. **Create (or reuse) the special profile repository.** It must be named exactly `sanan011` (your username) and be public.
2. **Copy these files into it**, preserving the folder structure above:
   - `README.md`
   - `.github/workflows/update-readme.yml`
   - `.github/workflows/snake.yml`
   - `.github/workflows/metrics.yml`
   - `scripts/update_readme.py`
3. **Commit and push to `main`.**
4. **(Optional, recommended) Add a `METRICS_TOKEN` secret** for the metrics workflow to unlock private-repo stats and extra plugins:
   - GitHub → Settings → Developer settings → Personal access tokens → generate a classic token with the `repo` scope.
   - In the `sanan011` repo → Settings → Secrets and variables → Actions → New repository secret → name it `METRICS_TOKEN`.
   - If you skip this, the workflow still runs using the default `GITHUB_TOKEN` with public-data-only plugins.
5. **Run each workflow once manually** (Actions tab → select workflow → "Run workflow") rather than waiting for the schedule, so the snake SVGs and metrics image exist before your first visitor arrives.
6. **Repin your Tier 1 repositories** as described in Section 1.
7. **Verify the rendered README** on your profile page — the snake animation and metrics image will take one workflow run (a few minutes) to appear.

---

## 6. Customization Guide

- **Color theme:** every stats/streak/trophy URL takes hex color parameters. To change the accent from gold (`FFC947`) to something else, find-and-replace that hex code across `README.md` — all the cards will update consistently.
- **Typing SVG lines:** edit the `lines=` parameter in the typing SVG URL (semicolon-separated, URL-encoded).
- **Featured Projects:** the table in `README.md` is plain HTML inside Markdown — add or remove `<td>` blocks as your active project mix changes. Keep it to an even number for the two-column grid to stay balanced.
- **Career Timeline:** update the table rows as new milestones happen — internships ending, certificates completed, the eventual graduate program.
- **WakaTime:** not currently connected (no coding-time tracking service found on this account). If you set one up later, add `wakatime-readme` (Cranium/waka-readme-stats) as an additional workflow and a "Coding Activity" section — don't add the badge before the account exists, or it will render empty/broken.
- **Blog / RSS:** no blog was found for this account. If you start one, `gautamkrishnar/blog-post-workflow` is the standard Action for auto-pulling recent posts into a marked README section.
- **Recent Activity cadence:** the default is every 6 hours. Drop to `0 */3 * * *` (every 3 hours) if you push more frequently and want fresher activity data, at the cost of slightly more Action minutes used.

---

## 7. Performance Optimizations

- All stats/graph images are served from Vercel-hosted edge functions with caching — no action needed, but avoid stacking more than the current ~6 dynamic images, since each is a separate HTTP request on profile load.
- The snake and metrics workflows write to the repository (or the `output` branch) rather than regenerating on every page view, so profile visitors load a static, cached SVG instead of triggering computation — this is the fastest option for the snake animation specifically.
- `hide_border=true` and `no-frame=true` are set throughout to reduce visual weight and shave a small amount of rendered SVG size.
- Keep the `plugin_languages_analysis_timeout` in `metrics.yml` reasonably low (currently 15s) — a higher value increases workflow run time without meaningfully changing the output for an account this size.

---

## 8. Future Improvements

- Once `unibank-smartorder` or `smartorder` has a live demo deployment, add a "Live Demo" badge/link to the relevant Featured Project card.
- If a WakaTime or Wakapi account is set up, add a weekly coding-time breakdown — this is a natural next differentiator once the current backend work stabilizes.
- Consider a short architecture write-up (a `/docs` folder or a blog post) walking through the SAGA/Outbox implementation in `unibank-smartorder` — this is genuinely uncommon at the internship level and would stand out linked from the README.
- As the DevJoint internship produces more repositories, fold the strongest of them into the Featured Projects section and retire the weakest current Tier 1 entry to keep the section at a disciplined six.
- Once graduate-school applications are underway, consider adding a one-line "Open to: research collaborations in distributed systems" call-to-action near the top of the About section.
