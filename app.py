from fastapi import FastAPI
import datetime
import os

app = FastAPI()

@app.get("/api/health")
def health():
    return {
    "eventId": "6897dad3-88e4-0ec2-ac47-f22e03ff6c8e",
    "eventTime": "2025-12-02T06:46:55.835Z",
    "eventType": "PartyAccountPostAttributeValueChangeEvent",
    "correlationId": "",
    "domain": "commercial",
    "title": "PartyAccountPostAttributeValueChangeEvent",
    "description": "PartyAccountPostAttributeValueChangeEvent",
    "priority": "",
    "timeOcurred": "2025-12-02T06:46:55.835Z",
    "fieldPath": "",
    "@baseType": "Event",
    "@type": "Event",
    "event": {
        "partyAccount": {
            "@type": "PartyAccount",
            "accountType": "customer",
            "accountClass": "customer",
            "name": "Child3",
            "externalId": "88-3H7B71",
            "id": "88-3H7B71",
            "billStructure": {
                "@type": "BillStructure",
                "name": "CBP1",
                "id": "88-3H7MS9",
                "cycleSpecification": {
                    "@type": "BillingCycleSpecification",
                    "billingDateShift": 1,
                    "billingPeriod": "yearly",
                    "frequency": "yearly"
                },
                "format": {
                    "@type": "BillFormat",
                    "name": "detail"
                },
                "presentationMedia": [
                    {
                        "@type": "BillPresentationMedia",
                        "name": "disk"
                    }
                ]
            },
            "contact": [
                {
                    "@type": "Contact",
                    "contactName": " ",
                    "contactType": "secondary",
                    "contactMedium": [
                        {
                            "@type": "GeographicAddressContactMedium",
                            "preferred": true,
                            "mediumType": "PostalAddress",
                            "city": "Chicago",
                            "country": "USA",
                            "postCode": "60657",
                            "street1": "3462 N. Lake Shore Drive",
                            "street2": "",
                            "stateOrProvince": "IL"
                        },
                        {
                            "@type": "EmailContactMedium",
                            "mediumType": "Email"
                        },
                        {
                            "@type": "PhoneContactMedium",
                            "mediumType": "Phone"
                        }
                    ],
                    "relatedParty": [
                        {
                            "role": "owner",
                            "@type": "RelatedRelatedPartyOracle",
                            "partyOrPartyRole": {
                                "@type": "RelatedPartyOracle",
                                "@referredType": "Individual",
                                "@baseType": "RelatedParty",
                                "href": "",
                                "id": "88-3H7B71",
                                "name": "Child3"
                            }
                        }
                    ]
                }
            ],
            "state": "active",
            "financialAccount": {
                "@referredType": "FinancialAccount",
                "@type": "FinancialAccountRef",
                "id": "88-3H7B71",
                "name": "Child3"
            },
            "paymentPlan": [
                {
                    "@type": "PaymentPlan",
                    "paymentMethod": {
                        "@type": "PaymentMethodRef",
                        "name": "Bill Me",
                        "id": "88-3H7MS9-PayMthd"
                    },
                    "paymentFrequency": "Monthly",
                    "status": "Active",
                    "totalAmount": {
                        "unit": "USD"
                    },
                    "validFor": {}
                }
            ],
            "defaultPaymentMethod": {
                "@type": "PaymentMethodRef",
                "href": "",
                "id": "",
                "name": "Bill Me"
            },
            "relatedParty": [
                {
                    "role": "owner",
                    "@type": "RelatedRelatedPartyOracle",
                    "partyOrPartyRole": {
                        "@type": "RelatedPartyOracle",
                        "@referredType": "Individual",
                        "@baseType": "RelatedParty",
                        "href": "",
                        "id": "88-3H7B71",
                        "name": "Child3"
                    }
                }
            ],
            "accountRelationship": [
                {
                    "@type": "AccountRelationship",
                    "relationshipType": "Parent",
                    "validFor": {
                        "startDateTime": "",
                        "endDateTime": ""
                    },
                    "billStructure": {
                        "id": "88-3H7MS9"
                    },
                    "account": {
                        "@type": "AccountRef",
                        "@referredType": "BillingAccount",
                        "billStructure": {}
                    }
                }
            ]
        }
    },
    "reportingSystem": {
        "id": "-",
        "name": "-",
        "@type": "ReportingResource",
        "@referredType": "LogicalResource"
    },
    "source": {
        "id": "-",
        "name": "-",
        "@type": "ReportingResource",
        "@referredType": "LogicalResource"
    }
}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
