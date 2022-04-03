variable "env" {
  type = string
  description = "deployment environment"
}

variable "eks_name" {
  type = string
  description = "the name of EKS"
}

variable "region" {
  type = string
  description = "AWS Region"
}
