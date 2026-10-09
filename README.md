# Digital Permit & License Management System
---

## Project Description

The **Digital Permit & License Management System** is a Python-based Object-Oriented application that allows government agencies and authorized users to create, store, update, and validate digital permits and licenses.  

The system uses only anonymized identifiers and non-sensitive information (no real names, national ID numbers, phone numbers, or addresses). It is deliberately designed to follow **Digital Public Goods (DPG)** principles so that it can be openly shared, reused, and improved by others.

This project demonstrates the core OOP concepts taught in Lectures 1–3:
- Classes and Objects
- Attributes and Methods
- Instance methods, Class methods (`@classmethod`), and Static methods (`@staticmethod`)
- One Python data structure (dictionary) to store multiple objects

---

## Features

- Create standard **Permits** (Business, Construction, etc.)
- Create standard **Licenses** (Professional, Trading, etc.)
- Store multiple records in a **dictionary** (ID as key)
- Display all records or look up a specific record by ID
- Update the status of any permit or license
- Check whether a record is still valid
- Validate ID formats using static methods
- Fully anonymized and privacy-respecting data model

---

## How This Solution Aligns with Digital Public Goods (DPG) Principles

| DPG Principle                      | How it is implemented in this project |
|------------------------------------|---------------------------------------|
| **Open-source**                    | Complete source code is published on GitHub under an open license. Anyone can view, fork, modify, and reuse it. |
| **Inclusive and accessible design**| Simple command-line interface with clear English messages. No complex graphical interface or advanced technical skills are required. |
| **Privacy-respecting**             | Only anonymized IDs (e.g. `PMT-2026-001`, `LIC-2026-001`), categories, dates, and status are stored. No sensitive personal data is collected or saved. |
| **Modular and reusable**           | Code is cleanly separated into two independent classes (`Permit` and `License`) plus helper functions. The structure can easily be extended for other government services. |

---

## Technical Requirements Met

### Task 1 – OOP Basics
- Two classes: `Permit` and `License`
- Attributes: ID, type, category, issue date, expiry date, status
- Methods: `display_info()`, `update_status()`, `is_valid()`
- Object creation and interaction demonstrated

### Task 2 – Python Data Structures
- One data structure used: **Dictionary** (`registry`)
- Key = unique ID, Value = Permit or License object
- Functions: `add_record()`, `display_all_records()`, `display_record_by_id()`, `count_records()`

### Task 3 – Methods
- Instance methods: `display_info()`, `update_status()`, `is_valid()`
- Class methods: `create_standard()` (in both classes)
- Static methods: `validate_id_format()` (in both classes)

---

## How to Run the Program

1. Make sure Python 3 is installed on your computer.
2. Open a terminal / command prompt.
3. Navigate to the folder containing the file.
4. Run the following command:

```bash
python permit_license_system.py

