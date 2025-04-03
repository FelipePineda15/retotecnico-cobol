import csv

def read_file(file_path):
    """
    Function to read a CSV file and process its contents.
    
    :param file_path: Path to the CSV file.
    :return: List of dictionaries representing the rows in the CSV file.
    """
    ## Open the CSV file
    # Se utiliza la función open() para abrir el archivo CSV en modo lectura ('r').
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        # Cada fila se almacena como un diccionario con las claves 'id', 'type' y 'amount'.
        # Se utiliza la función float() para convertir el monto a un número decimal.
        # Se utiliza la función replace() para eliminar el símbolo '$' del monto antes de convertirlo a float.
        reader = csv.reader(csvfile)
        next(reader)
        operations = []
        for record in reader:
            operations.append({
                'id': record[0],
                'type': record[1],
                'amount': float(record[2].replace('$', '')) if type(record[2]) != float else record[2],
            })
    # Se devuelve la lista de operaciones procesadas.
    # La lista contiene diccionarios con las transacciones leídas del archivo CSV.
    # Cada diccionario tiene las claves 'id', 'type' y 'amount'.
    # Se utiliza la función return para devolver la lista de operaciones.
        return proccess_info(operations)
        
def proccess_info(operations):
    """
    Function to process the operations and calculate the final balance and transaction counts.

    :param operations: List of dictionaries representing the transactions.
    :return: None
    """
    ## Initialize variables
    # Estas variables se inicializan para almacenar el balance final y los conteos de transacciones.
    # Se inicializan a 0 para evitar errores de referencia antes de la asignación.
    credit_transations = 0
    balance_final = 0
    most_values_transactions = 0
    credit_count = 0
    debit_count = 0
    debit_transations = 0

    ## Process transactions
    # Se itera sobre cada transacción en la lista de operaciones.
    for transaction in operations:
        ## Se verifica el tipo de transacción (Crédito o Débito) y se actualizan las variables correspondientes.
        # Se utiliza un condicional para determinar si la transacción es de tipo 'Crédito' o 'Débito'.
        # Dependiendo del tipo, se suman o restan los montos de las transacciones al balance final.
        if transaction['type'] == 'Crédito':
            credit_transations += float(transaction['amount'])
            credit_count += 1
        elif transaction['type'] == 'Débito':
            debit_transations += float(transaction['amount']) * -1
            debit_count += 1
        else:
            print(f'Tipo de transacción no válida: {transaction.get("id")} {transaction.get("type")}')
        # Se actualiza el balance final sumando las transacciones de crédito y restando las de débito.
        balance_final = credit_transations + debit_transations
    # Se determina la transacción de mayor monto utilizando la función max() y una expresión lambda.
    # Se utiliza la función max() para encontrar la transacción con el monto más alto en la lista de operaciones.
    # La expresión lambda se utiliza para extraer el monto de cada transacción y compararlo.
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
    # Se imprime un mensaje formateado que muestra el balance final, la transacción de mayor monto y el conteo de transacciones.
    # Se utiliza la función print() para mostrar el mensaje en la consola.
    # Se utiliza una cadena de formato para incluir las variables en el mensaje.
    # Se utiliza la función f-string para formatear el mensaje con los valores de las variables.
    print(f"""Reporte de Transacciones:
------------------------------------------------------
Balance Final: {balance_final}
Transaccion de Mayor Monto: ID {most_values_transactions.get('id')} - {most_values_transactions.get('amount')}
Conteo de Transacciones: Credito: {credit_count} Debito {debit_count}
                """)
read_file('./files/operaciones.csv')