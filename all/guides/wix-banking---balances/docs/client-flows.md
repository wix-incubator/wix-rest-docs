SortOrder: 1
## Use Cases

- [**Get Available balance**](#get-available-balance)

## Get Available balance
It is up to the client decide when to show balances.
Usually cases are
- fetch and show balances on UI when user enters wix checking zone
- period fetch and update balances on UI, so user always sees the latest balances
- show available balance on UI when user initiates transfer

```mermaid
sequenceDiagram
autonumber

    actor U as User
    participant M as Mobile / UI
    participant S as Server
    
    U->>M: Open Home Page<br/>(already passed stepUp)
    Note over M: all subsequent calls to server<br/>are done with BANKING_BASIC_SESSION<br/> stepup_token
    M->>M: Get bankAccountId (up to client how and when)
    M->>+S: Get Bank Account Available Balance by bankAccountId
    S->>-M: Available Balance
    M->>M: Render rest of page
```