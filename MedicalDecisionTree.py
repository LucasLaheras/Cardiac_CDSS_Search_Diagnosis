def decisionMedicalTree(characteristics):
    if characteristics['Acute coronary syndrome (ACS) ST segment elevation'] > 0 or characteristics[
        'Acute coronary syndrome (ACS) ST segment elevation'] is None:
        if characteristics['slope'] == "downsloping" or characteristics['slope'] == "upsloping":
            return "1 mm or more ST segment elevation"

    elif characteristics['shortness of breath'] > 0 or characteristics['shortness of breath'] is None:
        if characteristics['Exercise induced angina'] == 0:
            return 'left bundle branch block'

    if characteristics['Acute coronary syndrome (ACS) ST segment elevation'] > 0.1:
        # Level 2: Checking for atherosclerosis instability
        if characteristics['acute instability of atherosclerosis']:
            return "Acute myocardial infarction with ST segment elevation"
        else:
            # Level 3: Checking pain intensity
            if characteristics['pain intensity'] == 'high':
                return "Type 1 AMI"
            else:
                return "Type 2 AMI"
    else:
        # Level 2: Checking for shortness of breath and blood pressure
        if characteristics['shortness of breath']:
            if characteristics['The person’s resting blood pressure'] > 150:
                return "Atrial fibrillation"
            else:
                return "Type 3 AMI"
        else:
            # Level 3: Checking pain duration and cholesterol
            if characteristics['duration of pain per hour of the day'] > 2 and characteristics['cholesterol'] > 200:
                return "Type 4 AMI"
            else:
                return "Type 5 AMI"

        # Evaluate and treat reversible causes
        treat_reversible_causes = input("Have reversible causes been treated? (yes/no): ")
        if treat_reversible_causes.lower() != 'yes':
            print("Treat reversible causes before proceeding.")
            return

        # Moderate or severe symptoms
        severe_symptoms = input("Does the patient have moderate or severe symptoms? (yes/no): ")
        if severe_symptoms.lower() == 'yes':
            print("Administer Atropine")

            # Medication intoxication
            medication_intoxication = input("Does the patient have medication intoxication? (yes/no): ")
            if medication_intoxication.lower() == 'yes':
                # Which medication?
                medication = input("Which medication? (calcium channel blocker/beta-blocker/digoxin): ").lower()
                if medication == 'calcium channel blocker':
                    print("Administer IV Calcium")
                elif medication == 'beta-blocker':
                    print("Administer IV Glucagon")
                elif medication == 'digoxin':
                    print("Administer anti-digoxin antibody")

                # High-dose insulin
                print("Administer high-dose insulin")
                symptoms_persist = input("Do the symptoms persist? (yes/no): ")
                if symptoms_persist.lower() == 'yes':
                    print("Administer transcutaneous/transvenous pacemaker")
            else:
                severe_symptoms = input("Does the patient have severe symptoms/hemodynamically unstable? (yes/no): ")
                if severe_symptoms.lower() == 'yes':
                    print("Administer transcutaneous/transvenous pacemaker")
                else:
                    AMI_with_AV_block = input("Does the patient have AMI with AV block? (yes/no): ")
                    if AMI_with_AV_block.lower() == 'yes':
                        print("Administer Aminophylline")
                    else:
                        print("Administer beta-agonists")
                        symptoms_continue = input("Do the symptoms continue? (yes/no): ")
                        if symptoms_continue.lower() == 'yes':
                            print("Administer transcutaneous/transvenous pacemaker")

# Acute coronary syndrome without ST segment elevation, acute myocardial infarction with ST segment elevation
