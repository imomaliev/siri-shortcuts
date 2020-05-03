# siri-shortcuts
Siri shortcuts project

## Setup steps

### Zapier
1. add webhook
2. put python code in it

### Shortcuts
1. Url with webhook
2. Text -> Var for Login, Password, Email
3. Ask for input "When":Date
4. Get date from "prev" -> Var
5. Get contens of "Url". POST request with json data of `{"login": ..., "password": ..., "email": ..., "date": ...}`
6. Speak Date
7. End shortcut
