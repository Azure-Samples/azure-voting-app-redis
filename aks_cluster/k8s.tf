resource "azurerm_resource_group" "rg" {
  name     = "testResourceGroup"
  location = "southeastasia"
}

resource "azurerm_kubernetes_cluster" "k8s" {
  name                = "aksCluster"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "testk8s"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_d2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }
}
