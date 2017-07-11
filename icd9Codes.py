#Neoplasia codes
neoplasia_codes = [179,185,193,220,226,23699]
neoplasia_codes.extend(range(1400,2398))
neoplasia_codes.extend(range(17300,17400))
neoplasia_codes.extend(range(19881,19890))
neoplasia_codes.extend(range(20382,22390))
neoplasia_codes.extend(range(23690,23692))
neoplasia_codes.extend(range(25802,25804))

#Hypertension codes
hypertension_codes = range(4010,4021)
hypertension_codes.extend(range(40501,40600))

#Diabetes codes
diabetes_code = [2535,2537]
diabetes_code.extend(range(25000,25003))

#Lipid Disorders
lipid_disorders = range(2721,2730)

#Cardiovascular Disorders
cardiovascular_disorders = range(42511,42519)
cardiovascular_disorders.extend(range(4252,4294))
cardiovascular_disorders.extend(range(3900,4600))
cardiovascular_disorders.extend(range(42700,42900))

# Function to assign label
def assign_label(x):
    label = x
    if x in neoplasia_codes:
        label = "neoplasia"
    elif x in hypertension_codes:
        label = "hypertension"
    elif x in diabetes_code:
        label = "diabetes"
    elif x in lipid_disorders:
        label = "lipid_disorders"
    elif x in cardiovascular_disorders:
        label = "cardiovascular_disorders"
    else:
        label = None
    return label

