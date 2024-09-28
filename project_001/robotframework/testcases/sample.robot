*** Settings ***
Library    ExcelLibrary


*** Test Cases ***
Forlooptest
    FOR    ${i}    IN  
       Log To Console    ${i}
      
    END    