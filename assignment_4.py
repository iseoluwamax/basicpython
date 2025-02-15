from datetime import datetime, timedelta


def between_dates(start_date, end_date):


    """to acquire the number of days between 2 dates."""
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    result = start_date - end_date
    print(result.days)


start_date = "2025-01-07"
end_date = "2025-01-01"


between_dates(start_date, end_date)