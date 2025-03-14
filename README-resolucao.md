# Entrega da Atividade DDD-3

### Alunos:

| Nome                           | RM      |
|--------------------------------|--------|
| FERNANDO REBELATO SAETA       | 359961 |
| INGO HENRIQUE ALMENDROS GIRÃO | 358616 |
| KALEO VIEIRA LEITE            | 359754 |
| NATHAN GRECCO FONSECA         | 359289 |


## 1. Identifique as Entidades e Value Objects do seu domínio:

| **Elemento**            | **Tipo**         | **Explicação** |
|-------------------------|-----------------|---------------|
| **Player**               | Entidade        | Possui identidade única e guarda as informações variáveis dos usuários. |
| **Local**                 | Entidade        | Pode personalizar seu conteúdo que será disponibilizado para o agendamento de partidas |
| **Esporte**                 | Entidade        | Objetos importantes para a estratégia do Negócio.  |
| **Modalidade do Esporte**                 | Value Object        | Relacionado sempre a um esporte, não podendo ser editado, somente selecionado na criaçãoi de partidas.  |
| **Email**                    | Value Object    | Não muda e sempre pertence a um único player. |
| **Horário**                    | Value Object    | Não pode conflitar horário (data e hora) para o mesmo local. |
| **Endereço**               | Value Object    | Se o paciente mudar de endereço, um novo objeto será criado. |


## 2. Defina os Agregados e seu Aggregate Root:

| **Elemento**            | **Tipo**         | **Explicação** |
|-------------------------|-----------------|---------------|
| **Time**    | Aggregate | Utilizado para agregar players para organização de partidas. |
| **Players**    | Aggregate | Utilizado para agregar os players cadastrados em uma partida e o status referente à inscrição. |
| **Partida (Agregado)**    | Aggregate Root  | Relaciona os objetos principais para o domínio do app. (Players, Locais, Times e Esportes). |

## 3. Implemente um diagrama mostrando as relações entre os elementos:

![Context Map](/DDD-3/classes-uml.jpg)


## 4. Crie a interface do repositório para persistência do agregado:

CLASSES IMPLEMENTADAS EM [MODELS](/models)
