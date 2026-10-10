Here’s a clean, ready-to-use `README.md` for your GitHub repo:

```markdown
# Athlete Stat Tracker

A command-line application for tracking college basketball athletes, their season statistics, school/team performance, and draft information.

Built with Python and SQLite.

---

## Features

- Add and update athletes
- Record and update per-season athlete statistics
- Add schools and update team statistics
- Manage seasons and draft data
- View statistics by position
- Rank athletes by any major statistic
- Compare an athlete’s averages against their conference averages
- View individual athlete season stats or the full athlete roster

---

## Tech Stack

- **Python 3**
- **SQLite3** (built-in)
- No external dependencies

---

## Project Structure

```
├── main.py          # User interface (menu, prompts, display)
├── database.py      # Database connection and business logic
├── queries.py       # All SQL statements
└── data.db          # SQLite database (created automatically on first run)
```

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/demarcus-mitchell/Basketball-Database.git
   cd athlete-stat-tracker
   ```

2. Run the application:
   ```bash
   python main.py
   ```

On first launch the program automatically creates all required tables.

### Optional: Load Sample Data

Inside `main.py` you will find this line (commented out by default):

```python
# database.insert_synthetic_data()
```

Uncomment it, run the program once, then comment it out again.  
This loads:

- 4 schools (3 SEC + Gonzaga)
- 25 athletes
- 3 seasons
- 1 draft with 5 picks
- Full athlete and school statistics

---

## Menu Options

| #  | Action                              |
|----|--------------------------------------|
| 1  | Add Athlete                          |
| 2  | Add Athlete Stats                    |
| 3  | Update Athlete Stats                 |
| 4  | Add New School                       |
| 5  | Update School Stats                  |
| 6  | Add New Season                       |
| 7  | Add New Draft                        |
| 8  | Add Draft Pick                       |
| 9  | View Stats by Position               |
| 10 | View Athletes Ranked by Stat         |
| 11 | View Athlete vs Conference Averages  |
| 12 | View Athlete Stats                   |
| 13 | View All Athletes                    |
| 14 | Exit                                 |

---

## Database Schema Overview

**Core Tables**
- `athlete` – player information
- `athlete_stats` – per-season box score totals
- `school` – school / program information
- `school_stats` – per-season team totals
- `position` – position lookup (1–5)
- `season` – season identifiers
- `draft` / `draft_pick` – draft events and selections

The design keeps the schema simple while still supporting the required reporting features (position filters, ranking, conference comparisons, etc.).

---

## Design Notes

- `athlete_stats` and `school_stats` intentionally mirror each other to make player-vs-conference comparisons straightforward.
- Conference is stored directly on the `school` table instead of creating a separate conference entity.
- Only season-level aggregates are stored (no individual game table) to keep the model lean.

---

## License

This project was created for academic purposes.
```
