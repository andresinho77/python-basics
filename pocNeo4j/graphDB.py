
from neo4j import GraphDatabase, RoutingControl
import os


URI = "neo4j://localhost:7687"
AUTH = (os.environ.get('neo4j_user'), os.environ.get('neo4j_password'))


def create_event_wwft_customer(driver, customer, arrangement, product , id, wwft_tag):
    driver.execute_query(
        "MERGE (c:Customer {name: $customer}) "
        "MERGE (a:Arrangement {name: $arrangement}) "
        "MERGE (p:Product      {name: $product, wwft_tag: $wwft_tag})" 
        "MERGE (c)-[:OWNES]->(a)-[:APPLIES]->(p)",
        customer=customer, arrangement=arrangement, product=product, id=id, wwft_tag=wwft_tag, database_="neo4j",
    )
def create_event_wwft_poa(driver, customer, arrangement_n, arrangement_e ):
    driver.execute_query(
        "MERGE (c:Customer {name: $customer}) "
        "MERGE (a:Arrangement {name: $arrangement}) "
        "MERGE (given:Arrangement {name: $arrangement_e})" 
        "MERGE (c)-[:OWNES]->(a)-[:ACCESS]->(given)",
        customer=customer, arrangement=arrangement_n, arrangement_e=arrangement_e, database_="neo4j",
    )

def print_relationship(driver, customer):
    records, _, _ = driver.execute_query(
        "MATCH (c:Customer)-[:OWNES]->(a:Arrangement) WHERE c.name = $customer "
        "RETURN a.name ORDER BY a.name",
        customer=customer, database_="neo4j", routing_=RoutingControl.READ,
    )
    for record in records:
        print(record["a.name"])


with GraphDatabase.driver(URI, auth=AUTH) as driver:   
    create_event_wwft_customer(driver, "Arjan", "Arrangement_product_1", "Current_Account", 1,  "TRUE")
    create_event_wwft_customer(driver, "Mando", "Arrangement_product_2", "Current_Account", 2,"TRUE")
    create_event_wwft_customer(driver, "Biplav", "Arrangement_product_3", "Saving_Account", 3, "TRUE")
    create_event_wwft_customer(driver, "Andres", "Arrangement_product_4", "Morgage_Account", 4, "FALSE")
    create_event_wwft_customer(driver, "Felipe", "Arrangement_product_5", "Saving_Account", 5, "TRUE")
    create_event_wwft_customer(driver, "Lara", "Arrangement_product_6", "Saving_Account", 6, "FALSE")
    create_event_wwft_poa(driver, "Arjan", "Arrangement_product_11", "Arrangement_product_4")
    create_event_wwft_poa(driver, "Mando", "Arrangement_product_31", "Arrangement_product_3")
    print_relationship(driver, "Arrangement_product_11")