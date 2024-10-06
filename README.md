[![CI](https://github.com/nogibjj/Wenye_Li_Mini_Project_5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Wenye_Li_Mini_Project_5/actions/workflows/cicd.yml)

## Wenye Li Mini Project 5

## Requirements

Connect to a SQL database
Perform CRUD operations
Write at least two different SQL queries

## Deliverables

- Python script: Please check **extract.py**, **transform_load.py**, and **query.py**
- Screenshot or log of successful database operations: Please check **db_operations.md**

## Project Structures

- `Makefile`:

- `requirements.txt`

- `mylib`:

  - **extract.py**
  - **transform_load**
  - **queryt**

- `main.py`

- `test_main.py`

- `README.me`

- `cicd.yml`

- `devcontainer`

- `DrugUse.db`

## Dataset

| Header                    | Definition                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------- |
| `alcohol-use`             | Percentage of those in an age group who used alcohol in the past 12 months              |
| `alcohol-frequency`       | Median number of times a user in an age group used alcohol in the past 12 months        |
| `marijuana-use`           | Percentage of those in an age group who used marijuana in the past 12 months            |
| `marijuana-frequency`     | Median number of times a user in an age group used marijuana in the past 12 months      |
| `cocaine-use`             | Percentage of those in an age group who used cocaine in the past 12 months              |
| `cocaine-frequency`       | Median number of times a user in an age group used cocaine in the past 12 months        |
| `crack-use`               | Percentage of those in an age group who used crack in the past 12 months                |
| `crack-frequency`         | Median number of times a user in an age group used crack in the past 12 months          |
| `heroin-use`              | Percentage of those in an age group who used heroin in the past 12 months               |
| `heroin-frequency`        | Median number of times a user in an age group used heroin in the past 12 months         |
| `hallucinogen-use`        | Percentage of those in an age group who used hallucinogens in the past 12 months        |
| `hallucinogen-frequency`  | Median number of times a user in an age group used hallucinogens in the past 12 months  |
| `inhalant-use`            | Percentage of those in an age group who used inhalants in the past 12 months            |
| `inhalant-frequency`      | Median number of times a user in an age group used inhalants in the past 12 months      |
| `pain-releiver-use`       | Percentage of those in an age group who used pain relievers in the past 12 months       |
| `pain-releiver-frequency` | Median number of times a user in an age group used pain relievers in the past 12 months |
| `oxycontin-use`           | Percentage of those in an age group who used oxycontin in the past 12 months            |
| `oxycontin-frequency`     | Median number of times a user in an age group used oxycontin in the past 12 months      |
| `tranquilizer-use`        | Percentage of those in an age group who used tranquilizer in the past 12 months         |
| `tranquilizer-frequency`  | Median number of times a user in an age group used tranquilizer in the past 12 months   |
| `stimulant-use`           | Percentage of those in an age group who used stimulants in the past 12 months           |
| `stimulant-frequency`     | Median number of times a user in an age group used stimulants in the past 12 months     |
| `meth-use`                | Percentage of those in an age group who used meth in the past 12 months                 |
| `meth-frequency`          | Median number of times a user in an age group used meth in the past 12 months           |
| `sedative-use`            | Percentage of those in an age group who used sedatives in the past 12 months            |
| `sedative-frequency`      | Median number of times a user in an age group used sedatives in the past 12 months      |

## CRUD Operations：

- **`read`** </br>
  Retrieving all records from the DrugUse.db table.

- **`create`** </br>
  Inserting a new record into the DrugUse.db table with predefined values.

- **`delete`** </br>
  Deleting a row from the DrugUse.db table.

- **`update`** </br>
  Updating an existing row from the DrugUse.db table.
