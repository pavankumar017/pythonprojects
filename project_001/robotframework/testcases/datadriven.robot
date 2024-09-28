***Settings***
Library  SeleniumLibrary
Resource  ../keywords/tc1_keyword.robot   
Test Template  Login and enter

*** Keywords ***
Enter username
    [Arguments]    ${username}
    Input Text    xpath://input[@type="email"]    ${username}

Enterpwd
    [Arguments]    ${pwd}
    Input Text    id:Password    ${pwd}

Login and enter
    [Arguments]   ${username}  ${pwd}
    Open Browser    https://demo.nopcommerce.com/login?returnUrl=%2F    chrome
    Enter username  ${username}
    Enterpwd  ${pwd}

*** Test Cases ***    ${username} ${pwd}
Login with 1st    pavan1@gmail    asdsad
Login wth 2nd    pavab2@gmail    iyioyo
