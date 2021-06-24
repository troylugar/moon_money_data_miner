delete from submissions
where "guid" not in (
        select "guid"
        from (
                select "id",
                    MAX("date_added_utc") as "date_added_utc"
                from submissions
                group by "id"
            ) a
            join submissions b on a."id" = b."id"
            and a."date_added_utc" = b."date_added_utc"
    );