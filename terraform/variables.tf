variable "resource_group_name" {
  description = "Name of the Azure resource group"
  default     = "devops-project-rg"
}

variable "location" {
  description = "Azure region for all resources"
  default     = "East US"
}

variable "cluster_name" {
  description = "Name of the AKS cluster"
  default     = "devops-aks-cluster"
}

variable "acr_name" {
  description = "Name of the Azure Container Registry - must be globally unique"
  default     = "diegogambaacr"
}

variable "node_count" {
  description = "Number of nodes in the AKS cluster"
  default     = 1
}

variable "vm_size" {
  description = "VM size for AKS nodes"
  default     = "Standard_DC2s_v3"
}