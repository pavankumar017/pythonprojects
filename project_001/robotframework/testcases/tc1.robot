***Settings***
Library  SeleniumLibrary
Resource  ../keywords/tc1_keyword.robot   


*** Variables ***
${url}    https://demo.nopcommerce.com/login?returnUrl=%2F 

***Test Cases***
Logintest
    [Tags]  sanity
   Open Browser    ${url}    browser=chrome
   Click Link    xpath://a[@class="ico-login"]
   cl
   # here tryng to to pass email and pwd as arguments
   Then loginact email pwd
  
TC1
    [Tags]  regression
    ope
    Log  message=asasda

TC3
    [Tags]  NEW1
    Open Browser    url=https://www.facebook.com/    browser=chrome



# *** Keywords ***
# loginact
#    Input Text    id:Email    Email
#    Input Password    id:Password    hjasghjd
#    Click Element    xpath://button[@type='submit']
