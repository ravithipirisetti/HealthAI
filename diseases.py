DISEASES = [

        {
        "name": "Common Cold",
        "category": "Respiratory",
        "symptoms": ["fever", "cough", "runny nose", "sore throat", "sneezing"],
        "description": "A common viral infection affecting the nose and throat.",
        "causes": ["Rhinovirus", "Coronavirus"],
        "prevention": ["Wash hands", "Stay hydrated", "Avoid close contact with sick people"],
        "risk": ["Children", "Older adults"],
        "redflags": ["Difficulty breathing", "Persistent high fever"]
    },
    {
        "name": "Influenza",
        "category": "Respiratory",
        "symptoms": ["fever", "cough", "fatigue", "body ache", "headache"],
        "description": "A contagious viral infection that attacks the respiratory system.",
        "causes": ["Influenza virus"],
        "prevention": ["Annual flu vaccine", "Wash hands"],
        "risk": ["Children", "Older adults", "Pregnant women"],
        "redflags": ["Chest pain", "Difficulty breathing"]
    },
    {
        "name": "Asthma",
        "category": "Respiratory",
        "symptoms": ["cough", "shortness of breath", "chest pain", "fatigue", "wheezing"],
        "description": "A condition in which the airways become inflamed and narrow.",
        "causes": ["Allergies", "Genetics", "Air pollution"],
        "prevention": ["Avoid triggers", "Take prescribed medication"],
        "risk": ["Children", "People with allergies"],
        "redflags": ["Severe breathing difficulty"]
    },
    {
        "name": "Migraine",
        "category": "Neurological",
        "symptoms": ["headache", "nausea", "vomiting", "dizziness"],
        "description": "A severe recurring headache often accompanied by nausea.",
        "causes": ["Stress", "Hormonal changes", "Certain foods"],
        "prevention": ["Manage stress", "Adequate sleep"],
        "risk": ["Adults", "Women"],
        "redflags": ["Vision loss", "Confusion"]
    },
    {
        "name": "Diabetes",
        "category": "Endocrine",
        "symptoms": ["fatigue", "thirst", "weight loss", "frequent urination"],
        "description": "A condition that affects how the body uses blood sugar.",
        "causes": ["Insulin deficiency", "Insulin resistance"],
        "prevention": ["Healthy diet", "Regular exercise"],
        "risk": ["Overweight individuals", "Family history"],
        "redflags": ["Confusion", "Loss of consciousness"]
    },
    {
        "name": "Food Poisoning",
        "category": "Digestive",
        "symptoms": ["vomiting", "nausea", "stomach pain", "diarrhea"],
        "description": "Illness caused by consuming contaminated food.",
        "causes": ["Bacteria", "Viruses", "Parasites"],
        "prevention": ["Cook food properly", "Maintain food hygiene"],
        "risk": ["Children", "Older adults"],
        "redflags": ["Severe dehydration", "Bloody diarrhea"]
    },
    {
        "name": "Pneumonia",
        "category": "Respiratory",
        "symptoms": ["fever", "cough", "chest pain", "fatigue", "shortness of breath"],
        "description": "An infection that inflames the air sacs in one or both lungs.",
        "causes": ["Bacteria", "Viruses", "Fungi"],
        "prevention": ["Vaccination", "Wash hands"],
        "risk": ["Older adults", "Children"],
        "redflags": ["Difficulty breathing", "Blue lips"]
    },
    {
        "name": "Dehydration",
        "category": "General",
        "symptoms": ["thirst", "fatigue", "dizziness", "dry mouth"],
        "description": "A condition caused by excessive loss of body fluids.",
        "causes": ["Vomiting", "Diarrhea", "Excessive sweating"],
        "prevention": ["Drink enough water"],
        "risk": ["Children", "Older adults"],
        "redflags": ["Fainting", "Confusion"]
    },
    {
        "name": "Ear Infection",
        "category": "ENT",
        "symptoms": ["ear pain", "fever", "hearing loss"],
        "description": "An infection of the middle or outer ear.",
        "causes": ["Bacteria", "Viruses"],
        "prevention": ["Treat colds promptly", "Maintain ear hygiene"],
        "risk": ["Children"],
        "redflags": ["Severe swelling", "Hearing loss"]
    },
        {
        "name": "COVID-19",
        "category": "Viral",
        "symptoms": ["fever", "cough", "fatigue", "loss of taste", "shortness of breath"],
        "description": "A viral respiratory illness caused by SARS-CoV-2.",
        "causes": ["Coronavirus"],
        "prevention": ["Vaccination", "Hand washing", "Wear masks"],
        "risk": ["Elderly", "People with chronic diseases"],
         "category": "Viral",
         "redflags": ["Difficulty breathing", "Chest pain"]
    },
    {
        "name": "Dengue Fever",
        "category": "Viral",
        "symptoms": ["fever", "headache", "body ache", "joint pain", "rash"],
        "description": "A mosquito-borne viral disease.",
        "causes": ["Dengue virus"],
        "prevention": ["Avoid mosquito bites", "Remove stagnant water"],
        "risk": ["Children", "People in tropical regions"],
        "redflags": ["Bleeding", "Severe abdominal pain"]
    },
    {
        "name": "Malaria",
        "category": "Parasitic",
        "symptoms": ["fever", "chills", "headache", "vomiting", "fatigue"],
        "description": "A mosquito-borne parasitic disease.",
        "causes": ["Plasmodium parasite"],
        "prevention": ["Mosquito nets", "Insect repellent"],
        "risk": ["Travelers", "Children"],
        "redflags": ["Confusion", "Seizures"]
    },
    {
        "name": "Typhoid Fever",
        "category": "Bacterial",
        "symptoms": ["fever", "headache", "stomach pain", "weakness", "constipation"],
        "description": "A bacterial infection spread through contaminated food and water.",
        "causes": ["Salmonella Typhi"],
        "prevention": ["Safe food", "Clean drinking water"],
        "risk": ["Children", "Travelers"],
        "redflags": ["Severe dehydration", "Internal bleeding"]
    },
    {
        "name": "Tuberculosis",
        "category": "Bacterial",
        "symptoms": ["cough", "weight loss", "fever", "night sweats", "fatigue"],
        "description": "A bacterial infection mainly affecting the lungs.",
        "causes": ["Mycobacterium tuberculosis"],
        "prevention": ["BCG vaccination", "Good ventilation"],
        "risk": ["People with weak immunity"],
        "redflags": ["Coughing blood", "Difficulty breathing"]
    },
    {
        "name": "Bronchitis",
        "category": "Respiratory",
        "symptoms": ["cough", "fatigue", "chest pain", "shortness of breath"],
        "description": "Inflammation of the bronchial tubes.",
        "causes": ["Virus", "Smoking"],
        "prevention": ["Avoid smoking", "Wash hands"],
        "risk": ["Smokers", "Older adults"],
        "redflags": ["Blue lips", "High fever"]
    },
    {
        "name": "Sinusitis",
        "category": "Respiratory",
        "symptoms": ["headache", "runny nose", "fever", "facial pain"],
        "description": "Inflammation of the sinuses.",
        "causes": ["Virus", "Bacteria", "Allergy"],
        "prevention": ["Treat allergies", "Avoid infections"],
        "risk": ["People with allergies"],
        "redflags": ["Vision changes", "Severe swelling"]
    },
    {
        "name": "Tonsillitis",
        "category": "Respiratory",
        "symptoms": ["sore throat", "fever", "headache", "difficulty swallowing"],
        "description": "Inflammation of the tonsils.",
        "causes": ["Virus", "Bacteria"],
        "prevention": ["Good hygiene"],
        "risk": ["Children"],
        "redflags": ["Difficulty breathing", "Severe swelling"]
    },
    {
        "name": "Chickenpox",
        "category": "Viral",
        "symptoms": ["fever", "rash", "fatigue", "itching"],
        "description": "A contagious viral infection causing itchy blisters.",
        "causes": ["Varicella-zoster virus"],
        "prevention": ["Vaccination"],
        "risk": ["Children"],
        "redflags": ["Breathing difficulty", "Confusion"]
    },
    {
        "name": "Measles",
      "symptoms": ["fever", "rash", "cough", "runny nose", "red eyes"],
        "description": "A highly contagious viral disease.",
        "causes": ["Measles virus"],
        "prevention": ["MMR vaccination"],
        "risk": ["Unvaccinated children"],
        "redflags": ["Seizures", "Difficulty breathing"]
    },
        {
        "name": "Mumps",
        "category": "Viral",
        "symptoms": ["fever", "headache", "swollen glands", "fatigue"],
        "description": "A viral infection affecting the salivary glands.",
        "causes": ["Mumps virus"],
        "prevention": ["MMR vaccination"],
        "risk": ["Children"],
        "redflags": ["Difficulty swallowing", "Severe headache"]
    },
    {
        "name": "Hepatitis A",
        "category": "Liver",
        "symptoms": ["fatigue", "nausea", "vomiting", "jaundice", "stomach pain"],
        "description": "A viral liver infection.",
        "causes": ["Hepatitis A virus"],
        "prevention": ["Vaccination", "Safe food and water"],
        "risk": ["Travelers"],
        "redflags": ["Confusion", "Persistent vomiting"]
    },
    {
        "name": "Hepatitis B",
        "category": "Liver",
        "symptoms": ["fatigue", "jaundice", "stomach pain", "nausea"],
        "description": "A viral infection affecting the liver.",
        "causes": ["Hepatitis B virus"],
        "prevention": ["Vaccination", "Safe blood practices"],
        "risk": ["Healthcare workers"],
        "redflags": ["Severe abdominal pain", "Bleeding"]
    },
    {
        "name": "Gastroenteritis",
        "category": "Digestive",
        "symptoms": ["vomiting", "diarrhea", "stomach pain", "fever"],
        "description": "Inflammation of the stomach and intestines.",
        "causes": ["Virus", "Bacteria"],
        "prevention": ["Hand washing", "Safe food"],
        "risk": ["Children", "Elderly"],
        "redflags": ["Severe dehydration", "Blood in stool"]
    },
    {
        "name": "Appendicitis",
        "category": "Digestive",
        "symptoms": ["stomach pain", "fever", "nausea", "vomiting"],
        "description": "Inflammation of the appendix.",
        "causes": ["Blocked appendix"],
        "prevention": ["No specific prevention"],
        "risk": ["Young adults"],
        "redflags": ["Severe abdominal pain", "High fever"]
    },
    {
        "name": "Gastritis",
        "category": "Digestive",
        "symptoms": ["stomach pain", "nausea", "vomiting", "bloating"],
        "description": "Inflammation of the stomach lining.",
        "causes": ["H. pylori", "Painkillers"],
        "prevention": ["Healthy diet", "Avoid alcohol"],
        "risk": ["Adults"],
        "redflags": ["Vomiting blood", "Black stools"]
    },
    {
        "name": "Peptic Ulcer",
        "category": "Digestive",
        "symptoms": ["stomach pain", "bloating", "nausea", "heartburn"],
        "description": "Sores in the stomach or upper intestine.",
        "causes": ["H. pylori", "NSAIDs"],
        "prevention": ["Avoid smoking", "Healthy diet"],
        "risk": ["Adults"],
        "redflags": ["Vomiting blood", "Black stools"]
    },
    {
        "name": "Acid Reflux",
        "category": "Digestive",
        "symptoms": ["heartburn", "chest pain", "sore throat", "cough"],
        "description": "Stomach acid flows back into the esophagus.",
        "causes": ["Weak lower esophageal sphincter"],
        "prevention": ["Avoid spicy food", "Eat smaller meals"],
        "risk": ["Obesity"],
        "redflags": ["Difficulty swallowing", "Chest pain"]
    },
    {
        "name": "Constipation",
        "category": "Digestive",
        "symptoms": ["stomach pain", "bloating", "constipation"],
        "description": "Difficulty passing stools.",
        "causes": ["Low fiber diet", "Dehydration"],
        "prevention": ["High-fiber diet", "Drink water"],
        "risk": ["Older adults"],
        "redflags": ["Blood in stool", "Severe abdominal pain"]
    },
    {
        "name": "Diarrhea",
        "category": "Digestive",
        "symptoms": ["diarrhea", "stomach pain", "vomiting", "fever"],
        "description": "Frequent loose or watery stools.",
        "causes": ["Virus", "Bacteria", "Food poisoning"],
        "prevention": ["Safe food", "Drink clean water"],
        "risk": ["Children"],
        "redflags": ["Severe dehydration", "Blood in stool"]
    },
        {
        "name": "Hypertension",
        "category": "Cardiovascular",
        "symptoms": ["headache", "dizziness", "chest pain", "blurred vision"],
        "description": "A condition where blood pressure remains consistently high.",
        "causes": ["Genetics", "High salt intake", "Obesity"],
        "prevention": ["Exercise", "Healthy diet", "Reduce salt"],
        "risk": ["Older adults", "Obesity"],
        "redflags": ["Chest pain", "Stroke symptoms"]
    },
    {
        "name": "Hypotension",
        "category": "Cardiovascular",
        "symptoms": ["dizziness", "fatigue", "blurred vision", "fainting"],
        "description": "A condition where blood pressure is lower than normal.",
        "causes": ["Dehydration", "Blood loss"],
        "prevention": ["Drink fluids", "Healthy diet"],
        "risk": ["Older adults"],
        "redflags": ["Loss of consciousness"]
    },
    {
        "name": "Heart Attack",
        "category": "Cardiovascular",
        "symptoms": ["chest pain", "shortness of breath", "fatigue", "nausea"],
        "description": "Occurs when blood flow to the heart is blocked.",
        "causes": ["Blocked coronary artery"],
        "prevention": ["Exercise", "Healthy diet", "Avoid smoking"],
        "risk": ["High blood pressure", "Diabetes"],
        "redflags": ["Severe chest pain", "Difficulty breathing"]
    },
    {
        "name": "Stroke",
        "category": "Neurological",
        "symptoms": ["headache", "dizziness", "confusion", "weakness"],
        "description": "Occurs when blood supply to the brain is interrupted.",
        "causes": ["Blood clot", "Bleeding in the brain"],
        "prevention": ["Control blood pressure", "Exercise"],
        "risk": ["Hypertension", "Diabetes"],
        "redflags": ["Sudden paralysis", "Difficulty speaking"]
    },
    {
        "name": "Anemia",
        "category": "Blood",
        "symptoms": ["fatigue", "dizziness", "shortness of breath", "pale skin"],
        "description": "A condition with a low number of healthy red blood cells.",
        "causes": ["Iron deficiency", "Blood loss"],
        "prevention": ["Iron-rich diet"],
        "risk": ["Women", "Children"],
        "redflags": ["Chest pain", "Fainting"]
    },
    {
        "name": "Kidney Stones",
        "category": "Kidney",
        "symptoms": ["stomach pain", "back pain", "vomiting", "blood in urine"],
        "description": "Hard mineral deposits that form inside the kidneys.",
        "causes": ["Dehydration", "High mineral levels"],
        "prevention": ["Drink plenty of water"],
        "risk": ["Adults"],
        "redflags": ["Severe pain", "High fever"]
    },
    {
        "name": "Urinary Tract Infection",
        "category": "Urinary",
        "symptoms": ["burning urination", "fever", "stomach pain", "frequent urination"],
        "description": "A bacterial infection affecting the urinary tract.",
        "causes": ["Bacteria"],
        "prevention": ["Drink water", "Maintain hygiene"],
        "risk": ["Women"],
        "redflags": ["High fever", "Back pain"]
    },
    {
        "name": "Chronic Kidney Disease",
        "category": "Kidney",
        "symptoms": ["fatigue", "swelling", "shortness of breath", "nausea"],
        "description": "Gradual loss of kidney function over time.",
        "causes": ["Diabetes", "High blood pressure"],
        "prevention": ["Control blood sugar", "Healthy lifestyle"],
        "risk": ["Diabetics"],
        "redflags": ["Difficulty breathing", "Chest pain"]
    },
    {
        "name": "Liver Cirrhosis",
        "category": "Liver",
        "symptoms": ["fatigue", "jaundice", "swelling", "weight loss"],
        "description": "Scarring of the liver caused by long-term damage.",
        "causes": ["Alcohol", "Hepatitis"],
        "prevention": ["Avoid alcohol", "Vaccination"],
        "risk": ["People with liver disease"],
        "redflags": ["Vomiting blood", "Confusion"]
    },
    {
        "name": "Gallstones",
        "category": "Digestive",
        "symptoms": ["stomach pain", "nausea", "vomiting", "fever"],
        "description": "Hardened deposits that form in the gallbladder.",
        "causes": ["High cholesterol"],
        "prevention": ["Healthy diet", "Maintain weight"],
        "risk": ["Adults"],
        "redflags": ["Severe abdominal pain", "Jaundice"]
    },
        {
        "name": "Hyperthyroidism",
        "category": "Endocrine",
        "symptoms": ["weight loss", "fatigue", "rapid heartbeat", "sweating"],
        "description": "A condition where the thyroid gland produces too much hormone.",
        "causes": ["Graves' disease", "Thyroid nodules"],
        "prevention": ["Regular checkups"],
        "risk": ["Women"],
        "redflags": ["Chest pain", "Irregular heartbeat"]
    },
    {
        "name": "Hypothyroidism",
        "category": "Endocrine",
        "symptoms": ["fatigue", "weight gain", "dry skin", "constipation"],
        "description": "A condition where the thyroid gland does not produce enough hormone.",
        "causes": ["Hashimoto's disease"],
        "prevention": ["Regular thyroid checkups"],
        "risk": ["Women", "Older adults"],
        "redflags": ["Difficulty breathing", "Severe weakness"]
    },
    {
        "name": "Goiter",
        "category": "Endocrine",
        "symptoms": ["swollen neck", "difficulty swallowing", "cough"],
        "description": "Abnormal enlargement of the thyroid gland.",
        "causes": ["Iodine deficiency"],
        "prevention": ["Adequate iodine intake"],
        "risk": ["Women"],
        "redflags": ["Difficulty breathing"]
    },
    {
        "name": "Obesity",
        "category": "Metabolic",
        "symptoms": ["weight gain", "fatigue", "shortness of breath"],
        "description": "Excess body fat that increases health risks.",
        "causes": ["Poor diet", "Lack of exercise"],
        "prevention": ["Healthy diet", "Exercise"],
        "risk": ["Adults"],
        "redflags": ["Chest pain"]
    },
    {
        "name": "High Cholesterol",
        "category": "Cardiovascular",
        "symptoms": ["fatigue", "chest pain"],
        "description": "High levels of cholesterol in the blood.",
        "causes": ["Poor diet", "Genetics"],
        "prevention": ["Exercise", "Healthy diet"],
        "risk": ["Adults"],
        "redflags": ["Heart attack", "Stroke symptoms"]
    },
    {
        "name": "Astigmatism",
        "category": "Eye",
        "symptoms": ["blurred vision", "headache", "eye strain"],
        "description": "An eye condition causing blurred vision.",
        "causes": ["Irregular cornea"],
        "prevention": ["Regular eye exams"],
        "risk": ["All ages"],
        "redflags": ["Sudden vision loss"]
    },
    {
        "name": "Conjunctivitis",
        "category": "Eye",
        "symptoms": ["red eyes", "itching", "eye discharge"],
        "description": "Inflammation of the conjunctiva.",
        "causes": ["Virus", "Bacteria", "Allergy"],
        "prevention": ["Hand hygiene"],
        "risk": ["Children"],
        "redflags": ["Severe eye pain", "Vision loss"]
    },
    {
        "name": "Glaucoma",
        "category": "Eye",
        "symptoms": ["blurred vision", "eye pain", "headache"],
        "description": "Damage to the optic nerve due to increased eye pressure.",
        "causes": ["High eye pressure"],
        "prevention": ["Regular eye checkups"],
        "risk": ["Older adults"],
        "redflags": ["Sudden vision loss"]
    },
    {
        "name": "Cataract",
        "category": "Eye",
        "symptoms": ["blurred vision", "poor night vision", "sensitivity to light"],
        "description": "Clouding of the eye's natural lens.",
        "causes": ["Aging"],
        "prevention": ["Protect eyes from UV light"],
        "risk": ["Older adults"],
        "redflags": ["Sudden vision changes"]
    },
    {
        "name": "Otitis Media",
        "category": "ENT",
        "symptoms": ["ear pain", "fever", "hearing loss"],
        "description": "Middle ear infection.",
        "causes": ["Bacteria", "Virus"],
        "prevention": ["Treat colds early"],
        "risk": ["Children"],
        "redflags": ["Severe swelling", "Persistent hearing loss"]
    },
        {
        "name": "Osteoarthritis",
        "category": "Bone",
        "symptoms": ["joint pain", "joint stiffness", "swelling"],
        "description": "A degenerative joint disease affecting cartilage.",
        "causes": ["Aging", "Joint wear"],
        "prevention": ["Exercise", "Maintain healthy weight"],
        "risk": ["Older adults"],
        "redflags": ["Severe joint swelling"]
    },
    {
        "name": "Rheumatoid Arthritis",
        "category": "Bone",
        "symptoms": ["joint pain", "joint swelling", "fatigue", "fever"],
        "description": "An autoimmune disease affecting joints.",
        "causes": ["Autoimmune disorder"],
        "prevention": ["Regular exercise"],
        "risk": ["Women"],
        "redflags": ["Loss of joint movement"]
    },
    {
        "name": "Osteoporosis",
        "category": "Bone",
        "symptoms": ["back pain", "bone fractures", "loss of height"],
        "description": "A condition causing weak and brittle bones.",
        "causes": ["Calcium deficiency", "Aging"],
        "prevention": ["Calcium", "Vitamin D", "Exercise"],
        "risk": ["Older adults", "Women"],
        "redflags": ["Hip fracture"]
    },
    {
        "name": "Gout",
        "category": "Bone",
        "symptoms": ["joint pain", "swelling", "redness"],
        "description": "A type of arthritis caused by uric acid crystals.",
        "causes": ["High uric acid"],
        "prevention": ["Healthy diet", "Drink water"],
        "risk": ["Adults"],
        "redflags": ["Severe joint pain"]
    },
    {
        "name": "Scoliosis",
        "category": "Bone",
        "symptoms": ["back pain", "uneven shoulders", "poor posture"],
        "description": "An abnormal sideways curvature of the spine.",
        "causes": ["Unknown", "Congenital"],
        "prevention": ["Regular screening"],
        "risk": ["Teenagers"],
        "redflags": ["Difficulty breathing"]
    },
    {
        "name": "Eczema",
        "category": "Skin",
        "symptoms": ["itching", "rash", "dry skin"],
        "description": "A skin condition causing itchy and inflamed patches.",
        "causes": ["Allergy", "Genetics"],
        "prevention": ["Moisturize skin", "Avoid triggers"],
        "risk": ["Children"],
        "redflags": ["Skin infection"]
    },
    {
        "name": "Psoriasis",
        "category": "Skin",
        "symptoms": ["rash", "itching", "dry skin"],
        "description": "A chronic autoimmune skin condition.",
        "causes": ["Autoimmune disorder"],
        "prevention": ["Avoid skin injury"],
        "risk": ["Adults"],
        "redflags": ["Joint pain"]
    },
    {
        "name": "Acne",
        "category": "Skin",
        "symptoms": ["pimples", "oily skin", "skin redness"],
        "description": "A common skin condition affecting hair follicles.",
        "causes": ["Hormonal changes"],
        "prevention": ["Clean skin regularly"],
        "risk": ["Teenagers"],
        "redflags": ["Severe skin infection"]
    },
    {
        "name": "Cellulitis",
        "category": "Skin",
        "symptoms": ["fever", "skin redness", "swelling", "pain"],
        "description": "A bacterial skin infection.",
        "causes": ["Bacteria"],
        "prevention": ["Keep wounds clean"],
        "risk": ["Diabetics"],
        "redflags": ["Rapid spreading redness"]
    },
    {
        "name": "Ringworm",
        "category": "Skin",
        "symptoms": ["itching", "rash", "circular skin patches"],
        "description": "A fungal skin infection.",
        "causes": ["Fungus"],
        "prevention": ["Keep skin dry", "Maintain hygiene"],
        "risk": ["Children"],
        "redflags": ["Severe spreading infection"]
    },
        {
        "name": "Allergic Rhinitis",
        "category": "Allergy",
        "symptoms": ["runny nose", "sneezing", "itching", "red eyes"],
        "description": "An allergic reaction affecting the nose.",
        "causes": ["Pollen", "Dust", "Pet dander"],
        "prevention": ["Avoid allergens", "Wear a mask"],
        "risk": ["People with allergies"],
        "redflags": ["Difficulty breathing"]
    },
    {
        "name": "Food Allergy",
        "category": "Allergy",
        "symptoms": ["rash", "itching", "vomiting", "swelling"],
        "description": "An immune system reaction to certain foods.",
        "causes": ["Peanuts", "Milk", "Eggs", "Shellfish"],
        "prevention": ["Avoid trigger foods"],
        "risk": ["Children"],
        "redflags": ["Difficulty breathing", "Severe swelling"]
    },
    {
        "name": "Epilepsy",
        "category": "Neurological",
        "symptoms": ["seizures", "confusion", "loss of consciousness"],
        "description": "A neurological disorder causing repeated seizures.",
        "causes": ["Brain injury", "Genetics"],
        "prevention": ["Take prescribed medication"],
        "risk": ["Children", "Older adults"],
        "redflags": ["Seizure lasting over 5 minutes"]
    },
    {
        "name": "Parkinson's Disease",
        "category": "Neurological",
        "symptoms": ["tremors", "muscle stiffness", "slow movement"],
        "description": "A progressive disorder affecting movement.",
        "causes": ["Loss of dopamine-producing brain cells"],
        "prevention": ["No known prevention"],
        "risk": ["Older adults"],
        "redflags": ["Difficulty swallowing", "Frequent falls"]
    },
    {
        "name": "Alzheimer's Disease",
        "category": "Neurological",
        "symptoms": ["memory loss", "confusion", "difficulty speaking"],
        "description": "A progressive brain disorder affecting memory.",
        "causes": ["Brain cell damage"],
        "prevention": ["Healthy lifestyle", "Mental exercise"],
        "risk": ["Older adults"],
        "redflags": ["Sudden behavior changes"]
    },
    {
        "name": "Depression",
        "category": "Mental Health",
        "symptoms": ["fatigue", "sadness", "loss of interest", "sleep problems"],
        "description": "A mental health condition affecting mood and daily life.",
        "causes": ["Stress", "Genetics", "Brain chemistry"],
        "prevention": ["Stress management", "Social support"],
        "risk": ["Anyone"],
        "redflags": ["Thoughts of self-harm"]
    },
    {
        "name": "Anxiety Disorder",
        "category": "Mental Health",
        "symptoms": ["rapid heartbeat", "sweating", "fear", "restlessness"],
        "description": "A condition involving excessive fear and worry.",
        "causes": ["Stress", "Genetics"],
        "prevention": ["Stress management", "Exercise"],
        "risk": ["Anyone"],
        "redflags": ["Panic attacks", "Difficulty breathing"]
    },
    {
        "name": "Panic Disorder",
        "category": "Mental Health",
        "symptoms": ["chest pain", "rapid heartbeat", "fear", "dizziness"],
        "description": "A condition causing sudden episodes of intense fear.",
        "causes": ["Stress", "Genetics"],
        "prevention": ["Counseling", "Stress reduction"],
        "risk": ["Young adults"],
        "redflags": ["Loss of consciousness"]
    },
    {
        "name": "Insomnia",
        "category": "Sleep Disorder",
        "symptoms": ["difficulty sleeping", "fatigue", "poor concentration"],
        "description": "A disorder that makes it difficult to fall or stay asleep.",
        "causes": ["Stress", "Poor sleep habits"],
        "prevention": ["Maintain a regular sleep schedule"],
        "risk": ["Adults"],
        "redflags": ["Severe daytime drowsiness"]
    },
    {
        "name": "Sleep Apnea",
        "category": "Sleep Disorder",
        "symptoms": ["snoring", "fatigue", "morning headache"],
        "description": "A disorder in which breathing repeatedly stops during sleep.",
        "causes": ["Blocked airway", "Obesity"],
        "prevention": ["Maintain healthy weight"],
        "risk": ["Adults"],
        "redflags": ["Difficulty breathing during sleep"]
    }, 
        {
        "name": "Fibromyalgia",
        "category": "Musculoskeletal",
        "symptoms": ["fatigue", "muscle pain", "joint pain", "sleep problems"],
        "description": "A chronic condition causing widespread pain and tenderness.",
        "causes": ["Unknown", "Genetics", "Stress"],
        "prevention": ["Regular exercise", "Stress management"],
        "risk": ["Women"],
        "redflags": ["Severe weakness"]
    },
    {
        "name": "Lupus",
        "category": "Autoimmune",
        "symptoms": ["fatigue", "joint pain", "rash", "fever"],
        "description": "An autoimmune disease that can affect many organs.",
        "causes": ["Immune system disorder"],
        "prevention": ["No known prevention"],
        "risk": ["Women"],
        "redflags": ["Chest pain", "Kidney problems"]
    },
    {
        "name": "Multiple Sclerosis",
        "category": "Neurological",
        "symptoms": ["muscle weakness", "blurred vision", "dizziness", "fatigue"],
        "description": "An autoimmune disease affecting the brain and spinal cord.",
        "causes": ["Immune system disorder"],
        "prevention": ["No known prevention"],
        "risk": ["Young adults"],
        "redflags": ["Loss of vision", "Difficulty walking"]
    },
    {
        "name": "Lyme Disease",
        "category": "Infectious",
        "symptoms": ["fever", "rash", "joint pain", "fatigue"],
        "description": "A bacterial infection spread through tick bites.",
        "causes": ["Borrelia bacteria"],
        "prevention": ["Avoid tick bites", "Use insect repellent"],
        "risk": ["Outdoor workers"],
        "redflags": ["Facial paralysis", "Chest pain"]
    },
    {
        "name": "Leptospirosis",
        "category": "Bacterial",
        "symptoms": ["fever", "headache", "muscle pain", "vomiting"],
        "description": "A bacterial infection spread by contaminated water.",
        "causes": ["Leptospira bacteria"],
        "prevention": ["Avoid contaminated water"],
        "risk": ["Farmers", "Outdoor workers"],
        "redflags": ["Jaundice", "Kidney failure"]
    },
    {
        "name": "Cholera",
        "category": "Bacterial",
        "symptoms": ["diarrhea", "vomiting", "dehydration"],
        "description": "A bacterial disease causing severe diarrhea.",
        "causes": ["Vibrio cholerae"],
        "prevention": ["Safe drinking water", "Hand washing"],
        "risk": ["Areas with poor sanitation"],
        "redflags": ["Severe dehydration", "Shock"]
    },
    {
        "name": "Rabies",
        "category": "Viral",
        "symptoms": ["fever", "headache", "confusion", "difficulty swallowing"],
        "description": "A deadly viral disease spread by animal bites.",
        "causes": ["Rabies virus"],
        "prevention": ["Vaccination after animal bite"],
        "risk": ["Animal handlers"],
        "redflags": ["Hydrophobia", "Paralysis"]
    },
    {
        "name": "Tetanus",
        "category": "Bacterial",
        "symptoms": ["muscle stiffness", "jaw stiffness", "fever"],
        "description": "A serious bacterial infection affecting muscles and nerves.",
        "causes": ["Clostridium tetani"],
        "prevention": ["Tetanus vaccination"],
        "risk": ["People with open wounds"],
        "redflags": ["Difficulty breathing", "Severe muscle spasms"]
    },
    {
        "name": "Whooping Cough",
        "category": "Respiratory",
        "symptoms": ["cough", "fever", "runny nose", "difficulty breathing"],
        "description": "A highly contagious bacterial respiratory infection.",
        "causes": ["Bordetella pertussis"],
        "prevention": ["Vaccination"],
        "risk": ["Children"],
        "redflags": ["Blue lips", "Breathing difficulty"]
    },
    {
        "name": "Polio",
        "category": "Viral",
        "symptoms": ["fever", "fatigue", "muscle weakness", "headache"],
        "description": "A viral disease that can affect the nervous system.",
        "causes": ["Poliovirus"],
        "prevention": ["Polio vaccination"],
        "risk": ["Unvaccinated children"],
        "redflags": ["Paralysis", "Difficulty breathing"]
    }, 
        {
        "name": "Chickenpox (Severe)",
        "category": "Viral",
        "symptoms": ["fever", "rash", "itching", "fatigue", "blisters"],
        "description": "A severe form of chickenpox causing widespread skin lesions.",
        "causes": ["Varicella-zoster virus"],
        "prevention": ["Vaccination"],
        "risk": ["Children", "People with weak immunity"],
        "redflags": ["Difficulty breathing", "Confusion"]
    },
    {
        "name": "Meningitis",
        "category": "Neurological",
        "symptoms": ["fever", "headache", "neck stiffness", "vomiting"],
        "description": "Inflammation of the protective membranes covering the brain and spinal cord.",
        "causes": ["Virus", "Bacteria"],
        "prevention": ["Vaccination", "Good hygiene"],
        "risk": ["Children", "College students"],
        "redflags": ["Seizures", "Loss of consciousness"]
    },
    {
        "name": "Encephalitis",
        "category": "Neurological",
        "symptoms": ["fever", "headache", "confusion", "seizures"],
        "description": "Inflammation of the brain, usually caused by infection.",
        "causes": ["Virus"],
        "prevention": ["Vaccination", "Mosquito protection"],
        "risk": ["Children", "Older adults"],
        "redflags": ["Coma", "Seizures"]
    },
    {
        "name": "Sepsis",
        "category": "Infectious",
        "symptoms": ["fever", "rapid heartbeat", "confusion", "difficulty breathing"],
        "description": "A life-threatening response to infection.",
        "causes": ["Severe infection"],
        "prevention": ["Treat infections promptly"],
        "risk": ["Older adults", "Hospital patients"],
        "redflags": ["Low blood pressure", "Organ failure"]
    },
    {
        "name": "Heat Stroke",
        "category": "Environmental",
        "symptoms": ["high fever", "dizziness", "confusion", "rapid heartbeat"],
        "description": "A dangerous condition caused by prolonged exposure to high temperatures.",
        "causes": ["Extreme heat"],
        "prevention": ["Stay hydrated", "Avoid excessive heat"],
        "risk": ["Athletes", "Older adults"],
        "redflags": ["Loss of consciousness", "Seizures"]
    },
    {
        "name": "Heat Exhaustion",
        "category": "Environmental",
        "symptoms": ["fatigue", "dizziness", "headache", "heavy sweating"],
        "description": "A heat-related illness caused by excessive loss of water and salt.",
        "causes": ["Hot weather", "Dehydration"],
        "prevention": ["Drink water", "Rest in shade"],
        "risk": ["Outdoor workers"],
        "redflags": ["Confusion", "Fainting"]
    },
    {
        "name": "Hypothermia",
        "category": "Environmental",
        "symptoms": ["shivering", "confusion", "fatigue", "slow heartbeat"],
        "description": "A condition caused by dangerously low body temperature.",
        "causes": ["Cold exposure"],
        "prevention": ["Wear warm clothing"],
        "risk": ["Older adults", "Outdoor workers"],
        "redflags": ["Loss of consciousness", "Difficulty breathing"]
    },
    {
        "name": "Frostbite",
        "category": "Environmental",
        "symptoms": ["numbness", "skin discoloration", "pain"],
        "description": "Damage to skin and tissue caused by freezing temperatures.",
        "causes": ["Extreme cold"],
        "prevention": ["Protect exposed skin"],
        "risk": ["Outdoor workers"],
        "redflags": ["Blackened skin", "Loss of sensation"]
    },
    {
        "name": "Motion Sickness",
        "category": "Neurological",
        "symptoms": ["nausea", "vomiting", "dizziness", "sweating"],
        "description": "A condition caused by conflicting signals to the brain during movement.",
        "causes": ["Travel by car, boat, or plane"],
        "prevention": ["Look ahead", "Avoid reading while traveling"],
        "risk": ["Children"],
        "redflags": ["Persistent vomiting"]
    },
    {
        "name": "Altitude Sickness",
        "category": "Environmental",
        "symptoms": ["headache", "dizziness", "fatigue", "shortness of breath"],
        "description": "A condition caused by reduced oxygen at high altitude.",
        "causes": ["Rapid ascent to high altitude"],
        "prevention": ["Ascend slowly", "Stay hydrated"],
        "risk": ["Mountain climbers"],
        "redflags": ["Confusion", "Difficulty breathing"]
    }, 
        {
        "name": "Shingles",
        "category": "Viral",
        "symptoms": ["rash", "pain", "itching", "fever"],
        "description": "A viral infection causing a painful rash.",
        "causes": ["Varicella-zoster virus"],
        "prevention": ["Shingles vaccine"],
        "risk": ["Older adults"],
        "redflags": ["Vision problems", "Severe pain"]
    },
    {
        "name": "Chikungunya",
        "category": "Viral",
        "symptoms": ["fever", "joint pain", "headache", "rash"],
        "description": "A mosquito-borne viral disease.",
        "causes": ["Chikungunya virus"],
        "prevention": ["Avoid mosquito bites"],
        "risk": ["People in tropical regions"],
        "redflags": ["Persistent joint pain"]
    },
    {
        "name": "Zika Virus Infection",
        "category": "Viral",
        "symptoms": ["fever", "rash", "joint pain", "red eyes"],
        "description": "A mosquito-borne viral infection.",
        "causes": ["Zika virus"],
        "prevention": ["Mosquito control"],
        "risk": ["Pregnant women"],
        "redflags": ["Neurological complications"]
    },
    {
        "name": "Yellow Fever",
        "category": "Viral",
        "symptoms": ["fever", "headache", "muscle pain", "jaundice"],
        "description": "A mosquito-borne viral disease.",
        "causes": ["Yellow fever virus"],
        "prevention": ["Vaccination"],
        "risk": ["Travelers"],
        "redflags": ["Bleeding", "Liver failure"]
    },
    {
        "name": "Typhus",
        "category": "Bacterial",
        "symptoms": ["fever", "headache", "rash", "fatigue"],
        "description": "A bacterial infection spread by lice or fleas.",
        "causes": ["Rickettsia bacteria"],
        "prevention": ["Maintain hygiene"],
        "risk": ["Crowded living conditions"],
        "redflags": ["Confusion", "Low blood pressure"]
    },
    {
        "name": "Brucellosis",
        "category": "Bacterial",
        "symptoms": ["fever", "joint pain", "fatigue", "night sweats"],
        "description": "A bacterial infection spread from animals.",
        "causes": ["Brucella bacteria"],
        "prevention": ["Avoid unpasteurized milk"],
        "risk": ["Farm workers"],
        "redflags": ["Persistent fever"]
    },
    {
        "name": "Anthrax",
        "category": "Bacterial",
        "symptoms": ["fever", "skin sores", "fatigue", "cough"],
        "description": "A serious bacterial infection.",
        "causes": ["Bacillus anthracis"],
        "prevention": ["Protective equipment"],
        "risk": ["Animal handlers"],
        "redflags": ["Difficulty breathing", "Shock"]
    },
    {
        "name": "Plague",
        "category": "Bacterial",
        "symptoms": ["fever", "swollen glands", "fatigue", "headache"],
        "description": "A bacterial disease spread by fleas.",
        "causes": ["Yersinia pestis"],
        "prevention": ["Control fleas"],
        "risk": ["Rural areas"],
        "redflags": ["Difficulty breathing", "Sepsis"]
    },
    {
        "name": "Tonsillitis",
        "category": "ENT",
        "symptoms": ["sore throat", "fever", "difficulty swallowing", "headache"],
        "description": "Inflammation of the tonsils.",
        "causes": ["Virus", "Bacteria"],
        "prevention": ["Hand hygiene"],
        "risk": ["Children"],
        "redflags": ["Difficulty breathing"]
    },
    {
        "name": "Sinusitis",
        "category": "ENT",
        "symptoms": ["headache", "runny nose", "facial pain", "fever"],
        "description": "Inflammation of the sinuses.",
        "causes": ["Virus", "Bacteria", "Allergy"],
        "prevention": ["Treat allergies", "Hand washing"],
        "risk": ["People with allergies"],
        "redflags": ["Vision changes", "High fever"]
    }, 
        {
        "name": "Bronchitis",
        "category": "Respiratory",
        "symptoms": ["cough", "fatigue", "fever", "shortness of breath"],
        "description": "Inflammation of the bronchial tubes.",
        "causes": ["Virus", "Smoking"],
        "prevention": ["Avoid smoking", "Wash hands"],
        "risk": ["Smokers"],
        "redflags": ["Difficulty breathing", "Blue lips"]
    },
    {
        "name": "Emphysema",
        "category": "Respiratory",
        "symptoms": ["shortness of breath", "cough", "fatigue"],
        "description": "A lung disease causing damaged air sacs.",
        "causes": ["Smoking"],
        "prevention": ["Avoid smoking"],
        "risk": ["Smokers"],
        "redflags": ["Severe breathing difficulty"]
    },
    {
        "name": "COPD",
        "category": "Respiratory",
        "symptoms": ["cough", "shortness of breath", "fatigue", "wheezing"],
        "description": "Chronic Obstructive Pulmonary Disease affecting airflow.",
        "causes": ["Smoking", "Air pollution"],
        "prevention": ["Avoid smoking"],
        "risk": ["Older adults"],
        "redflags": ["Blue lips", "Chest pain"]
    },
    {
        "name": "Pulmonary Tuberculosis",
        "category": "Respiratory",
        "symptoms": ["cough", "fever", "weight loss", "night sweats"],
        "description": "A bacterial infection affecting the lungs.",
        "causes": ["Mycobacterium tuberculosis"],
        "prevention": ["BCG vaccination", "Cover cough"],
        "risk": ["People with weak immunity"],
        "redflags": ["Coughing blood", "Difficulty breathing"]
    },
    {
        "name": "Pleural Effusion",
        "category": "Respiratory",
        "symptoms": ["chest pain", "shortness of breath", "cough"],
        "description": "Fluid buildup around the lungs.",
        "causes": ["Heart failure", "Infection"],
        "prevention": ["Treat underlying disease"],
        "risk": ["Older adults"],
        "redflags": ["Severe breathing difficulty"]
    },
    {
        "name": "Pericarditis",
        "category": "Cardiovascular",
        "symptoms": ["chest pain", "fever", "fatigue"],
        "description": "Inflammation of the sac surrounding the heart.",
        "causes": ["Virus", "Autoimmune disease"],
        "prevention": ["Treat infections promptly"],
        "risk": ["Adults"],
        "redflags": ["Difficulty breathing"]
    },
    {
        "name": "Myocarditis",
        "category": "Cardiovascular",
        "symptoms": ["chest pain", "fatigue", "shortness of breath"],
        "description": "Inflammation of the heart muscle.",
        "causes": ["Virus"],
        "prevention": ["Prevent viral infections"],
        "risk": ["Young adults"],
        "redflags": ["Irregular heartbeat", "Fainting"]
    },
    {
        "name": "Endocarditis",
        "category": "Cardiovascular",
        "symptoms": ["fever", "fatigue", "heart murmur"],
        "description": "Infection of the inner lining of the heart.",
        "causes": ["Bacteria"],
        "prevention": ["Good dental hygiene"],
        "risk": ["Heart valve disease"],
        "redflags": ["Stroke symptoms"]
    },
    {
        "name": "Deep Vein Thrombosis",
        "category": "Cardiovascular",
        "symptoms": ["leg swelling", "leg pain", "skin redness"],
        "description": "A blood clot in a deep vein.",
        "causes": ["Prolonged sitting", "Surgery"],
        "prevention": ["Regular movement"],
        "risk": ["Travelers", "Post-surgery patients"],
        "redflags": ["Chest pain", "Difficulty breathing"]
    },
    {
        "name": "Pulmonary Embolism",
        "category": "Cardiovascular",
        "symptoms": ["chest pain", "shortness of breath", "rapid heartbeat"],
        "description": "A blood clot blocking an artery in the lungs.",
        "causes": ["Blood clot"],
        "prevention": ["Prevent DVT"],
        "risk": ["Hospital patients"],
        "redflags": ["Collapse", "Severe breathing difficulty"]
    }, 
        {
        "name": "Cushing Syndrome",
        "category": "Endocrine",
        "symptoms": ["weight gain", "fatigue", "high blood pressure"],
        "description": "A disorder caused by high cortisol levels.",
        "causes": ["Long-term steroid use", "Pituitary tumor"],
        "prevention": ["Use steroids only as prescribed"],
        "risk": ["Adults"],
        "redflags": ["Severe weakness"]
    },
    {
        "name": "Addison's Disease",
        "category": "Endocrine",
        "symptoms": ["fatigue", "weight loss", "low blood pressure"],
        "description": "A disorder where the adrenal glands produce too little hormone.",
        "causes": ["Autoimmune disease"],
        "prevention": ["No known prevention"],
        "risk": ["Adults"],
        "redflags": ["Severe dehydration", "Shock"]
    },
    {
        "name": "Pancreatitis",
        "category": "Digestive",
        "symptoms": ["stomach pain", "vomiting", "fever", "nausea"],
        "description": "Inflammation of the pancreas.",
        "causes": ["Gallstones", "Alcohol"],
        "prevention": ["Avoid alcohol", "Healthy diet"],
        "risk": ["Adults"],
        "redflags": ["Severe abdominal pain"]
    },
    {
        "name": "Diverticulitis",
        "category": "Digestive",
        "symptoms": ["stomach pain", "fever", "constipation", "nausea"],
        "description": "Inflammation of small pouches in the colon.",
        "causes": ["Infection"],
        "prevention": ["High-fiber diet"],
        "risk": ["Older adults"],
        "redflags": ["Severe abdominal pain"]
    },
    {
        "name": "Hemorrhoids",
        "category": "Digestive",
        "symptoms": ["rectal bleeding", "pain", "itching"],
        "description": "Swollen veins in the lower rectum.",
        "causes": ["Straining", "Constipation"],
        "prevention": ["High-fiber diet", "Drink water"],
        "risk": ["Adults"],
        "redflags": ["Heavy bleeding"]
    },
    {
        "name": "Prostatitis",
        "category": "Urinary",
        "symptoms": ["fever", "painful urination", "pelvic pain"],
        "description": "Inflammation of the prostate gland.",
        "causes": ["Bacterial infection"],
        "prevention": ["Maintain hygiene"],
        "risk": ["Adult men"],
        "redflags": ["Unable to urinate"]
    },
    {
        "name": "Benign Prostatic Hyperplasia",
        "category": "Urinary",
        "symptoms": ["frequent urination", "difficulty urinating"],
        "description": "Non-cancerous enlargement of the prostate.",
        "causes": ["Aging"],
        "prevention": ["Regular checkups"],
        "risk": ["Older men"],
        "redflags": ["Complete urinary blockage"]
    },
    {
        "name": "Endometriosis",
        "category": "Reproductive",
        "symptoms": ["pelvic pain", "painful periods", "fatigue"],
        "description": "A condition where tissue similar to the uterine lining grows outside the uterus.",
        "causes": ["Unknown"],
        "prevention": ["No known prevention"],
        "risk": ["Women"],
        "redflags": ["Severe pelvic pain"]
    },
    {
        "name": "Polycystic Ovary Syndrome",
        "category": "Reproductive",
        "symptoms": ["weight gain", "irregular periods", "acne"],
        "description": "A hormonal disorder affecting women.",
        "causes": ["Hormonal imbalance"],
        "prevention": ["Healthy lifestyle"],
        "risk": ["Women"],
        "redflags": ["Heavy bleeding"]
    },
    {
        "name": "Dengue Hemorrhagic Fever",
        "category": "Viral",
        "symptoms": ["high fever", "bleeding", "stomach pain", "vomiting"],
        "description": "A severe form of dengue infection.",
        "causes": ["Dengue virus"],
        "prevention": ["Prevent mosquito bites"],
        "risk": ["Children"],
        "redflags": ["Shock", "Severe bleeding"]
    },
    {
        "name": "Acute Respiratory Distress Syndrome",
        "category": "Respiratory",
        "symptoms": ["difficulty breathing", "rapid breathing", "low oxygen"],
        "description": "A life-threatening lung condition.",
        "causes": ["Severe infection", "Trauma"],
        "prevention": ["Treat severe illness promptly"],
        "risk": ["ICU patients"],
        "redflags": ["Respiratory failure"]
    }
] 