
from gdbconnection import Neo4jConnection, execute_merge_query
# connection = Neo4jConnection()
# node_label = 'BUSINESS'
# node_properties = {"name": "John", "age": 30}
# result = connection.add_node(node_label, node_properties)
# print("Node created:", result)


# connection = Neo4jConnection()
# result = connection.delete_node()
# connection.close()

# node_properties = {"name": "John", "age": 30, "Hola":'Andres', "sdada":3123}
# node_label = "ANDRES"
# result = connection.merge_node(node_label, node_properties)
# print("Node merged:", result)



def execute_cypher_query(connection, cypher_query, parameters):
    try:
        result = connection.execute_query(cypher_query, parameters)
        return result
    except Exception as e:
        return str(e)

def main():

    # Create a Neo4jConnection instance
    connection = Neo4jConnection()

    # Cypher query template
    cypher_query_template = (
        "MERGE (c:Customer {name: $customer, age: $age, status: $status }) "
        "MERGE (a:Arrangement {name: $arrangement, attr1: $attr1, attr2: $attr2}) "
        "MERGE (p:Product {name: $product, wwft_tag: $wwft_tag}) "
        "MERGE (c)-[:OWNS]->(a)-[:APPLIES]->(p)"
    )

    # Example JSON input
# Example JSON input with attributes as an array of maps
    json_input = {
        "customer": "Andres",
        "age": 35,
        "status": "Active",
        "arrangement": "arrangement_1",
        "attr1": "value1",
        "attr2": "value2",
        "product": "Savings",
        "wwft_tag": "TRUE"
    }

    try:
        result = execute_cypher_query(connection, cypher_query_template, json_input)
        print("Query executed successfully. Result:", result)
    except Exception as e:
        print("Error:", e)
    finally:
        connection.close()  

if __name__ == "__main__":
    main()





























# def main():
#     connection = Neo4jConnection()
#     # Cypher query
#     cypher_query = (
#        "MERGE (c:Customer {name: $customer}) "
#         "MERGE (a:Arrangement {name: $arrangement}) "
#         "MERGE (p:Product      {name: $product, wwft_tag: $wwft_tag})" 
#         "MERGE (c)-[:OWNES]->(a)-[:APPLIES]->(p)"
#     )
#     query_parameters = {
#         "customer": "Mando",
#         "arrangement": "Arrangement_1",
#         "product": "Morgage",
#         "wwft_tag": "FALSE"
#     }
#     try:
#         result = connection.execute_query(cypher_query, query_parameters)
#         print("Query executed successfully. Result:", result)
#     except Exception as e:
#         print("Error:", e)
#     finally:
#         connection.close() 

# if __name__ == "__main__":
#     main()


# def main():
#     # Neo4j configuration
#     # uri = "bolt://localhost:7687"  # Replace with your Neo4j server's URI
#     # username = "neo4j"  # Replace with your Neo4j username
#     # password = "your_password"  # Replace with your Neo4j password

#     # Create a Neo4jConnection instance
#     connection = Neo4jConnection()

#     # Input parameters
#     input_parameters = {
#         "customer": "Nala",
#         "arrangement": "arrangement_2",
#         "product": {
#             "name": "Savings",
#             "wwft_tag": "FALSE"
#         }
#     }

#     try:
#         result = execute_merge_query(connection, input_parameters)
#         print("Query executed successfully. Result:", result)
#     except Exception as e:
#         print("Error:", e)
#     finally:
#         connection.close()  # Don't forget to close the connection when done

# if __name__ == "__main__":
#     main()