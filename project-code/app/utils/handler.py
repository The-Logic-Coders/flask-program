import pandas as pd 


class Handler:
    def __init__(self):
        pass
    
    @staticmethod
    def process_file(content):
        try:
            data = pd.read_excel(content)
        except Exception as e:
            raise ValueError(f'Error reading Excel file: {e}')
        
        data = data.to_dict(orient = 'index')
        print(data)
        
        processed_q = []
        review = []
        for key, val in data.items():
            processed_val = {k.lower(): v for k, v in val.items()}
            if not all (k in processed_val for k in ['question', 'a', 'b', 'c', 'd', 'correct answer','difficulty']):
                review.append(processed_val)
                continue
            processed_q.append({
                'question': processed_val['question'],
                'option_a': processed_val['a'],
                'option_b': processed_val['b'],
                'option_c': processed_val['c'],
                'option_d': processed_val['d'],
                'correct_answer': processed_val['correct answer'],
                'difficulty': processed_val['difficulty'].lower(),
            }
            )
        return processed_q, review
    
                
                
            
        
        
        