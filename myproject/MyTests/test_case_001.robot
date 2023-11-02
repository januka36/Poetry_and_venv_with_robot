*** Settings ***
Library          OperatingSystem

*** Test Cases ***
Verify Python Version
    ${output}=    Run    python --version
    Log To Console    ${output}    