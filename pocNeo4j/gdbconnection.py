from neo4j import GraphDatabase
import os

class Neo4jConnection:
    def __init__(self):
        uri = "neo4j://localhost:7687"  
        username = os.environ.get('neo4j_user')  
        password = os.environ.get('neo4j_password')
        self._driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self._driver.close()


# -------------------- ADD NODE METHOD -------------------- #

    def add_node(self, label, properties):
        with self._driver.session() as session:
            result = session.execute_write(self._add_node, label, properties)
            return result
    @staticmethod
    def _add_node(tx, label, properties):
        query = "CREATE (n:`$node_label` $properties) RETURN n"
        parameters = {"node_label": label, "properties": properties}
        result = tx.run(query, parameters)
        return result.single()[0]
    

# -------------------- DELETE ALL METHOD -------------------- #
    
    def delete_node(self):
         with self._driver.session() as session:
            session.execute_write(self._delete_node)

    @staticmethod
    def _delete_node(tx):
        query = "MATCH (n) DETACH DELETE n"
        tx.run(query)
    
# -------------------- MERGE NODE METHOD -------------------- #
    def merge_node(self, label, properties):
        with self._driver.session() as session:
            result = session.execute_write(self._merge_node, label, properties)
            return result

    @staticmethod
    def _merge_node(tx, label, properties):
        property_str = ', '.join([f'{key}: ${key}' for key in properties.keys()])
        query = f"MERGE (n:{label} {{ {property_str} }}) RETURN n"

        result = tx.run(query, **properties)
        return result.single()[0]

# -------------------- EXECUTE A NODE METHOD -------------------- #
    def execute_query(self, query, parameters):
        with self._driver.session() as session:
            result = session.execute_write(self._execute_query, query, parameters)
        return result 
    
    @staticmethod
    def _execute_query(tx, query, parameters):
        tx.run(query, parameters)
        result = tx.run(query, **parameters)
        return result
