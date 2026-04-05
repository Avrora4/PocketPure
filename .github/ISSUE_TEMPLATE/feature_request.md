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
