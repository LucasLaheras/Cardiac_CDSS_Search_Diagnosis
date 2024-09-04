def decisionMedicalTree(characteristics):
    if characteristics['Acute coronary syndrome (ACS) ST segment elevation'] > 0 or characteristics[
        'Acute coronary syndrome ST segment elevation'] is None:
        if characteristics['slope'] == "downsloping" or characteristics['slope'] == "upsloping":
            return "1 mm or more ST segment elevation"

    elif characteristics['shortness of breath'] > 0 or characteristics['shortness of breath'] is None:
        if characteristics['Exercise induced angina'] == 0:
            return 'left bundle branch block'

    if characteristics['Acute coronary syndrome ST segment elevation'] > 0.1:
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
            return "Treat reversible causes before proceeding."

        # Moderate or severe symptoms
        severe_symptoms = input("Does the patient have moderate or severe symptoms? (yes/no): ")
        if severe_symptoms.lower() == 'yes':
            if characteristics['have medication intoxication'].lower() == 'no':
                return "Administer Atropine and high-dose insulin"

            # Medication intoxication
            if characteristics['have medication intoxication'].lower() == 'yes':
                # Which medication?
                if characteristics['medication'].lower() == 'calcium channel blocker':
                    return "Administer IV Calcium"
                elif characteristics['medication'].lower() == 'beta-blocker':
                    return "Administer IV Glucagon"
                elif characteristics['medication'].lower() == 'digoxin':
                    return "Administer anti-digoxin antibody"

                if characteristics['post mediacal symtons'].lower() == 'yes':
                    return "Administer transcutaneous/transvenous pacemaker"
            else:
                if characteristics['hemodynamically unstable'].lower() == 'yes':
                    return "Administer transcutaneous/transvenous pacemaker"
                else:
                    if characteristics['AMI with AV block'].lower() == 'yes':
                        if characteristics['alrery have adminiter Aminophyline'].lower() == 'yes':
                            return "Administer transcutaneous/transvenous pacemaker"
                        else:
                            return "Administer Aminophylline"
                    else:
                        return "Administer beta-agonists"

    return "inconclusive"

# Acute coronary syndrome without ST segment elevation, acute myocardial infarction with ST segment elevation
