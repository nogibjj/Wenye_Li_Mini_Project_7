**2024-10-15 23:25:33,999** - INFO - Successfully opened session 01ef8b6e-4dce-12a5-b1d2-35a4a8c7f2ef
**2024-10-15 23:25:35,413** - INFO - Executed query:

```sql

            WITH AgeStats AS (
                SELECT age,
                       AVG(alcohol_use) AS avg_alcohol_use,
                       AVG(marijuana_use) AS avg_marijuana_use
                FROM DrugUseDB
                GROUP BY age
            )
            SELECT d.age, d.n, d.alcohol_use, a.avg_alcohol_use,
            d.marijuana_use, a.avg_marijuana_use
            FROM DrugUseDB d
            JOIN AgeStats a
            ON d.age = a.age
            ORDER BY d.age ASC, d.n DESC

```

**2024-10-15 23:25:35,413** - INFO - Query results:
[Row(age='12', n=2798, alcohol_use=3.9000000953674316, avg_alcohol_use=3.9000000953674316, marijuana_use=1.100000023841858, avg_marijuana_use=1.100000023841858), Row(age='13', n=2757, alcohol_use=8.5, avg_alcohol_use=8.5, marijuana_use=3.4000000953674316, avg_marijuana_use=3.4000000953674316), Row(age='14', n=2792, alcohol_use=18.100000381469727, avg_alcohol_use=18.100000381469727, marijuana_use=8.699999809265137, avg_marijuana_use=8.699999809265137), Row(age='15', n=2956, alcohol_use=29.200000762939453, avg_alcohol_use=29.200000762939453, marijuana_use=14.5, avg_marijuana_use=14.5), Row(age='16', n=3058, alcohol_use=40.099998474121094, avg_alcohol_use=40.099998474121094, marijuana_use=22.5, avg_marijuana_use=22.5), Row(age='17', n=3038, alcohol_use=49.29999923706055, avg_alcohol_use=49.29999923706055, marijuana_use=28.0, avg_marijuana_use=28.0), Row(age='18', n=2469, alcohol_use=58.70000076293945, avg_alcohol_use=58.70000076293945, marijuana_use=33.70000076293945, avg_marijuana_use=33.70000076293945), Row(age='19', n=2223, alcohol_use=64.5999984741211, avg_alcohol_use=64.5999984741211, marijuana_use=33.400001525878906, avg_marijuana_use=33.400001525878906), Row(age='20', n=2271, alcohol_use=69.69999694824219, avg_alcohol_use=69.69999694824219, marijuana_use=34.0, avg_marijuana_use=34.0), Row(age='21', n=2354, alcohol_use=83.19999694824219, avg_alcohol_use=83.19999694824219, marijuana_use=33.0, avg_marijuana_use=33.0), Row(age='22-23', n=4707, alcohol_use=84.19999694824219, avg_alcohol_use=84.19999694824219, marijuana_use=28.399999618530273, avg_marijuana_use=28.399999618530273), Row(age='24-25', n=4591, alcohol_use=83.0999984741211, avg_alcohol_use=83.0999984741211, marijuana_use=24.899999618530273, avg_marijuana_use=24.899999618530273), Row(age='26-29', n=2628, alcohol_use=80.69999694824219, avg_alcohol_use=80.69999694824219, marijuana_use=20.799999237060547, avg_marijuana_use=20.799999237060547), Row(age='30-34', n=2864, alcohol_use=77.5, avg_alcohol_use=77.5, marijuana_use=16.399999618530273, avg_marijuana_use=16.399999618530273), Row(age='35-49', n=7391, alcohol_use=75.0, avg_alcohol_use=75.0, marijuana_use=10.399999618530273, avg_marijuana_use=10.399999618530273), Row(age='50-64', n=3923, alcohol_use=67.19999694824219, avg_alcohol_use=67.19999694824219, marijuana_use=7.300000190734863, avg_marijuana_use=7.300000190734863), Row(age='65+', n=2448, alcohol_use=49.29999923706055, avg_alcohol_use=49.29999923706055, marijuana_use=1.2000000476837158, avg_marijuana_use=1.2000000476837158)]
**2024-10-15 23:25:35,414** - INFO - Closing session 01ef8b6e-4dce-12a5-b1d2-35a4a8c7f2ef
