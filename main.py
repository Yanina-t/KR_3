from app.utils import get_operations, get_sorted_operations
from settings import OPERATION_PATH

operations = get_operations(OPERATION_PATH)
executed_sort_operations = get_sorted_operations(operations)

executed_operations = []

def main ():
    operations: list[dict] = File(DATA_JSON).get_data()
    for operation in operations:
        if "EXECUTED" in operation["state"]:
            executed_operations.append(operation)
    return executed_operations

