***Settings***
Library    SeleniumLibrary


*** Keywords ***
loginact ${email} ${pwd}
   Input Text    id:Email    ${email}
   Input Password    id:Password    ${pwd}
   Click Element    xpath://button[@type='submit']


loginfacebooks ${email} ${pwd}