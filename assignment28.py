def check_baggage(baggage_weight):
    if(baggage_weight >= 0 and baggage_weight < 40):
        return True
    else:
        return False
def check_immigration(expiry_year):
    if(expiry_year >= 2001 and expiry_year <= 2025):
        return True
    else:
        return False

def check_security(noc_status):
    if(noc_status == 'VALID' or noc_status == 'valid'):
        return True
    else:
        return False

def traveler():
    traveler_id = 1002
    traveler_name = "Cook"
    if(check_baggage(45) and check_immigration(2019) and check_security("VALID")):
        print(traveler_id,traveler_name)
        print("Allow Traveller to Fly!")
    else:
        print(traveler_id,traveler_name)
        print("Detain Traveller for re-checking.")
traveler()

# OUTPUT
# 1001 Jim
# Allow Traveller to Fly!
# 1002 Cook
# Detain Traveller for re-checking.