---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

## Overview
Example: Enable batch transaction registration by uploading a CSV file.

## Context / Why
Example: Manually entering dozens of card transactions every month is time-consuming and cuts into the 1.5-hour development window.

## Acceptance Criteria / Definition of Done
- [ ] A button for CSV upload is placed in the UI
- [ ] The backend (FastAPI) can receive and parse the CSV
- [ ] The parsed data is saved in bulk to the `transactions` table
- [ ] The UI table automatically reloads after saving is complete

## Notes / References
- FastAPI file upload specifications: https://fastapi.tiangolo.com/tutorial/request-files/

## Related Issue
Closes #

## What and Why
- Purpose: 
- Summary: 

## Details
- 
- 

## How to Test
1. Start the DB using `docker-compose up -d`
2. Start the backend and frontend
3. Access `http://localhost:5173/`, enter test data into the form, and submit
4. Confirm that it is immediately reflected in the list

## Screenshots
| Before | After |
| :---: | :---: |
| (Image URL) | (Image URL) |

## Checklist
- [ ] No errors or warnings in the console
- [ ] Executed Linter/Formatter (`Prettier`, `Ruff`)
- [ ] Updated environment variable documentation such as `.env.example` (if necessary)
