import csv

def read_file(file_path):
    """
    Function to read a CSV file and process its contents.
    
    :param file_path: Path to the CSV file.
    :return: List of dictionaries representing the rows in the CSV file.
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        row = 0
        operations = []
        for record in reader:
            if row > 0:
                operations.append({
                    'id': record[0],
                    'type': record[1],
                    'amount': float(record[2].replace('$', '')) if type(record[2]) != float else record[2],
                })
            row += 1
        return proccess_info(operations)
        
def proccess_info(operations):
    """
    Function to process the operations and calculate the final balance and transaction counts.

    :param operations: List of dictionaries representing the transactions.
    :return: None
    """
    credit_transations = 0
    balance_final = 0
    most_values_transactions = 0
    credit_count = 0
    debit_count = 0
    debit_transations = 0

    for transaction in operations:
        if transaction['type'] == 'Crédito':
            credit_transations += float(transaction['amount'])
            credit_count += 1
        elif transaction['type'] == 'Débito':
            debit_transations += float(transaction['amount']) * -1
            debit_count += 1
        else:
            print(f'Tipo de transacción no válida: {transaction.get("id")} {transaction.get("type")}')
        balance_final = credit_transations + debit_transations
    most_values_transactions = max(operations, key=lambda x: x['amount'])
    return print_message(balance_final, most_values_transactions, credit_count, debit_count)

def print_message(balance_final, most_values_transactions, credit_count, debit_count):
    """
    Function to print the final report of transactions.
    :param balance_final: Final balance after all transactions.
    :param most_values_transactions: Transaction with the highest amount.
    :param credit_count: Count of credit transactions.
    :param debit_count: Count of debit transactions.
    :return: None
    """
    print(f"""Reporte de Transacciones:
------------------------------------------------------
Balance Final: {balance_final}
Transaccion de Mayor Monto: ID {most_values_transactions.get('id')} - {most_values_transactions.get('amount')}
Conteo de Transacciones: Credito: {credit_count} Debito {debit_count}
                """)
read_file('./files/operaciones.csv')