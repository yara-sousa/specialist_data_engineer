# Guia Rápido: Terraform

## 1. Instalar o Terraform
Baixe em: https://www.terraform.io/downloads.html

## 2. Comandos Básicos

### Inicializar o projeto
```bash
terraform init
```

### Validar arquivos de configuração
```bash
terraform validate
```

### Visualizar o que será criado/modificado
```bash
terraform plan
```

### Aplicar as mudanças (criar/alterar recursos)
```bash
terraform apply
```

### Destruir todos os recursos gerenciados
```bash
terraform destroy
```

## 3. Estrutura Básica de um Arquivo

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "exemplo" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}
```

## 4. Dicas

- Arquivos terminam com `.tf`
- Use variáveis para tornar o código reutilizável
- Sempre revise o `terraform plan` antes de aplicar mudanças

## 5. Documentação