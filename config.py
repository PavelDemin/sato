#write_url = 'http://admin:admin@172.16.90.67/printer_config_write.html'
#read_url = 'http://admin:admin@172.16.90.67/printer_config_read.html'
advanced_mode_url = 'http://admin:admin@172.16.90.67/advanced_mode.html'
url_advanced_mode_cgi = 'http://admin:admin@172.16.90.67/advanced_mode.cgi'
url_restart_cgi = 'http://admin:admin@172.16.90.67/restart.cgi'
#restart_url = 'http://admin:admin@172.16.90.67/restart.html'
#dispenser_conf = 'dispenser.txt'
#continuous_conf = 'continuous.txt'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}



data = {
    'AutoOnine': '1',
    'BackfeedMotionDispensor': '0',
    'CalenderCaseFormat': '1',
    'CalenderCheck': '0',
    'CalenderDay': '11',
    'CalenderDayOfWeekCodeFriday': '6',
    'CalenderDayOfWeekCodeMonday': '2',
    'CalenderDayOfWeekCodeSaturday': '7',
    'CalenderDayOfWeekCodeSunday': '1',
    'CalenderDayOfWeekCodeThursday': '5',
    'CalenderDayOfWeekCodeTuesday': '3',
    'CalenderDayOfWeekCodeWednesday': '4',
    'CalenderHour': '06',
    'CalenderMIn': '50',
    'CalenderMont': '12',
    'CalenderMonthCodeApril': '3',
    'CalenderMonthCodeAugust': '7',
    'CalenderMonthCodeDecember': '12',
    'CalenderMonthCodeFebruary': '1',
    'CalenderMonthCodeJanuary': '0',
    'CalenderMonthCodeJuly': '6',
    'CalenderMonthCodeJune': '5',
    'CalenderMonthCodeMarch': '2',
    'CalenderMonthCodeMay': '4',
    'CalenderMonthCodeNomenber': '11',
    'CalenderMonthCodeOctober': '10',
    'CalenderMonthCodeSeptember': '9',
    'CalenderYear': '19',
    'CharacterPitch': '1',
    'CommandError': '0',
    'ContinuousPrint': '1',
    'EnhancedReprint': '0',
    'ErrorIndication': '0',
    'ExternalReprint': '0',
    'ExternalSignal': '0',
    'ExternalSignalType': '3',
    'HeadCheckMode': '0',
    'HeadCheckPageNo': '000001',
    'HeadDotDensity': '2',
    'HeadcheckEnableDisable': '0',
    'HeadcheckNormalBarcode': '0',
    'IgnoreA1': '0',
    'InputSignalDispenseIn': '2',
    'InputSignalFeed': '2',
    'InputSignalLabelNear': '1',
    'InputSignalPrintStasrt': '1',
    'InputSignalReprint': '0',
    'JobModification': '0',
    'LabelSizeAdjHight': '01080',
    'LabelSizeAdjWidth': '1248',
    'LcdPowerSaving': '00',
    'LedIndication': '1',
    'ModeSelect': '0',
    'OutputSignalHomePos': '1',
    'OutputSignalMachineErr': '1',
    'OutputSignalOnline': '3',
    'OutputSignalPaperEnd': '5',
    'OutputSignalPrintEnd': '1',
    'OutputSignalRibbonEnd': '4',
    'OutputSignalRobbonNear': '6',
    'PitchSensorContinuous': '1',
    'PrintMethod': '1',
    'PrintOffsetH': '0000',
    'PrintOffsetV': '0000',
    'PrinterType': '1',
    'ProtocolCode': '0',
    'RibbonSaver': '0',
    'RotateLabel': '2',
    'SaverFeed': '0',
    'SensorTypeDispenser': '1',
    'ZeroSlash': '0'
}

data_list = ['AutoOnine',
'BackfeedMotionDispensor',
'CalenderCaseFormat',
'CalenderCheck',
'CalenderDay',
'CalenderDayOfWeekCodeFriday',
'CalenderDayOfWeekCodeMonday',
'CalenderDayOfWeekCodeSaturday',
'CalenderDayOfWeekCodeSunday',
'CalenderDayOfWeekCodeThursday',
'CalenderDayOfWeekCodeTuesday',
'CalenderDayOfWeekCodeWednesday',
'CalenderHour',
'CalenderMIn',
'CalenderMont',
'CalenderMonthCodeApril',
'CalenderMonthCodeAugust',
'CalenderMonthCodeDecember',
'CalenderMonthCodeFebruary',
'CalenderMonthCodeJanuary',
'CalenderMonthCodeJuly',
'CalenderMonthCodeJune',
'CalenderMonthCodeMarch',
'CalenderMonthCodeMay',
'CalenderMonthCodeNomenber',
'CalenderMonthCodeOctober',
'CalenderMonthCodeSeptember',
'CalenderYear',
'CharacterPitch',
'CommandError',
'ContinuousPrint',
'EnhancedReprint',
'ErrorIndication',
'ExternalReprint',
'ExternalSignal',
'ExternalSignalType',
'HeadCheckMode',
'HeadCheckPageNo',
'HeadDotDensity',
'HeadcheckEnableDisable',
'HeadcheckNormalBarcode',
'IgnoreA1',
'InputSignalDispenseIn',
'InputSignalFeed',
'InputSignalLabelNear',
'InputSignalPrintStasrt',
'InputSignalReprint',
'JobModification',
'LabelSizeAdjHight',
'LabelSizeAdjWidth',
'LcdPowerSaving',
'LedIndication',
'ModeSelect',
'OutputSignalHomePos',
'OutputSignalMachineErr',
'OutputSignalOnline',
'OutputSignalPaperEnd',
'OutputSignalPrintEnd',
'OutputSignalRibbonEnd',
'OutputSignalRobbonNear',
'PitchSensorContinuous',
'PrintMethod',
'PrintOffsetH',
'PrintOffsetV',
'PrinterType',
'ProtocolCode',
'RibbonSaver',
'RotateLabel',
'SaverFeed',
'SensorTypeDispenser',
'ZeroSlash']

param_continuous_mode = {
    'AutoOnine': '0',
    'ExternalSignal': '0',
    'PrinterType': '1'
}

param_dispenser_mode = {
    'AutoOnine': '1',
    'ExternalSignal': '1',
    'PrinterType': '0'
}