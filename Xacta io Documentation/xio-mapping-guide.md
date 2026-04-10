




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 1 of 19


















## Xacta.io Mapping Guide
## 4.0
## May 2025









Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 2 of 19
## Xacta
## ®
is a premier suite of cyber risk management and automation software solutions developed by Telos Corporation
(“Telos”) and launched in August 2000. Xacta content is protected under the copyright laws of the United States of
America and is the property of Telos or the party credited as the provider of the content. Copyright © 2000 – 2025. All
## Rights Reserved.
Xacta has been developed at private expense and embodies certain trade secrets and other confidential, proprietary,
and commercially-sensitive information that Telos safeguards through various measures implemented to maintain
confidentiality and prevent unauthorized use or disclosure.
Access to and use of Xacta is subject to the terms of a license agreement with Telos (a “License”) and is restricted to
Authorized Users of the Customer (the “Licensee”) that has been granted a License from Telos. “Authorized Users”
means the employees, consultants, contractors, agents, or other designees of the Licensee who are authorized by the
Licensee to use Xacta in accordance with the license granted by Telos and who have been supplied user login keys and
credentials by the Licensee or Telos.
If  the Licensee of Xacta software solutions and/or documentation is the U.S. Government or an agency thereof, or
anyone licensing Xacta on behalf of the U.S Government, the following notice is applicable:
U.S. GOVERNMENT END USERS: Xacta software solutions and/or documentation delivered to U.S. Government
end users are “commercial computer software” and “restricted computer software” as these terms are used in
applicable Federal Acquisition Regulation (FAR) and Defense Federal Acquisition Regulation Supplement (DFARS)
clauses, and agency-specific supplemental regulations. As such, the use, duplication, disclosure, modification,
and adaptation of the Xacta software solutions and/or documentation, and rights in technical data, shall be
subject to the terms and restrictions set forth in the License applicable to the Xacta software solutions, and
restrictions set forth in applicable FAR and DFARS clauses. See, e.g., FAR 12.211 (Technical Data), FAR 12.212
(Software), FAR 52-227-14 (Rights in Data-General), FAR 52-227-19 (Commercial Computer Software License),
DFARS 252.227-7015 (Technical Data – Commercial Items), and DFARS 227.7202-3 (Rights in Commercial
Computer Software or Computer Software Documentation). No other rights are granted to the U.S.
## Government.
No Xacta user or other party may, without the express written permission of Telos or other rights owner, as
applicable: 1) reverse engineer or otherwise attempt to discover the source code, object code or underlying structure,
ideas, know-how or algorithms of Xacta; 2) copy, reproduce, distribute, publish, display, perform, modify, create
derivative works, transmit, or in any way exploit the content of Xacta; 3) distribute any part of Xacta content over any
network, including a local area network, or sell or offer it for sale, or; 4) use Xacta source code or content to construct
any kind of database or to develop or enhance a competing Governance, Risk and Compliance (GRC) solution.
Furthermore, no user or other party may alter or remove any copyright or other notice from Xacta or Xacta content.
Xacta is a registered trademark of Telos Corporation. All other registered trademarks and unregistered common law
trademarks that appear in Xacta content are the property of their respective holders.
This document is furnished for informational purposes only. The material presented in this document is believed to be
accurate at the time of release. However, Telos assumes no liability in connection with this document except as set
forth in the License under which the document is furnished.





Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 3 of 19


## Contents
Overview ............................................................................................................................................................................................................ 5
Mapping Scanner Data with Xacta.io ............................................................................................................................................ 6
Amazon Inspector ....................................................................................................................................................................................... 6
AWS Config ...................................................................................................................................................................................................... 7
McAfee................................................................................................................................................................................................................. 7
Nessus .................................................................................................................................................................................................................. 9
Nexpose (Rapid7) ....................................................................................................................................................................................... 13
Qualys ................................................................................................................................................................................................................ 13
Qualys (Azure) .............................................................................................................................................................................................. 14
Splunk ................................................................................................................................................................................................................ 14
Symantec ........................................................................................................................................................................................................ 16
Tenable.sc ....................................................................................................................................................................................................... 17






Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 4 of 19

## Change History



## Version
## Number
Date of Last Revision Comments
1.0 04/29/2021 New document
## 2.0 01/09/2022
Add information regarding Notes
values
## 3.0 04/16/2024
Add information re: Asset Role;
Add Qualys (Azure)
## 4.0 04/04/2025
Add information re: JSON imports;
Updated cover page and copy
right page




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 5   of 19
## Overview
This article is applicable to the following:

## Product License Type Release /
## Build
## Number
OS Database
## Xacta.io

## Xacta.io 1.4.1
and higher


This article aims to provide users information on how each data from different scanners
supported by Xacta.io are mapped to a specific Xacta.io field. These scanner data are retrieved
by Xacta.io from Splunk, which uses a Common Information Model (CIM) tool that helps
normalize data to match a common standard using the same field names; for more information,
please refer to the Configuring Splunk Integration article.
Xacta.io supports the following data from the following asset and vulnerability scanners; how
each data is mapped to a specific Xacta.io field is detailed in the
Mapping Scanner Data with
## Xacta.io:
## • Amazon Inspector
- AWS Config
- McAfee
## • Nessus
- Nexpose (Rapid7)
## • Qualys
- Qualys (Azure)
## • Splunk
## • Symantec
## • Tenable.sc





Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 6   of 19
Mapping Scanner Data with Xacta.io
Each scanner data is mapped to a specific Xacta.io field, which allows users to easily determine
where the scanner data will be displayed in Xacta.io when it is imported in the application. It is
important to note that only scan data in XML, JSON, CSV, ZIP, and GZIP formats can be imported
into Xacta.io; please refer to the Xacta.io User Guide for more information. For JSON imports,
note that Scan Results other than “pass” or “n/a” will be reflected as “fail”.
Below are the lists of the Xacta.io fields and their corresponding fields from each scanner. The
Scanner Data column lists the data retrieved from the scanner. For example, the Amazon
Inspector data named numericSeverity will be displayed in the Scan Result field of Xacta.io.
 Important: Values displayed in the Notes field are pulled from the corresponding scanner
tag. For example,  in Qualys scanner data, all values included within or in the <RESULT> under
<VULN_INFO> tag will also be displayed in the Notes field.

## Amazon Inspector

## Xacta.io Fields Scanner Data
Host Name Findings > networkInterfaces[0]>
privateDnsName
Scan Date Findings > createdAt

Asset Roles Refers to the roles assigned to assets to
categorize how the assets are used in the
system. Note that the asset role must exist in
the application in order for the Asset Role
mapping to appear on import.
## Cloud
Resource Name Findings > assetAttributes > agentID

Resource Type Findings > assetType
TestResult
## Test Name Findings > Id
## Result Data
Refers to any of the following scanner data; any of these
information will be displayed in the Test Data field:
- Findings > Severity (raw value, no
translation applied)
- Findings > recommendation
Scan Result Findings > numericSeverity
## Notes Findings > Description
Content Findings > attributes > value where findings >
attributes > key = “CVE-ID”





Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 7   of 19
## Xacta.io Fields Scanner Data
## Description Findings > Description
Protocol Findings > attributes > value  where findings >
attributes > key = “PROTOCOL”
Port Findings > attributes > value  where findings >
attributes > key = “PORT”
Peered VPC Findings > attributes > value  where findings >
attributes > key = “PCX_VPC”
Run Time Findings > createdAt
Scanned with Credentials Flag “No”
Risk Factor Findings > severity
The mapping value for Risk Factor are as
follows:
## • Critical = Critical
## • High = High
## • Medium = Medium
## • Low = Low
## • Informational = None
## • Undefined = Unknown
Note: This is not applicable to Network
## Reachability Rules Package.

AWS Config

## Xacta.io Fields Scanner Data
Host Name privateDnsName
Scan Date configurationItemCaptureTime
Scanner Version configurationItemVersion
## Cloud
Cloud Resource ID (ARN) ARN
Cloud Account ID (AWS Account ID) awsAccountId
Resource Name resourceName
Region awsRegion
Resource Type resourceType
Cloud Resource Data All raw data for the resource

McAfee

## Xacta.io Fields Scanner Data
## Host Name System Name




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 8   of 19
## Xacta.io Fields Scanner Data
## System Name Group Notes
## Scan Date Last Detected Time
Scanner Version Product Version (VirusScan Enterprise)
## Vendor Data
## Model System Model
## Vendor Info System Manufacturer
## Serial System Serial Number
## Operating System
OS Name OS Type
OS Build OS Build Number
OS Version OS Version
OS Patch OS Service Pack Version
OS Family OS Type (parse to determine Unix, Mac,
Windows, etc)
## Software
## Software Name Software
## Software Version Software Version
## Endpoint Data
Virus Scan Product Version Product Version (VirusScan Enterprise)
Virus Scan Engine Version Engine Version (VirusScan Enterprise)
Virus Scan Patch Num Hotfix/Patch Version (VirusScan Enterprise)
AntiSpyware Version Product Version (AntiSpyware)
DAT Version DAT Version (VirusScan Enterprise)
HIP Version Product Version (Host Intrusion Prevention)
HIP Patch Num Hotfix/Patch Version (Host Intrusion
## Prevention)
HIPStatus Host IPS Status (Host IPS)
HIP Firewall Status Firewall Status (Host IPS)
## Last Definition Date Last Detected Time
TestResult (Note that each record is a new result)
Vendor ID The value displayed depends on the dictionary
used. If CVE is populated, the value displayed
is FaultlineID. If   the CCE is populated, the
value displayed is the value of the CCE. If there
are no CVE or CCE, the Vendor ID value is
FaultlineID.
Test Name FaultlineID Title (Note that faultlineID will be
used if faultlineID Title is not present)
## Result Data Result
Scan Result Result is displayed as value if CVEs exist or
both CVE and CCE do not exist. If the value is
Vulnerable, indicate it as test failure. If no CVE
exist and CCE exists, test passes if CCE
Compliance is pass.
Raw Result Result is displayed as value if CVE is present or
both CVE and CCE are not present. CCE
Compliance is displayed as value when CCE is
present and CVE is not.
Content For CVE is displayed as value if it does not
equal CVE-MAP-NOMATCH, split by comma.




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 9   of 19
## Xacta.io Fields Scanner Data
The value is Content Name if the content type
is CVE. For CCE, the value is the content name
if the content type is CCE.
## Run Time  Last Detected Time
Scanned with Credentials Flag The value for this field is True

## Nessus

## Xacta.io Fields Scanner Data
Host Name Returns the content of <tag name=”netbios-
name”>, <tag name=”hostname”> or <tag
name=”host-fqdn”> from the ReportHost name
attribute. If none of the above are available, the
hostname value will be the same as the IP.
Scan Date Returns the content of <tag
name=”HOST_START”>

## Vendor Data
Serial Returns the content of <tag name =”aws-
instance-xxxx”> or  <tag name=”aws-instance-
xxxx-xxxx”>.
## Operating System
OS name Returns the content of <tag name=”operating-
system”>. The Name attribute of tag that starts
with cpe- then parse out OS information out of
CPE if CPE starts with cpe:/o. If this condition is
met, the value should be the parsed CPE value
from plugin_output.
OS build Parsed from CPE (refer to OS name)
OS version Parsed from CPE (refer to OS name)
OS patch Parsed from CPE (refer to OS name)
OS family Returns the content of <tag name=”operating-
system”> (parse to determine UNIX, Mac,
Windows, etc.)
## Cloud
Cloud Account ID (AWS Account ID) Returns the content of <tag name=”aws-
instance-accountid”>
Resource Name Returns the content of <tag name=”aws-
instance-instanceid”>.
Region Returns the content of <tag name=”aws-
instance-region”>
Resource Type EC2
Cloud Resource Data The value will be based from the following tags:
- <tag name=”aws-intance-xxxx”>
- <tag name=”aws-instance-xxxx-xxxx”>
NetAdapater




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 10  of 19
## Xacta.io Fields Scanner Data
IP Returns the name attribute of ReportHost <tag
name=”host-ip”>
Mac Address Returns the content of <tag name=”mac-
address”>
## Software
Name Returns the name attribute of tag that starts
with cpe- then parse out OS information out of
CPE if CPE starts with cpe:/a. If the vedor ID is
20811, the value for OS name is plugin_output
Version The version value displayed is parsed from CPE
app name. If the Vendor ID is 28011, the value
for OS name is plugin_output
Vendor Parsed from CPE app name
CPE Returns the content of tag when name
attribute starts with CPE and the CPE starts
with cpe:/a
Endpoint Data (Note that if the Vendor ID is 16193, the value for OS name is plugin_output)
Virus Scan Product Version Returns the content of regex:(((mcafee
virusscan enterprise)|(symantec endpoint
protection))\s*:\s*\d+\.\d+\.\d+\.\d+)
Note: Use the first match group with no
spaces.
Virus Scan Engine Version Returns the content of regex: (engine
version\s*:\s*\d+\.\d+)
AntiSypware Version Returns the content of regex:(((mcafee
virusscan enterprise)|(symantec endpoint
protection))\s*:\s*\d+\.\d+\.\d+\.\d+)
Note: Use the first match group with no
spaces.
DAT Version Returns the content of regex: (DAT
version\s*:\s*\d+\.\d+)
Last Definition Date Returns the content of regex: (updated
date\s*:\s*\d+\.\d+)

Note: The format of the date will be in
YYYY/MM/DD for McAfee and YYYYMMDD for
Symantec. The tag content will contain the
word McAfee if it was from McAfee and Savce if
it is from Symantec.
TestResult
Vendor ID pluginID attribute under ReportItem tag
Test Name The test name value displayed is the
ReportItem pluginName attribute. If
compliance-check-name exists, use value from
this tag (replace out \t), set to auto-generated
vendorID
Result Data Refers to any of the following scanner data:
- compliance-info
- compliance-reference
- risk_factor
- plugin_output




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 11  of 19
## Xacta.io Fields Scanner Data
- compliance-audit-file
- compliance-check-id
- compliance-actual-value
## Test Data
Refers to any of the following scanner data; any of these
information will be displayed in the Test Data field:
- ReportItem pluginFamily attribute
## • Synopsis
## • Stig_severity
## • Xref
## • Plugin_modification_date
## • Plugin_publication_date
- patch_publication_date
## • Vuln_publication_date
## • Exploitability_ease
## • Exploit_available
## • Exploit_framework_canvas
## • Exploit_framework_metasploit
## • Exploit_framework_core
## • Metasploit_name
## • Canvas_package
## • Cvss_vector
## • Cvss_base_score
## • Cvss_temporal_score
## • Plugin_type
Scan Result If compliance-result or pci-dss-compliance tag
exists, test failed if the value is either Warning,
Skipped, Failed, or Error. Otherwise, set to fail if
the Severity is > = 1. If the compliance-tag exists,
the value of N/A is set when compliance tag is
## INFO.
Raw Result If the compliance-tag does not exist, the raw
result value is the value of the severity. If




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 12 of 19
## Xacta.io Fields Scanner Data
severity value is not within 0 to 4, the value will
be Cleared.
If the compliance-tag exists, use value from the
compliance-result or pci-dss-compliance
severity mapping to result:
## 0=info
## 1=low
## 2=medium
## 3=high
## 4=critical
## Notes Solution
Content The content type displayed for CVE is CVE while
the content type displayed for CWE is CWE.
For compliance-check-name, find any CCEs
from the content and add it with the content
type of CCE.
For compliance-info, find any CCI and add it
with the content type of the CCI.
For controls, find any controls and add it with
the content type of IAC.
For compliance-reference, parse out controls
where controls type is in (800-53, ISO/IEC-2700,
8500.2, Vuln-ID, PCI-DSSv3.1, 800-171, CSF, ITSG-
33, HIPAA) and add as content type for IAC.
For xref-, parse out IAVA: and IAVAB: and add as
content where content type is Alert.
## Description Description
Protocol ReportItem protocol attribute
Port ReportItem port attribute
Run Time Returns the content of <tag
name=”HOST_START”>
Scanned with Credentials Flag <tag name=”Credentialed_Scan”> is set to true
if any of the following values are contained in
the tag: Yes, True, or Success
Skipped Flag Compliance-tag exists, but value is not
recognized if it is not within Warning, Skipped,
Failed, Passed, Cleared, Error, or Info.
Error Running Test Flag Description = Syntax error
## Risk Factor Risk_factor

## Compliance Name Compliance-check-name






Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 13 of 19
Nexpose (Rapid7)

## Xacta.io Fields Scanner Data
## Host Name Asset Names
## Operating System
OS name  Asset OS Name

OS family Asset OS Family
NetAdapater
IP Asset IP Address
TestResult
Vendor ID Vulnerability ID
## Test Name Vulnerability Title
## Result Data Vulnerable Since
## Test Data Vulnerability Solution, Published On, Service
## Name
Scan Result The Vulnerability Test Result Codes will be
translated into IO Scan Results and will be
mapped to IO values as follows:
- VE, VV, VP, = Fail (IO)
## •
NP, NV = Pass (IO)
## • EE, EV, EP, UK, SD, SV, ER, DS, OV, NT = N/A (IO)
## Raw Result Vulnerability Test Result Code
## Notes Vulnerability Proof
Content Vulnerability CVE IDs
## Description Vulnerability Description
## Protocol Service Protocol
## Port Service Port
Skipped Flagged TRUE
## Risk Factor Vulnerability Severity Level

## Qualys

## Xacta.io Fields Scanner Data
Host Name <NETBIOS_HOSTNAME>
Scan Date <GENERATION_DATETIME>

## Operating System
OS name  <OPERATING_SYSTEM>

TestResult
Vendor ID <QID>
Test Name <Title>
Test Data Solution, Threat, Impact, PCI Flag




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 14 of 19
## Xacta.io Fields Scanner Data
Scan Result PCI 0 = Pass; PCI 1 = Fail
Raw Result PCI 0 = Pass; PCI 1 = Fail
Notes <RESULT> under <VULN_INFO>
Content <CVE_ID><ID>
Description <THREAT>
Protocol <VULN_INFO><PROTOCOL>
Port <VULN_INFO><PORT>
Qualys (Azure)

## Xacta.io Fields Scanner Data
Host Name <NETBIOS_HOSTNAME>
Scan Date <GENERATION_DATETIME>

## Operating System
OS name  <OPERATING_SYSTEM>

TestResult
Vendor ID <QID>
Test Name <Title>
Test Data Solution, Threat, Impact, PCI Flag
Scan Result PCI 0 = Pass; PCI 1 = Fail
Raw Result PCI 0 = Pass; PCI 1 = Fail
Notes <RESULT> under <VULN_INFO>
Content <CVE_ID><ID>
Description <THREAT>
Protocol <VULN_INFO><PROTOCOL>
Port <VULN_INFO><PORT>

## Splunk

## Xacta.io Fields Scanner Data
Host Name asset_ds.hostName
System Name asset_ds.systemName
Scan Date asset_ds.scanDate

Scanner Version asset_ds.scannerVersion

Ram Size asset_ds.ramSize
## Vendor Data
Vendor Info vendorInformation.vendorInfo
Model vendorInformation.systemModel
Serial vendorInformation.serial
## BIOS
manufacturer bios.biosManufacturer




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 15  of 19
## Xacta.io Fields Scanner Data
Date bios.biosDate
Version bios.biosVersion
## CPU
Model cpu.cpuModel
Clock cpu.cpuClock
## Operating System
OS Name os.osName
OS Build os.osBuild
OS Version os.osVersion
OS Patch os.osPatch
OS family os.osFamily
OS CPE os.osCPE
External ID cloud.externalId
## Cloud
Cloud Resource ID (ARN) cloud.cloudResourceId
Cloud Account ID (AWS Account ID) cloud.cloudAccountId
Resource Name cloud.resourceName
Region cloud.region
Resource Type cloud.resourceType
Cloud Resource Data cloud.resrouceData
## POC
POC Name poc.pocName
POC Org poc.pocOrganization
POC Phone poc.pocPhone
POC Email poc.pocEmail
POC Location poc.pocLocation
POC Title poc.pocTitle
NetAdapter
IP netAdapater.ipAddress
MAC Address netAdapater.macAddress
## Software
Name software.softwareName
Version software.softwareVersion
Vendor software.softwareVendor
CPE software.softwareCpe
## Endpoint Data
Virus Scan Product Version endpointData.virusScanProductVersion
Virus Scan Engine Version endpointData.virusScanEngineVersion
Virus Scan Patch Num endpointData.virusScanPatchNum
AntiSpyware Version endpointData.antiSpywareVersion
DAT Version endpointData.datversion
HIP Version endpointData.hipVersion
HIP Patch Num endpointdata.hipPatchNum
HIP Status endpointData.hipStatus
HIP Firewall Status endpointData.firewallStatus
Last Definition Date endpointData.lastDefinitionDate
Last Scan endpointData.lastScan
TestResult
Vendor ID testResult.vendorId
Test Name testResult.testName




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 16 of 19
## Xacta.io Fields Scanner Data
Result Data testResult.resultData
Test Data testResult.testData
Scan Result testResult.result
Raw Result testResult.rawResult
Notes testResult.notes
Content testResult.content
Description testResult.description
Protocol testResult.protocol
Port testResult.port
Run Time testResult.runTime
Scanned With Credentials Flag testResult.scannedWithCredentialsFlag
Error Running Test Flag testResult.errorRunningTestFlag
Risk Factor testResult.riskFactor
Compliance Name testResult.complianceCheckName

## Symantec

## Xacta.io Fields Scanner Data
Host Name COMPUTER_NAME

System Name GROUPNAME
Scan Date LAST_SCAN_TIME
Scanner Version AGENT_VERSION

## Operating System
OS name OPERATION_SYSTEM

OS patch SERVICE_PACK
OS family OPERATION_SYSTEM

NetAdapter
## IP IP_ADDR1

## Endpoint Data
Virus Scan Product Version AGENT_VERSION

Virus Scan Engine Version CIDS_ENGINE_VERSION

Virus Scan Patch Num AGENT_VERSION
AntiSpyware Version AGENT_VERSION

DAT Version PATTERNDATE
HIP Version CIDS_ENGINE_VERSION

HIP Patch Num CIDS_ENGINE_VERSION





Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 17  of 19
## Xacta.io Fields Scanner Data
HIP Status CIDS_DRV_ONOFF

HIP Firewall Status FIREWALL_ONOFF

Last Definition Date LAST_UPDATE_TIME

Last Scan LAST_SCAN_TIME

## Tenable.sc

## Xacta.io Fields Scanner Data
Host Name Returns the content of <tag name=”netbios-
name”>, <tag name=”hostname”> or <tag
name=”host-fqdn”> from the ReportHost name
attribute. If none of the above are available, the
hostname value will be the same as the IP.
Scan Date Returns the content of <tag
name=”HOST_START”>
## Operating System
OS name Returns the content of <tag name=”operating-
system”>. The Name attribute of tag that starts
with cpe- then parse out OS information out of
CPE if CPE starts with cpe:/o. If this condition is
met, the value should be the parsed CPE value
from plugin_output.
OS build Parsed from CPE (refer to OS name)
NetAdapater
IP Returns the name attribute of ReportHost <tag
name=”host-ip”>
Mac Address Returns the content of <tag name=”mac-
address”>
## Software
## Name <plugin_output>

## Version <plugin_output>
CPE Returns the content of tag when name
attribute starts with CPE and the CPE starts
with cpe:/a
## Endpoint
Last Scan <tag_name=”HOST_END”>
TestResults
Vendor ID pluginID attribute under ReportItem tag.
Test Name The test name value displayed is the
ReportItem pluginName attribute. If
compliance-check-name exists, use value from
this tag (replace out \t), set to auto-generated
vendorID.
Result Data Refers to any of the following scanner data:




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 18 of 19
## Xacta.io Fields Scanner Data
- compliance-info
- compliance-reference
- risk_factor
- plugin_output
- compliance-audit-file
- compliance-check-id
- compliance-actual-value

Test Data Refers to any of the following scanner data; any
of these information will be displayed in the
Test Data field:
- ReportItem pluginFamily attribute
## • Synopsis
## • Stig_severity
## • Xref
## • Plugin_modification_date
## • Plugin_publication_date
- patch_publication_date
## • Vuln_publication_date
## • Exploitability_ease
## • Exploit_available
## • Exploit_framework_canvas
## • Exploit_framework_metasploit
## • Exploit_framework_core
## • Metasploit_name
## • Canvas_package
## • Cvss_vector




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 |
www.telos.com

Xacta.io Mapping Guide | May 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 19 of 19
## Xacta.io Fields Scanner Data
## • Cvss_base_score
## • Cvss_temporal_score
## • Plugin_type
Scan Result If compliance-result or pci-dss-compliance tag
exists, test failed if the value is either Warning,
Skipped, Failed, or Error. Otherwise, set to fail if
the Severity is > = 1. If the compliance-tag exists,
the value of N/A is set when compliance tag is
## INFO.
Raw Result If the compliance-tag does not exist, the raw
result value is the value of the severity. If
severity value is not within 0 to 4, the value will
be Cleared.
If the compliance-tag exists, use value from the
compliance-result or pci-dss-compliance
severity mapping to result:
## 0=info
## 1=low
## 2=medium
## 3=high
## 4=critical
Content The content type displayed for CVE is CVE while
the content type displayed for CWE is CWE.
For compliance-check-name, find any CCEs
from the content and add it with the content
type of CCE.
For compliance-info, find any CCI and add it
with the content type of the CCI.
For controls, find any controls and add it with
the content type of IAC.
For compliance-reference, parse out controls
where controls type is in (800-53, ISO/IEC-2700,
8500.2, Vuln-ID, PCI-DSSv3.1, 800-171, CSF, ITSG-
33, HIPAA) and add as content type for IAC.
For xref-, parse out IAVA: and IAVAB: and add as
content where content type is Alert.
Description Gets all the Plugins matching the filters, if
provided.
Protocol ReportItem protocol attribute
Run Time Returns the content of <tag
name=”HOST_START”>
Scanned with Credentials Flag <tag name=”Credentialed_Scan”> is set to true
if any of the following values are contained in
the tag: Yes, True, or Success
Risk Factor severity=””
