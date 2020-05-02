# siri-shortcuts
Siri shortcuts project

## Setup steps
### Shortcuts

1. Dictate text
2. Calendar "Get dates from"
3. Set variable "Date" to "Dates"
4. Run script over SSH. Here we need to create RSA key 2048 and add public key to our server.
5. In run script `cd projects/water && venv/bin/python water.py $Date"
6. Speak Date
7. End shortcut

### Server
1. add user siri
2. put settings in .bashrc but before "interactive" check
