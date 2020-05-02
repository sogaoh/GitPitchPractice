from diagrams import Cluster, Diagram
from diagrams.gcp.network import DNS
from diagrams.azure.web import AppServices
from diagrams.azure.database import DatabaseForMysqlServers
from diagrams.azure.compute import FunctionApps
from diagrams.azure.database import CosmosDb

with Diagram("", show=False):
    dns = DNS("dns (GCP)")

    with Cluster("azure_virtual_network internal-it"):
        with Cluster("azurerm_subnet public"):
            snipe_it_web = AppServices("snipe-it")
            stns_api = FunctionApps("stns-api")

        with Cluster("azurerm_subnet db"):
            rdb = DatabaseForMysqlServers("snipe-it-db")
            cosmos_db = CosmosDb("stnd-db")

    dns >> snipe_it_web >> rdb
    dns >> stns_api >> cosmos_db
