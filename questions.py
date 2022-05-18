# functions handling each question
import csv
from datetime import datetime


# loads dataset
def question_one():
    
    with open(r"data_file\Python Developer Test Dataset.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            yield row


# returns data with lease years = 25 years
def question_two(rows_obj):

    rows = list(rows_obj)
    twentyfive_lease_years = [row for row in rows if row["Lease Years"] == "25"]

    return twentyfive_lease_years


# returns dict object with tenant and mast count
def question_three(rows_obj):
    
    tenant_list = []

    for row in rows_obj:
        tenant_list.append(row["Tenant Name"])
    
    arqiva_mast_count = 0
    vodafone_mast_count = 0
    o2_mast_count = 0
    everything_mast_count = 0
    cornerstone_mast_count = 0

    for item in tenant_list:
        
        if "Arqiva" in item:
            arqiva_mast_count += 1
        elif "Vodafone" in item:
            vodafone_mast_count += 1
        elif "O2" in item:
            o2_mast_count += 1
        elif "Everything" in item:
            everything_mast_count += 1
        elif "Cornerstone" in item:
            cornerstone_mast_count += 1
    
    return {
        "Arqiva": arqiva_mast_count,
        "Vodafone": vodafone_mast_count,
        "O2": o2_mast_count,
        "Everything": everything_mast_count,
        "Cornerstone": cornerstone_mast_count
    }


# returns rental object with lease start date between 01-06-99 and 31-08-07
def question_four(rows_obj):
    
    start_date_range_obj = datetime(1999, 6, 1).date()
    end_date_range_obj = datetime(2007, 8, 31).date()

    rental_data = []

    for row in rows_obj:
    
        lease_date = datetime.strptime(row["Lease Start Date"], "%d %b %Y").date()
        row["Lease Start Date"] = lease_date

        rental_data.append(row)
    
    for item in rental_data:
        if item["Lease Start Date"] > start_date_range_obj and item["Lease Start Date"] < end_date_range_obj:
            yield item


