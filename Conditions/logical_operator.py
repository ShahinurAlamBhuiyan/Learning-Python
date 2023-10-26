has_high_income = False
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan.")
elif has_good_credit or has_high_income:
    print("Okay for load.")
else:
    print("Not eligible for loan.")

# if applicant has good credit and doesn't have any criminal record
has_good_credit = True
has_criminal_records = False

if has_good_credit and not has_criminal_records:
    print("Good people.")
