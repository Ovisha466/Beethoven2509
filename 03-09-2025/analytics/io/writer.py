from ..tools.formatter import format_data
def write_data(data):
    formatted_data= format_data(data)
    return f'Written:{formatted_data}'