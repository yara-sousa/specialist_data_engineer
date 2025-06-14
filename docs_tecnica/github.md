# Guia Rápido: Branches no Git

## Criar uma nova branch
```bash
git checkout -b nome-da-branch
# ou (Git 2.23+)
git switch -c nome-da-branch
```

## Listar todas as branches
```bash
git branch
```

## Trocar para uma branch existente
```bash
git checkout nome-da-branch
# ou
git switch nome-da-branch
```

## Renomear a branch atual
```bash
git branch -m novo-nome
```

## Deletar uma branch local
```bash
git branch -d nome-da-branch
```

## Enviar branch para o repositório remoto
```bash
git push origin nome-da-branch
```

## Deletar uma branch no repositório remoto
```bash
git push origin --delete nome-da-branch
```