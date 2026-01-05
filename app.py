from fastapi import FastAPI
import datetime
import os

app = FastAPI()

@app.get("/api/health")
def health():
    return {
    "eventType": "attributeValueChange",
    "SiebelMessage": {
        "IntObjectName": "SWICustomerPartyIO",
        "IntObjectFormat": "Siebel Hierarchical",
        "ListOfSWICustomerPartyIO": {
            "Account": {
                "Account Number": "88-3EPVLN",
                "Price List": "CME Price List",
                "Primary Billing Profile Id": "88-3EPVMJ",
                "ListOfInternal Division": {
                    "Internal Division": [
                        {
                            "Organization": "Default Organization",
                            "Organization Id": "0-R9NH",
                            "Name": "Default Organization"
                        }
                    ]
                },
                "Primary Bill To Address Id": "",
                "Primary Contact Id": "88-3EMW6U",
                "Integration Id": "",
                "Name": "AGH-Test-Acnt-5",
                "Created": "07/03/2025 23:41:15",
                "Primary Ship To Address Id": "",
                "Price List Id": "88-23AQ7",
                "ListOfAccount_Business Address": {
                    "Account_Business Address": [
                        {
                            "Postal Code": "560086",
                            "State": "AZ",
                            "Address Id": "88-3ENWK9",
                            "Street Address": "Street 101",
                            "Country": "India",
                            "Id": "88-3ENWK9",
                            "City": "Bengaluru",
                            "County": "",
                            "Street Address 2": "HSR layout",
                            "IsPrimaryMVG": "Y",
                            "Province": "",
                            "Apartment Number": ""
                        }
                    ]
                },
                "Main Fax Number": "",
                "Account Status": "Active",
                "Home Page": "",
                "ListOfPosition": {
                    "Position": [
                        {
                            "Account Id": "88-3EPVLN",
                            "Position Id": "0-5220",
                            "Active First Name": "Siebel",
                            "Login Id": "0-1",
                            "Active Email": "sadmin@siebel.com",
                            "Active Job Title": "Sys Admin",
                            "Active Last Name": "Administrator"
                        }
                    ]
                },
                "ListOfCUT Account - Bill To Ship To": {
                    "CUT Account - Bill To Ship To": [
                        {
                            "Row Id": "88-3EPVLN",
                            "Last Modified": "07/04/2025 06:41:15",
                            "Description": "",
                            "Parent Account Id": "",
                            "Primary Bill To Address Id": "",
                            "ListOfCUT Account - Bill To Ship To_Ship To Business Address": {
                                "CUT Account - Bill To Ship To_Ship To Business Address": [
                                    {
                                        "Ship To Country": "India",
                                        "Ship To City": "Bengaluru",
                                        "Address Name": "sam1750157829153@cheers.com-address",
                                        "Ship To Postal Code": "560086",
                                        "Ship To Street Address": "Street 101",
                                        "Ship To County": "",
                                        "Ship To Street Address 2": "HSR layout",
                                        "Id": "88-3ENWK9",
                                        "Ship To Street Address 3": "",
                                        "Ship To State": "AZ",
                                        "Ship To Province": "",
                                        "IsPrimaryMVG": "N"
                                    }
                                ]
                            },
                            "Primary Address Id": "88-3ENWK9",
                            "Name": "AGH-Test-Acnt-5",
                            "Primary Ship To Address Id": "",
                            "ListOfCUT Account - Bill To Ship To_Bill To Business Address": {
                                "CUT Account - Bill To Ship To_Bill To Business Address": [
                                    {
                                        "Bill To Street Address": "Street 101",
                                        "Bill To Street Address 2": "HSR layout",
                                        "Bill To Street Address 3": "",
                                        "Bill To City": "Bengaluru",
                                        "Bill To State": "AZ",
                                        "Bill To Country": "India",
                                        "Bill To Postal Code": "560086",
                                        "Bill To Province": "",
                                        "Bill To County": "",
                                        "Id": "88-3ENWK9",
                                        "IsPrimaryMVG": "N"
                                    }
                                ]
                            },
                            "Main Phone Number": "4562137999",
                            "Main Fax Number": "",
                            "Region": "Asia",
                            "Home Page": "",
                            "Location": "Bengaluru"
                        }
                    ]
                },
                "Row Id": "88-3EPVLN",
                "Parent Account Id": "",
                "ListOfContact": {
                    "Contact": [
                        {
                            "Suppress All Mailings": "N",
                            "First Name": "Sam",
                            "M/M": "",
                            "Middle Name": "",
                            "Gender": "M",
                            "Integration Id": "",
                            "Job Title": "VC",
                            "Suppress All Faxes": "N",
                            "Work Phone #": "9094157390",
                            "Cellular Phone #": "8701804116",
                            "Suppress All Emails": "N",
                            "Consumer Link": "",
                            "Status": "Active",
                            "Row Id": "88-3EMW6U",
                            "Contact Person Title": "",
                            "Social Security Number": "",
                            "Marital Status": "",
                            "Suppress All Calls": "N",
                            "Currency Code": "USD",
                            "Home Phone #": "5551326325",
                            "Primary Organization Id": "0-R9NH",
                            "Alias": "",
                            "Date of Birth": "",
                            "Last Name": "Malone",
                            "Fax Phone #": "",
                            "Email Address": "sam1749725774087@cheers.com",
                            "Mother Maiden Name": ""
                        }
                    ]
                },
                "Account Type Code": "Customer",
                "Primary Address Id": "88-3ENWK9",
                "DUNS Number": "",
                "ListOfCUT Address": {
                    "CUT Address": [
                        {
                            "Ship Address Flag": "N",
                            "Address Type": "",
                            "Row Id": "88-3ENWK9",
                            "Postal Code": "560086",
                            "City": "Bengaluru",
                            "Integration Id": "",
                            "Street Address 2": "HSR layout",
                            "County": "",
                            "Province": "",
                            "Bill Address Flag": "N",
                            "Disable DataCleansing": "N",
                            "Start Date": "07/03/2025",
                            "Address Name": "sam1750157829153@cheers.com-address",
                            "End Date": "",
                            "State": "AZ",
                            "Main Address Flag": "N",
                            "Street Address": "Street 101",
                            "Country": "India",
                            "Email Address": ""
                        }
                    ]
                },
                "Type": "Customer",
                "Main Phone Number": "4562137999",
                "Currency Code": "USD",
                "Master Account Id": "88-3EPVLN",
                "Primary Organization Id": "0-R9NH",
                "ListOfCom Invoice Profile": {
                    "Com Invoice Profile": [
                        {
                            "Bank Authorization flag": "N",
                            "Credit Card Block Flag": "N",
                            "Credit Card Verification Number Encryption Key": "",
                            "Bill Vendor Id": "",
                            "External Billing Account Number - Old": "",
                            "Bank Name": "",
                            "Credit Card Type": "",
                            "Name": "sam1749799277849@cheers.com",
                            "Credit Card Number": "4111111111111111",
                            "ListOfContact Query": {
                                "Contact Query": [
                                    {
                                        "Cell Phone #": "8701804116",
                                        "Row Id": "88-3EMW6U",
                                        "Home Phone #": "5551326325",
                                        "Primary Organization Id": "0-R9NH",
                                        "Work Phone #": "9094157390",
                                        "First Name": "Sam",
                                        "Middle Name": "",
                                        "M/M": "",
                                        "Last Name": "Malone",
                                        "Job Title": "VC",
                                        "Fax Phone #": "",
                                        "Email Address": "sam1749725774087@cheers.com"
                                    }
                                ]
                            },
                            "Bank Account Name": "",
                            "Status": "Active",
                            "Credit Card Expiration Month": "12",
                            "Last Bill Amount": "",
                            "CPNI Flag": "N",
                            "Bill Average": "",
                            "No Pay Form Flag": "N",
                            "Bank Branch": "",
                            "Reason for Manual Outsource": "",
                            "Credit Card Expiration Year": "2029",
                            "Standing Order Flag": "N",
                            "Address Id": "88-3ENWK9",
                            "Id": "88-3EPVMJ",
                            "External Billing Account Number": "",
                            "Account Id": "88-3EPVLN",
                            "Repeat Debtor Flag": "N",
                            "Bank Language Id": "",
                            "Credit Card Block Reason": "",
                            "Credit Card Security Code": "",
                            "Bill Frequency": "Monthly",
                            "Yearly Advance Payment Flag": "N",
                            "Statement Flag": "N",
                            "Bank Account Number": "",
                            "Last Bill Date": "",
                            "Payment Method": "Credit",
                            "Credit Card Expiration Calculated Date": "2029-12-15",
                            "Media Type": "Email",
                            "Credit Card Name": "",
                            "Credit Card Number Encryptkey Reference": "2",
                            "Bank Language Code": "",
                            "ListOfCUT Address Copy": {
                                "CUT Address Copy": [
                                    {
                                        "Row Id": "88-3ENWK9",
                                        "Postal Code": "560086",
                                        "Address Name": "sam1750157829153@cheers.com-address",
                                        "State": "AZ",
                                        "Street Address": "Street 101",
                                        "Country": "India",
                                        "City": "Bengaluru",
                                        "County": "",
                                        "Street Address 2": "HSR layout",
                                        "Province": ""
                                    }
                                ]
                            },
                            "Interest at Invoice Flag": "N",
                            "Bill Type": "Summary",
                            "CPNI Date": "",
                            "Credit Card Category": "",
                            "Bank Account Type": "",
                            "Collections Flag": "N",
                            "Routing Number": "",
                            "Credit Card Verification Number": "",
                            "Budget Billing Flag": "N",
                            "Bill Source": "",
                            "Email Bill To": "",
                            "Contact Id": "88-3EMW6U"
                        }
                    ]
                },
                "Location": "Bengaluru"
            }
        },
        "MessageType": "Integration Object",
        "MessageId": "88-AKPLM"
    }
}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
