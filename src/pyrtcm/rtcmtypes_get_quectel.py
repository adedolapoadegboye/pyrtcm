"""
RTCM Protocol Quectel proprietary payload definitions

Created on 29 Jan 2025

:author: semuadmin
:copyright: SEMU Consulting © 2022
:license: BSD 3-Clause
"""

# from pyrtcm.rtcmtypes_core import NHARMCOEFFC, NHARMCOEFFS

# *************************************************************
# RTCM3 Quectel Proprietary PAYLOAD DEFINITIONS
# *************************************************************
Q999_001 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 1 for RSS
    "DF004": "GPS Epoch Time (TOW)",
    "DF18P": "GPS Extended Week Number",
    "DF054": "Leap Seconds, GPS-UTC",
    "DF_Safety": "Safety Information (0 = Not available, 1 = Available)",
    "DF_ProtocolVersion": "Protocol Version Flags (RTCM 3.3 = 3)",
    "DF19P": "Firmware Version",
    "Reserved1": "Reserved (8 bits)",
    "Reserved2": "Reserved (8 bits)",
    "Reserved3": "Reserved (8 bits)",
    "DF01P": "Timing/PPS Status",
    "DF87P": "Time Validity",
    "DF21P": "Constellation Alarm Mask",
    "Reserved4": "Reserved (32 bits)",
    "DF95P": "GNSS Constellation Mask",
    "DF96P": "GNSS Multi-Frequency Constellation Mask",
    "NCO_ClockDrift": "NCO Clock Drift (0.0001 Hz, signed int, present if protocol version flag is 2 or 3)",
    "DF113P": "Time Best Satellite Type (present if protocol version flag is 3)",
    "DF95P_2": "Unavailable Satellite Type Mask (present if protocol version flag is 3 or above)",
}

Q999_002 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 2 for RCC
    "DF53P": "Response ID (Always 0x0000 for output)",
    "DF112P": "Config. Block (1 = RAM, 2 = Default, 3 = NVM stored configuration)",
    "DF25P": "Config. Page Number",
    "DF49P": "Continue on Next Message (0 = End, 1 = Continue)",
    "DF50P": "CDB Write Flag (0 = No, 1 = CDB Write for input only)",
    "DF26P": "Config. Page Mask (1-bit per page, N = Number of lines to be written)",
    "DF27P": "Config. Word (32*N, up to 16 words)",
}

Q999_004 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 4 for PVT
    "DF003": "Reference Station ID (0x3FF = Invalid)",
    "DF021": "ITRF Realization Year (Reserved)",
    "DF28P": "GPS Quality Indicator (0 = Invalid, 1 = SPS Mode, 2 = DGPS Mode)",
    "DF29P": "Number of Satellites in Use (0xFF = Invalid)",
    "DF37P": "Number of Satellites in View (0xFF = Invalid)",
    "DF30P_HDOP": "Horizontal Dilution of Precision (HDOP)",
    "DF30P_VDOP": "Vertical Dilution of Precision (VDOP)",
    "DF30P_PDOP": "Position Dilution of Precision (PDOP)",
    "DF31P": "Geoidal Separation (0x4000 = Invalid)",
    "DF32P": "Age of Differentials (0xFFFFFF = Invalid)",
    "DF33P": "Differential Reference Station ID (0x3FF = Invalid)",
    "DF72P": "Time ID (0xF = Invalid)",
    "DF16P": "GNSS Epoch Time (1 ms resolution, 0x3FFFFFFF = Invalid)",
    "DF18P": "Extended Week Number",
    "DF054": "Leap Seconds, GPS-UTC",
    "DF025": "Antenna Position ECEF-X",
    "DF026": "Antenna Position ECEF-Y",
    "DF027": "Antenna Position ECEF-Z",
    "DF34P": "Antenna Velocity ECEF-X",
    "DF35P": "Antenna Velocity ECEF-Y",
    "DF36P": "Antenna Velocity ECEF-Z",
}

Q999_005 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 5 for POSQM
    "Info": "Quectel internal debugging data (format unspecified)",
}

Q999_019 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 19 for Response Message
    "DF53P": "Response ID (identifies the input message that requested a response)",
    "DF54P": "Message Response (Response to the input message)",
}

Q999_021 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 21 for EPVT
    "DF003": "Reference Station ID (0x3FF = Invalid)",
    "DF021": "ITRF Realization Year (Reserved)",
    "DF28P": "GPS Quality Indicator (0 = Invalid, 1 = SPS Mode, 2 = DGPS Mode)",
    "DataStatus": "Data Status (0 = Valid, 1 = Navigation receiver warning)",
    "FixFrequencyMode": "Fix Frequency Mode (0 = Single frequency, 1 = Multi-frequency)",
    "FixIntegrityRAIM": "Fix Integrity RAIM (0 = Not checked, 1 = Checked)",
    "DF29P": "Number of Satellites in Use (0xFF = Invalid)",
    "DF37P": "Number of Satellites in View (0xFF = Invalid)",
    "DF30P_HDOP": "Horizontal Dilution of Precision (HDOP)",
    "DF30P_VDOP": "Vertical Dilution of Precision (VDOP)",
    "DF30P_PDOP": "Position Dilution of Precision (PDOP)",
    "DF31P": "Geoidal Separation (0x4000 = Invalid)",
    "DF32P": "Age of Differentials (0xFFFFFF = Invalid)",
    "DF33P": "Differential Reference Station ID (0x3FF = Invalid)",
    "DF72P": "Time ID (0xF = Invalid)",
    "DF87P": "Time Validity",
    "DF16P": "GNSS Epoch Time (1 ms resolution, 0x3FFFFFFF = Invalid)",
    "DF18P": "Extended Week Number",
    "DF054": "Leap Seconds, GPS-UTC",
    "DF73P": "Latitude (0x80000000 = Invalid)",
    "DF74P": "Longitude (0x80000000 = Invalid)",
    "DF75P": "Height (0x80000 = Invalid or not available in 2D fix)",
    "DF76P": "Velocity Horizontal (0x80000 = Invalid)",
    "DF77P": "Velocity Vertical (0x80000 = Invalid)",
    "DF78P": "Course Angle (0x8000 = Invalid)",
    "ProtectionLevelHorizontal": "Protection Level Horizontal (0.01 m resolution, 0xFFFF = Invalid)",
    "ProtectionLevelVertical": "Protection Level Vertical (0.01 m resolution, 0xFFFF = Invalid)",
    "ProtectionLevelAngle": "Protection Level Angle (0.01 degree resolution, 0xFFFF = Invalid)",
    "ReceiverClockBias": "Receiver Clock Bias (Unit: mm, 0x80000000 = Invalid)",
    "ReceiverClockDrift": "Receiver Clock Drift (Unit: cm/s, 0x80000000 = Invalid)",
}

Q999_024 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 24 for RFS
    "Info": "Quectel internal debugging data (format unspecified)",
}

Q999_025 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 25 for FWVER
    "FirmwareVersionDataLength": "Firmware Version Data Length (N bytes)",
    "FirmwareVersionDataString": "Firmware Version Data String (char*8*N, depends on length)",
}

Q999_026 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 26 for SIGQM2
    "Info": "Quectel internal debugging data (format unspecified)",
}

Q999_064 = {
    "DF002": "RTCM Message Number",  # Always 999 for proprietary messages
    "DF02P": "Subtype ID",  # 64 for SENS
    "NumFrameEntries": "Number of Frame Entries (Defines how many sensor data fields follow)",
    "FrameEntries": (  # Repeating sensor frame entries based on sensor type
        "NumFrameEntries",
        {
            "DF71P": "Sensor Type (0x00 = Common, 0x03 = Odometer, 0x1E = Accelerometer, 0x1F = Gyroscope)",
            "DF64P": "CPU Timestamp (977.5171 ns per step)",
            "SensorSpecific": (
                "DF71P",
                {
                    "0x00": {  # Sensor Common Frame
                        "SensorTypeLength": "Sensor Type Length (4-bit per step, 8 steps total)",
                        "SensorCommonVersion": "Sensor Common Version (0 = Version 0, 1-3 = RFU)",
                        "DF004": "GPS Epoch Time (TOW, best time converted to GPS system time)",
                    },
                    "0x03": {  # Odometer - Reverse Frame
                        "DF106P": "Odometer Count (Unsigned, represents distance traveled)",
                        "DF107P": "Reverse Status (0 = Forward, 1 = Reverse)",
                    },
                    "0x1E": {  # Accelerometer Frame
                        "DF65P": "Acc Raw X (Raw X-axis acceleration, ±2 g full scale)",
                        "DF66P": "Acc Raw Y (Raw Y-axis acceleration, ±2 g full scale)",
                        "DF67P": "Acc Raw Z (Raw Z-axis acceleration, ±2 g full scale)",
                    },
                    "0x1F": {  # Gyroscope Frame
                        "DF68P": "Gyro Raw X (Raw X-axis angular rate, ±125 dps full scale)",
                        "DF69P": "Gyro Raw Y (Raw Y-axis angular rate, ±125 dps full scale)",
                        "DF70P": "Gyro Raw Z (Raw Z-axis angular rate, ±125 dps full scale)",
                    },
                },
            ),
        },
    ),
}


# *************************************************************
# RTCM3 IGS MESSAGE PAYLOAD DEFINITIONS
# *************************************************************
RTCM_PAYLOADS_GET_Q999 = {
    "Q999_001": {**Q999_001},
    "Q999_002": {**Q999_002},
    "Q999_004": {**Q999_004},
    "Q999_005": {**Q999_005},
    "Q999_019": {**Q999_019},
    "Q999_021": {**Q999_021},
    "Q999_024": {**Q999_024},
    "Q999_025": {**Q999_025},
    "Q999_026": {**Q999_026},
    "Q999_064": {**Q999_064},
}
