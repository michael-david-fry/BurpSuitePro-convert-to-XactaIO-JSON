




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 1 of 22


















Xacta.io JSON Data Dictionary
## 2.0
## April 2025








Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 2 of 22
## Xacta
## ®
is a premier suite of cyber risk management and automation software solutions developed by Telos Corporation (“Telos”)
and launched in August 2000. Xacta content is protected under the copyright laws of the United States of America and is the
property of Telos or the party credited as the provider of the content. Copyright © 2000 – 2025. All Rights Reserved.
Xacta has been developed at private expense and embodies certain trade secrets and other confidential, proprietary, and
commercially-sensitive information that Telos safeguards through various measures implemented to maintain confidentiality
and prevent unauthorized use or disclosure.
Access to and use of Xacta is subject to the terms of a license agreement with Telos (a “License”) and is restricted to Authorized
Users of the Customer (the “Licensee”) that has been granted a License from Telos. “Authorized Users” means the employees,
consultants, contractors, agents, or other designees of the Licensee who are authorized by the Licensee to use Xacta in
accordance with the license granted by Telos and who have been supplied user login keys and credentials by the Licensee or
## Telos.
If  the Licensee of Xacta software solutions and/or documentation is the U.S. Government or an agency thereof, or anyone
licensing Xacta on behalf of the U.S Government, the following notice is applicable:
U.S. GOVERNMENT END USERS: Xacta software solutions and/or documentation delivered to U.S. Government end users
are “commercial computer software” and “restricted computer software” as these terms are used in applicable Federal
Acquisition Regulation (FAR) and Defense Federal Acquisition Regulation Supplement (DFARS) clauses, and agency-specific
supplemental regulations. As such, the use, duplication, disclosure, modification, and adaptation of the Xacta software
solutions and/or documentation, and rights in technical data, shall be subject to the terms and restrictions set forth in the
License applicable to the Xacta software solutions, and restrictions set forth in applicable FAR and DFARS clauses. See, e.g.,
FAR 12.211 (Technical Data), FAR 12.212 (Software), FAR 52-227-14 (Rights in Data-  General), FAR 52-227-19 (Commercial
Computer Software License), DFARS 252.227-7015 (Technical Data – Commercial Items), and DFARS 227.7202-3 (Rights in
Commercial Computer Software or Computer Software Documentation). No other rights are granted to the U.S.
## Government.
No Xacta user or other party may, without the express written permission of Telos or other rights owner, as applicable: 1)
reverse engineer or otherwise attempt to discover the source code, object code or underlying structure, ideas, know-how or
algorithms of Xacta; 2) copy, reproduce, distribute, publish, display, perform, modify, create derivative works, transmit, or in any
way exploit the content of Xacta; 3) distribute any part of Xacta content over any network, including a local area network, or sell
or offer it for sale, or; 4) use Xacta source code or content to construct any kind of database or to develop or enhance a
competing Governance, Risk and Compliance (GRC) solution. Furthermore, no user or other party may alter or remove any
copyright or other notice from Xacta or Xacta content.
Xacta is a registered trademark of Telos Corporation. All other registered trademarks and unregistered common law trademarks
that appear in Xacta content are the property of their respective holders.
This document is furnished for informational purposes only. The material presented in this document is believed to be accurate
at the time of release. However, Telos assumes no liability in connection with this document except as set forth in the License
under which the document is furnished.





Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 3 of 22
## Contents
Overview .............................................................................................................................................................................................................. 5
Xacta® JSON Data List .............................................................................................................................................................................. 6
cpus ......................................................................................................................................................................................................................... 7
osList ....................................................................................................................................................................................................................... 7
endpointData ................................................................................................................................................................................................... 9
cloudInfo ............................................................................................................................................................................................................ 10
testResults ......................................................................................................................................................................................................... 11
softwares ........................................................................................................................................................................................................... 13
drivelist ................................................................................................................................................................................................................ 14
netAdapters ..................................................................................................................................................................................................... 14
Sample Xacta® JSON Data Content .............................................................................................................................................. 16
Related Topics .............................................................................................................................................................................................. 22






Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 4 of 22

## Change History
## Version
## Number
Date of Last Revision Comments
1.0 04/25/2023 New document
2.0 04/16/2025 Updated cover page and copyright page







Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 5 of 22
## Overview
This article is applicable to the following:
Product License Type Release/Build
## Number
OS Database
Xacta.io  1.10 and higher

This article provides a list of data within in an Xacta® JSON file.  Xacta® JSON format provides significant
flexibility when working with structural datasets that can    transform your data in a variety of ways. This
allows users to import asset or vulnerability data into Xacta.io. For more on information on importing and
converting to Xacta® JSON, see the Importing Assets section of the Xacta.io User Guide and Converting to
Xacta® JSON Using Python.
An Xacta® JSON file contains information on multiple assets and their test results, operating systems, hardware, etc.
Please see screenshot below for sample Xacta® JSON file content; see also Sample Xacta JSON Content for another
Xacta® JSON file content sample.






Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 6 of 22


It is important to note that the contents of an Xacta® JSON file depends on the scanner tool used, where
the asset being scanned is hosted, and what the scanner tool has gathered. For example, cloudInfo data will
only be provided for any assets hosted in a cloud environment and will not be available for On-Premises
assets.
Users must also keep in mind that not all data in an Xacta® JSON file will be displayed or has an equivalent
Xacta.io field. Please refer to Xacta JSON Data List for more information on the content of an Xacta® JSON
file.
Xacta® JSON Data List
An Xacta® JSON file contains information, depending whether the assets come from a cloud environment
or has an anti-virus application.  Refer to the table below for the list of Xacta® JSON data and its description
and associated Xacta.io field.
Xacta® JSON Data Data Type Description Xacta.io Field
dataSource String
This refers to the
scanner tool providing
the data.

Note: If there are
testresults provided,
datasource is
required.

hostName String
This refers to the asset
identifier or the name
of the asset’s host.
Note that the value
must be unique within
the boundary.

Important: This is a
required value.
## Host Name
ramSize Integer  This refers to the RAM
size of the asset. This is
not required data.

scanDate String This refers to the date
when the scan was
executed by the tool.
## Last Updated
scannerVersion String  This refers to the
version or type of the
scanner tool.





Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 7 of 22
Xacta® JSON Data Data Type Description Xacta.io Field
systemName String This refers to the
accreditation
boundary where the
asset belongs. This is
not required data.
## System Name
cpus
Xacta® JSON Data Data Type Description Xacta.io Field
cpus Collection  This refers to CPU
information of the
scanned asset. This is
not a required value.
The succeeding rows
list the data typically
included in the cpus
## Collection.
Asset Info tab
model String This refers to the
model of the CPU.

clock String This refers to the clock
of the CPU.

biosManufacturer String This refers to the
manufacturer of the
asset. This is not
required data.

biosDate String This refers to how old
the asset could be.
This is not required
data.


osList
Xacta® JSON Data Data Type Description Xacta.io Field
osList Collection This refers to the
information on
operating system (OS)
or kernel of the asset.
This is not required
data. The succeeding
rows list the data
typically included in
the osList Collection.
OS Software tab
name  String This refers to the name
of operating system.
## Name
build String This refers to the build
of operating system.
## Build




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 8 of 22
Xacta® JSON Data Data Type Description Xacta.io Field
version String This refers to the
version of operating
system.
## Version
patch String This refers to the patch
of operating system.
## Patch
family String This refers to the
family of operating
system.

cpe String This refers to the CPE
of operating system.
## CPE
vendorInfo String This refers to the
vendor information of
hardware model. This
is not required data.
## Vendor
systemModel String This refers to the
information of
hardware model. This
is not required data.

serial String This refers to the serial
number of the
hardware. This is not
required data.

poc String
This refers to the point
of contact (POC) for
the host, if it is known.
This is not required
data.

Important: The email
address field uniquely
identifies a POC; each
unique email
introduced in the
Xacta  JSON will be
created as new POC
record.
## POC
name  String This refers to the name
of the asset’s POC.
Name under Asset Info
tab > Point of Contact
section
organization String This refers to the
organization of the
asset’s POC.
Organization under
Asset Info tab > Point
of Contact section
email String
This refers to the email
of the asset’s POC.

Note: If poc data is
Email under Asset Info
tab > Point of Contact
section




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 9 of 22
Xacta® JSON Data Data Type Description Xacta.io Field
provided, this is a
required data.
phone String This refers to the
phone of the asset’s
## POC.
Phone under Asset
Info tab > Point of
Contact section
location String This refers to the
location of the asset’s
## POC.
Location under Asset
Info tab > Point of
Contact section

endpointData
Xacta® JSON Data Data Type Description Xacta.io Field
endpointData Collection Used if there is AV
data collected. This is
not required data. This
is not required data.
The succeeding rows
list the data typically
included in the
endpoint Collection.

virusScanProductVersion String The refers to the
version of the anti-
virus scanner product.

virusScanPatchNum String This refers to the anti-
virus scanner product
patch number.

antiSpywareVersion String This refers to the anti-
Spyware tool’s version
number.

datVersion String This refers to the
version of the anti-
virus software’s DAT.
## Import Validation
Report > DAT
hipVersion String This refers to the
version of anti-virus
software’s HIP.
## Import Validation
Report > HIPS
hipPatchNum String This refers to the patch
number of HIP

hipStatus String This refers to the
status of HIP.

firewallStatus String This refers to the
status of the firewall.

lastScan String This refers to the date
when the anti-virus
tool completed the
scanning.

lastDefinitionDate String This refers to the date
when the virus





Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 10  of 22
Xacta® JSON Data Data Type Description Xacta.io Field
definition was last
updated.

cloudInfo
Xacta® JSON Data Data Type Description Xacta.io Field
cloudInfo Collection This is only displayed
when the scanned
asset is hosted in a
cloud environment.
Refer to the
succeeding rows
below under the
cloudInfo section for
the data that is
typically included in
the cloudinfo data
collection.

cloudResourceId String
This refers to the cloud
resource ID.

Note:   Assets must
have unique
cloudResourceID. In
instances where the
asset being imported
has the same
cloudResourceID with
an existing asset in
the Xacta.io
application, the
system will override
the existing asset with
the imported asset
with the same
cloudResourceID.
Resource ID
cloudType String This refers to the cloud
type.
## Type
cloudAccountId String This refers to the cloud
account ID.
Account ID
resourceName String This refers to the cloud
resource name.
## Resource Name
region String This refers to the cloud
region where the asset
belongs.
## Region




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 11  of 22
Xacta® JSON Data Data Type Description Xacta.io Field
resourceType String This refers to the cloud
resource type.

resourceData String
This refers to the cloud
resource data.

Note: Any valid JSON
object can be
provided for
resourceData. For
example:

“resourceData”: {
"anyField1":"sample
value",
"anyField2": true,
"anyField3": ["this",
## "is", "an", "array"]
## }


testResults
Xacta® JSON Data Data Type Description Xacta.io Field
testResults Collection This refers to the results
of the tests executed by
the scanner tool. This is
not a required value but
users may want to
leverage if there are test
results in the scan. This
is not required data. The
succeeding rows lists
the testResults
## Collection.

vendorID  String This refers to the unique
identifier of the test and
it is used to track
changes over time like
plugins. For testResults
data, this is required.
Vendor (ID)
testName String This refers to the
human-readable name
of test. For testResults
data, this is required.
Note that if only test
name is provided, the
isTestNameTestIdentifier
## Name




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 12 of 22
Xacta® JSON Data Data Type Description Xacta.io Field
data should be set to
True. Result is required.
notes String This refers to any
information or notes
provided by the tester.
This is not a required
data.

description String This refers to the
description of the test.
This is not a required
data.
## Test Details >
## Description
result String This refers to the result
of the test. This is
required.
Scan Result/Results
rawResult String This refers to the raw
result of the test.  The
data should be in
Xacta.io format: {"Pass",
"Fail", "N/A"}. This is not a
required data.
## Raw Result
contents Collection
This refers to mapping
information to any
regulation or content.
Note that a new array
should be created for
each content associated
with the test and should
be under the testResults
collection. This is not a
required data. This is not
required data. The
succeeding rows list the
data typically included
in the contents
## Collection.

Note: If content is
added, make sure that
values for name and
type should be provided.

name String
This refers to the
content text; e.g., CVE-
123-45677, AC-2.a, etc.

Note: If contents data is
provided, this is
required.
## Test Details >
## Controls




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 13 of 22
Xacta® JSON Data Data Type Description Xacta.io Field
type String
This refers to
information on where
the content goes in
Xacta.io and how it is
used in Xacta.io. For
example, {0:"CVE",
## 1:"CCE", 2:"CCI", 3:"V",
## 4:"CWE", 5:"IAC",
## 6:"ALERT", 7:"CPE"}.

Note: If contents data is
provided, this is
required.

port Integer This refers to the port of
the scanned asset.
## Test Data > Port
protocol String This refers to the
protocol. This is not a
required value.
## Test Data > Protocol
runTime String This refers to the date
and time the scan was
executed. This is not a
required value.
## Scan Date
scannedWithCredentialsFlag Boolean This indicates whether
the scanning was done
with credentials flag.
This is used for the scan
history report, and it  can
show quality of the scan.
This is not a required
data.
Cred/Scan
## Credentialing

softwares
Xacta® JSON Data Data Type Description Xacta.io Field
softwares Collection This populates
software inventory for
host, and will populate
data in Xacta 360. This
is not a required data.
The succeeding rows
list the data typically
included in the
softwares Collection.
## Asset Details >
## Hardware
name String
This refers to the
name of the software
in the asset.
## Model




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 14 of 22
Xacta® JSON Data Data Type Description Xacta.io Field

Note: If there is a
software data, this is a
required data.
version String This refers to the
version of the software
in the asset.

vendor String This refers to the
vendor of the software
in the asset.
## Vendor Info
cpe String This refers to the CPE
of the software in the
asset.
## CPE

drivelist
Xacta® JSON Data Data Type Description Xacta.io Field
driveList Collection This populates Drives
field in the Hardware
list of an asset. This is
not required. The
succeeding rows list
the data typically
included in the
driveList Collection.
## Drives
model String This refers to the
model of the hardware
drive.

sizeInMB Integer This refers to the size
of the drive or storage
in MB.


netAdapters
Xacta® JSON Data Data Type Description Xacta.io Field
netAdapters Collection This populates IP
address for host, and
will populate data in
Xacta 360. This is not
required. The
succeeding rows list
the data typically
included in the
## Net Adapters




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 15  of 22
Xacta® JSON Data Data Type Description Xacta.io Field
netAdapters
## Collection.
ipAddress String This refers to the IP
address of the net
adapter.
IP Address
macAddress String This refers to the MAC
address of the net
adapter.
MAC Address
dnsAddress String This refers to the DNS
address of the net
adapter.
## DNS







Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 16 of 22
Sample Xacta® JSON Data Content
Below is a sample Xacta® JSON Data file content that includes osList, testData, cloudInfo, and software
information:
## [
## {
"hostName": "testInstance2",
"dataSource": "Qualys",
"ramSize": 16021788,
"scanDate": 1425015828000,
"vendorInfo":"Vendor information of the Hardware ModelAAA",
## "cpus": [
## {
"model": "AMD Ryzen 5",
"clock": "3500Mhz"
## },
## {
"model": "Intel i7",
"clock": "3500Mhz"
## }
## ],
"osList": [
## {
"name": "Microsoft Windows 7 Enterprise",
"family": "WINDOWS"
## }
## ],
"testResults": [
## {
"vendorId": "V-  1",
"testName": "RHEL 8-test1",
"notes": "Notes 1",
"description": "Description 1",

"rawResult": "Pass",
## }
## ],
## "contents": [
## {
"name": "CCI-000015",
"type": "CCI"
## },
## {
"name": "CCI-000054",
"type": "CCI"
## },




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 17  of 22
## {
"name": "CCI-001814",
"type": "CCI"
## },
## {
"name": "AC-   17"  ,
"type": "IAC"
## },
## {
"name": "AC-   6 (9)",
"type": "IAC"
## },
## {
"name": "CCI-000015",
"type": "CCI"
## },
## {
"name": "CCI-000054",
"type": "CCI"
## },
## {
"name": "CCI-001453",
"type": "CCI"
## },
## {
"name": "AC-   17 (1)",
"type": "IAC"
## },
## {
"name": "CCI-000139",
"type": "CCI"
## }
## ],
"riskFactor": "High",
"scannedWithCredentialsFlag": true
## },
## {
"vendorId": "V-  2",
"testName": "RHEL 8-test2",
"notes": "Notes 2",
"description": "Description 2",

"rawResult": "N/A",
## }
## ],
## "contents": [
## {
"name": "AC-   3",




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 18 of 22
"type": "IAC"
## },
## {
"name": "CM-   6 b",
"type": "IAC"
## },
## {
"name": "CM-   6 b",
"type": "IAC"
## },
## {
"name": "CM-   6 b",
"type": "IAC"
## },
## {
"name": "CCI-000068",
"type": "CCI"
## },
## {
"name": "AC-   17 (2)",
"type": "IAC"
## },
## {
"name": "AC-   3",
"type": "IAC"
## },
## {
"name": "CCI-000054",
"type": "CCI"
## },
## {
"name": "AC-   17 (2)",
"type": "IAC"
## },
## {
"name": "AU-   5 a",
"type": "IAC"
## }
## ],
"scannedWithCredentialsFlag": true
## },

## {
"vendorId": "V-  500",
"testName": "RHEL 8-test500",
"notes": "Notes 500",
"description": "Description 500",

"rawResult": "Pass",




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 19 of 22
## }
## ],
## "contents": [
## {
"name": "AC-   3",
"type": "IAC"
## },
## {
"name": "CCI-001814",
"type": "CCI"
## },
## {
"name": "AC-   17 (2)",
"type": "IAC"
## },
## {
"name": "CCI-000015",
"type": "CCI"
## },
## {
"name": "CCI-001814",
"type": "CCI"
## },
## {
"name": "CCI-001453",
"type": "CCI"
## },
## {
"name": "CCI-000015",
"type": "CCI"
## },
## {
"name": "AU-   5 a",
"type": "IAC"
## },
## {
"name": "AC-   2 (1)",
"type": "IAC"
## },
## {
"name": "CCI-001453",
"type": "CCI"
## }
## ],
"scannedWithCredentialsFlag": true
## }
## ],
## "softwares": [
## {




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 20 of 22
"name": "Internet Explorer",
"vendor": "Microsoft",
## "version": "11",
## "cpe": "cpe:2.3:a:microsoft:internet_explorer:11:-:*:*:*:*:*:*"
## },
## {
"name": "Dolby Audio X2 (DAX2)",
"vendor": "Dolby",
## "version": "1.3",
## "cpe": "cpe:/a:dolby:dolby_audio_x2:1.3"
## },
## {
## "name": "openssl",
## "vendor": "openssl",
## "version": "3.1",
## "cpe": "cpe:/a:openssl:openssl"
## },
## {
"name": "Internet Explorer",
"vendor": "Microsoft",
## "version": "11",
## "cpe": "cpe:2.3:a:microsoft:internet_explorer:11:-:*:*:*:*:*:*"
## },
## {
"name": "Dolibarr ERP CRM",
"vendor": "Dolibarr",
## "version": "2.7.0",
## "cpe": "cpe:/a:dolibarr:dolibarr:2.7.0"
## },
## {
"name": "Dolibarr ERP CRM",
"vendor": "Dolibarr",
## "version": "2.7.0",
## "cpe": "cpe:/a:dolibarr:dolibarr:2.7.0"
## },
## {
"name": "Dolibarr ERP CRM",
"vendor": "Dolibarr",
## "version": "2.7.0",
## "cpe": "cpe:/a:dolibarr:dolibarr:2.7.0"
## },
## {
"name": "Python",
"vendor": "Python",
## "version": "3.8",
## "cpe": "cpe:2.3:a:python:python:3.10.3:*:*:*:*:*:*:*"
## },
## {
"name": "Fortinet FortiOS",




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 21 of 22
"vendor": "Fortinet",
## "version": "4.1.4",
## "cpe": "cpe:/o:fortinet:fortios:4.1.4"
## },
## {
## "name": "openssl",
## "vendor": "openssl",
## "version": "3.1",
## "cpe": "cpe:/a:openssl:openssl"
## }
## ],
"netAdapters": [
## {
"ipAddress": "250.13.208.239",
"macAddress": "0a:69:ac:94:fa:4c",
"dnsAddress": "ip-   250.13.208.239.internal"
## },
## {
"ipAddress": "84.80.74.89",
"macAddress": "0a:69:ac:d0:c5:a4",
"dnsAddress": "ip-   84.80.74.89.internal"
## },
## {
"ipAddress": "34.42.103.14",
"macAddress": "0a:69:ac:a4:62:f8"
## },
## {
"ipAddress": "188.41.109.21",
"macAddress": "0a:69:ac:66:ba:9c"
## }
## ],
"biosManufacturer": "AMI",
"biosDate": "2020",
"biosVersion": "1.42",
"systemModel": "Latitude E6400",
"serial": "1234578ULdRdrDe",
"scannerVersion": "3",
"systemName": "Cloud Service Provider Vulnerability Management (API)",
"driveList": [
## {
"model": "Buffalo",
"sizeInMB": 2000
## },
## {
"model": "Buffalo",
"sizeInMB": 2000
## }
## ],
## "poc": {




Telos Corporation | 19886 Ashburn Road, Ashburn, Virginia, USA 20147-2358 | 1.800.70.TELOS | 1.800.708.3567 | www.telos.com

Xacta.io JSON Data Dictionary | April 2025  PROPRIETARY INFORMATION
© 2025 Telos Corporation.  All rights reserved.  Page 22 of 22
"name": "James Brown",
"organization": "Company",
## "email": "james.brown@company.com",
## "phone": "58887345",
"title": "Mr.",
"location": "Frizz VA"
## },
"cloudInfo": {
"cloudresourceId": "i-1234567890abcdef0",
"cloudType": 0,
"cloudAccountId": "0662773",
"region": "us-   east-1",
"resourceType": "ec2-instance",
"resourceData": {
"amiId": "ami-12345",
"instanceId": "12345",
"instanceType": "mid",
"hostnameLocal": "hostnamelocal",
"hostnamePublic": "hostnamePUblic",
"ipLocal": "1.1.1.1",
"ipPublic": "8.8.8.8"
## },
"resourceName": "ec2-IPaddress-1.2.3.4"
## }

## }
## ]
## Related Topics
## • Xacta.io User Guide
- Xacta.io API Guide
- Converting to Xacta® JSON Data Using Python