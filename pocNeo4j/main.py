from fastapi import FastAPI, HTTPException
from gdbconnection import Neo4jConnection
import os

uri = "neo4j://localhost:7687"  
username = os.environ.get('neo4j_user')  
password = os.environ.get('neo4j_password') 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/all")
async def get_all_nodes():
    query = "MATCH (n) RETURN n"
    connection = Neo4jConnection()
    records = connection.execute_query_all(query)
    if records:
        return {"nodes": records}
    else: 
        raise HTTPException(status_code=404, detail="No nodes found")

@app.get("/wwft")
async def get_all_nodes():
    # query = "MATCH (c:Customer)-[t*..]->()-[]->(p:Product{wwft_tag:'True'})  RETURN c,  p order by c.name"
    query = "MATCH (c:Customer)-[t*..]->(a)-[]->(p:Product{wwft_tag:'True'})  RETURN c, a,  p order by c.name"
    connection = Neo4jConnection()
    records = set(connection.execute_query_all(query))
    if records:
        return {"nodes": records}
    else: 
        raise HTTPException(status_code=404, detail="No nodes found")

@app.post("/create-node/")
def create_item(node_data: dict):

    connection = Neo4jConnection()
    try:
        label = node_data.get("label")
        properties = node_data.get("properties")
        if not label or not properties:
            raise HTTPException(status_code=400, detail="Label and properties must be provided.")
        
        result = connection.add_node(label , properties)
        connection.close()
        return {"node_label": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/delete-node/")
def create_item():
    connection = Neo4jConnection()
    try:
        connection.delete_node()
        connection.close()
        return {"result": "All nodes has been deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/merge_node/")
async def merge_node(node_data: dict):
    connection = Neo4jConnection()
    try:
        label = node_data.get("label")
        properties = node_data.get("properties")
        
        if not label or not properties:
            raise HTTPException(status_code=400, detail="Label and properties must be provided.")

        result = connection.merge_node(label, properties)
        connection.close()
        return {"message": "Node merged successfully", "node": dict(result)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# TODO: Extract the Properties data from Query_data, are required to execute
@app.post("/execute_query/")
async def execute_query(query_data: dict):
    connection = Neo4jConnection()
    try:
        query = (
        "MERGE (c:Customer {name: $customer, age: $age}) "
        "MERGE (a:Arrangement {name: $arrangement, status: $status}) "
        "MERGE (p:Product {name: $product, wwft_tag: $wwft_tag}) "
        "MERGE (c)-[:HAS]->(a)-[:IS]->(p)"
        )
        if not query_data:
            raise HTTPException(status_code=400, detail="Json must be provided.")

        result = connection.execute_query(query, query_data)
        connection.close()
        return {"message": "Query executed successfully", "result": dict(result)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close() 

# @app.post("/execute/")
# async def execute_query(json_input: dict):
#     connection = Neo4jConnection()
#     #Create 
#     cypher_query_template = (
#         "MERGE (c:Customer {name: $customer, age: $age, status: $status }) "
#         "MERGE (a:Arrangement {name: $arrangement, attr1: $attr1, attr2: $attr2}) "
#         "MERGE (p:Product {name: $product, wwft_tag: $wwft_tag}) "
#         "MERGE (c)-[:OWNS]->(a)-[:APPLIES]->(p)"
#     )
#     try:
#         result = connection.execute_query(cypher_query_template, json_input)
#         return {"message": "Query executed successfully", "result": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     finally:
#         connection.close() 