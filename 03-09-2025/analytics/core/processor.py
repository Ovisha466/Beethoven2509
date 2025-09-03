from .validator import validate_data
def process_data(data):
    if(not validate_data(data)):
       return f'Processed Data:{data}' 
    return f'Invalid Data'

