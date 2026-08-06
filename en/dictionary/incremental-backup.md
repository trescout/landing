# What is Incremental Backup?

It is a backup method that saves time and space by saving only the files that have changed since the last backup.

## Overview
Incremental backup detects only recent changes and adds them, rather than copying all the data each time. This method significantly shortens backup time and allows you to use storage space efficiently. It is an indispensable strategy for large data sets.

*Analogy: Instead of rewriting an entire book every day, it's like writing only the pages added that day into a notebook and adding them.*

## How it works
The system checks the last modification date of the files. It only adds changed or newly added parts to the backup file.

## Where it is used
It is used in corporate databases, large file servers and professional backup systems.

## Commonly confused with
It should not be confused with full backup; a full backup copies everything every time.

## Frequently asked questions
**Is it difficult when restoring?**
Yes, it is a little more complicated than a full backup as all the parts need to be combined.

**How often should it be done?**
It can be done daily or hourly, depending on your data exchange rate.


## Related terms
- [Backup Program](/en/dictionary/backup-program/)
- [Data Pipeline](/en/dictionary/data-pipeline/)

## Related tools
- [Restic](/en/discover/restic/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/incremental-backup/
