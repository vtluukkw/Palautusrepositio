*** Settings ***
Resource  resource.robot
Test Setup  User cannot register with invalid credentials

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  harri  harri123
    Create User  harri  harri123
    Output Should Contain  User with username harri already exists

Register With Too Short Username And Valid Password
    Create User  a  kalle123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Create User  123123  kalle123
    Output Should Contain  Username contains invalid characters

Register With Valid Username And Too Short Password
    Create User  pekka  p1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  janne  jannejanne
    Output Should Contain  Password too weak

*** Keywords ***
User cannot register with invalid credentials
    Create User  kalle  kalle123
    Input New Command