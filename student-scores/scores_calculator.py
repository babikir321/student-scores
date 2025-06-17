import pandas as pd  

def calculate_scores(theory_path, practical_path):  
    theory = pd.read_csv(theory_path)  
    practical = pd.read_csv(practical_path)  

    merged = pd.merge(theory, practical, on="student_name")  
    merged["final_score"] = (merged["theory"] * 0.3) + (merged["practical"] * 0.7)  
    return merged  

results = calculate_scores("data/theory.csv", "data/practical.csv")  
print(results)  