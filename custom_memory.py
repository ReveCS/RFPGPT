def custom_memory(memory): 
# VIRGIN GALACTIC RESPONSES (ALL)

#     memory.save_context({"input": "Respond to Section 1.2 \"RMC Overview\" of the document RFP-KV-101422-RMC-NAI."},
#                         {"output": """As a program manager at NAI, my response to Section 1.2 \"RMC Overview\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: * Title:RMC Overview
#         * Noted/understood, per RFP:
#         Any Quote/Proposal submitted to GALACTIC CO in response to this RFP shall constitute a binding 
#         offer from Supplier to contract with GALACTIC CO according to the proposal's terms for a period of 
#         ninety (90) days after its date of submission.
#         Agreed."""})
    
#     memory.save_context({"input": "Respond to Section 2.1 \"Binding Offer\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 2.1 \"Binding Offer\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: * Title: Binding Offer
#         * Noted/understood, per RFP:
#         Any Quote/Proposal submitted to GALACTIC CO in response to this RFP shall constitute a binding 
#         offer from Supplier to contract with GALACTIC CO according to the proposal's terms for a period of 
#         ninety (90) days after its date of submission.
#         Agreed."""})
    
#     memory.save_context({"input": "Respond to Section 2.2 \"Terms and Conditions\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 2.2 \"Terms and Conditions\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: * Title: Terms and Conditions
#         * Noted, per RFP:
#         The Terms and Conditions that will apply to any procurement issued due to this solicitation are 
#         GALACTIC, CO. STANDARD TERMS AND CONDITIONS OF PURCHASE February 2022 
#         VERSION, or mutually agreed upon modified terms and conditions.
#         Exception: Standard NAI Terms and Conditions per NAI Schedule A will apply (provided with this 
#         submission)."""})
    
#     memory.save_context({"input": "Respond to Section 2.3 \"Quality Assurance\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 2.3 \"Quality Assurance\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: * Title: Quality Assurance
#         * Noted, per RFP:
#         The quality assurance requirements which will apply to any procurement issued as a result of this solicitation
#         [See attachment Schedule A]."""})
    
#     memory.save_context({"input": "Respond to Section 2.4 \"Payment Terms\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 2.4 \"Payment Terms\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: * Title: Payment Terms
#         * Noted, per RFP:Noted/understood, per RFP:
#         Virgin Galactic standard payment terms of Net 90.
#         Agreed"""})

#     memory.save_context({"input": "Respond to Section 3 \"TECHNICAL REQUIREMENTS\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3 \"TECHNICAL REQUIREMENTS\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: TECHNICAL REQUIREMENTS
#     * NAI’s RFP reply solution is to offer a NAI COTS configured SIU34 for the RMC. The SIU34 can support up to four 3U OpenVPX SBC and Multifunction I/O & Communications boards and one 3U 
# 	VITA 62 PSU slot. To meet or exceed the minimal threshold and in most cases the objective technical requirements of the RFP, the NAI SIU34-97864 will be comprised/fitted with the following 
# 	common boards and components:
# 	SIU34-97864
# 	SIU34 = 4x3U VPX slot, 12 Functions
# 	Configured With:
# 	Slot 1 = 68ARM2-2-SC3CB3DT11140WH4A05 3U OpenVPX, SBC, Xilinx Zynq UltraScale+
# 	Configured With:
# 	SC3 = 8 Channels (max) RS-232/422/485 Serial Comms or GPIO, Programmable, Non-isolated
# 	CB3 = 8 Channels CANBus, CAN 2.0 A/B (CB1) or J1939 (CB2) protocol layer, programmable
# 	DT1 = 24 Channels Discrete I/O, 0-60 VDC Input/Output, Max Iout 500 mA - 2 A, Source/Sink (out)
# 	1 = Dual-core Arm® Cortex®-A53 MPCore @ 1.3 GHz / Root Complex / 6 x1 PCIe
# 	1 = 8 GB (w/ECC)
# 	4 = 32 GB SATA NAND Flash
# 	0 = No IPMC Function Option (default/reserved)
# 	W = Conduction Cooled with Wedgelocks (Rear I/O Only)
# 	H = -40°C to +85°C with Conformal Coating
# 	4 = MB Port A (10/100/1000Base-T) & Port B (10/100/1000Base-T) To Rear
# 	A = Deos 653
# 	0 = No Enhanced Security Support
# 	5 = MOD3-24 I/O, USB, TTL 1-8
# 	Slot 2 = 68G5-2-ADFRT1RT1WH050 3U OpenVPX I/O and Communications Board
# 	Configured With:
# 	ADF = 16 Channels A/D, ±100 V, Individual 16-bit SAR, 200 kHz max., Simultaneous Sampling
# 	RT1 = 8 Channels Resistance Temperature Detectors (RTD), 2, 3, or 4 wire, 16 Bit Res, 16.7 Hz/Ch
# 	RT1 or DA5? = 8 Channels Resistance Temperature Detectors (RTD), 2, 3, or 4 wire, 16 Bit Res, 
# 	16.7 Hz/Ch (2 x DA5 (see below) is in lieu of a 2nd SW1 module on the 68SR1 board) 2nd RT1 would 
# 	be removed/replaced with DA5.
# 	W = Conduction Cooled with Wedgelocks (Rear I/O Only)
# 	H = -40°C to +85°C with Conformal Coating
# 	0 = No Ethernet
# 	5 = PCIe
# 	0 = No IPMC Function Option (default/reserved)
# 	Slot 3 = 68G5-2-DA3PS2TBDWH050 3U OpenVPX I/O and Communications Board
# 	Configured With:
# 	DA3 = 4 Channels D/A, ±40 V, ±100 mA, Voltage or Current Output
# 	PS2 = 1x 10V & 1x 20V low-noise DC Excitation
#     """})

#     memory.save_context({"input": "Respond to Section 3.1 \"Software\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.1 \"Software\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Software
# 	* As defined within the RFP,
# The primary function of the RMC is to interface with the sensors and controls of the Rocket Motor 
# System. VG requests vendors to include a description of software that will be provided with the 
# proposed RMC, including the operating system, board support package/drivers, libraries, and API 
# definitions.
# Previous correspondences and communications with VG have identified two possible basic RMC
# communications & data routing solutions that can be realized with the hardware/software
# configuration, as proposed.
# 1. Remote Interface Unit (RIU)
# Defined as the RMC hosting the NAI provided Ethernet Server/Listener application running 
# on the main 68ARM2 SBC; which supports the NAI GEN 5 Ethernet Protocol.
# 2. Embedded Customer Application 
# Defined as the RMC hosting a Virgin Galactic developed embedded software application
# running on the main 68ARM2 SBC; can fully control any of the other potential Avionics Data 
# Bus(es), i.e. CAN 2.0 or J1939, ARINC 429 or Serial (RS-422/485/232) communications 
# interfaces.
# However, based on the recurring and highlighted requirements discussions to demonstrate 
# compliance to DO-178C/254 DAL A, or equivalent, probability of failure per flight hour as defined in 
# ARP-4761 and Ethernet as the primary command/control and data interface being nondeterministic
# and ultimately uncertifiable, the RIU application solution may not be a valid solution choice.
# Therefore, a customer Embedded Software Application running and built-on the DDC-I Deos real 
# time and certifiable operating system is suggested.
# Unless otherwise stipulated or discussed for further detailing, the operating system on the 68ARM2 
# will be DDC-I Deos.
# DDC-I’s Deos is a space and time partitioning safety-critical avionics RTOS and supports and is 
# compliant to ARINC 653 requirements. Application software can be processed in appropriate 
# separate partitions. In order to decouple the real-time operating system platform from the application 
# software, ARINC 653 defines an API called APplication EXecutive (APEX). Each application 
# software is called a partition and has its own memory space. It also has a dedicated time slot allocated 
# by the APEX API. Within each partition, multitasking is allowed. The APEX API provides services 
# to manage partitions, processes and timing, as well as partition/process communication and error 
# handling. The partitioning environment can be implemented by using a hypervisor to map partitions 
# to virtual machines, but this is not required.
# NAI recommends that customers interested with Deos get training from DDC-I if new to integrating 
# on/with real time OS time, space & resource partitioning with ARINC 653 and/or Rate Monotonic 
# Analysis (RMA) scheduling. 
# All operational, configuration and initialization functions and I/O is accessed, commanded and 
# controlled via memory mapped register address space. The hardware is supported with the NAI 
# Software Support Kit (SSK), which is included as part of the overall system configuration data 
# support package, which contains the APIs/libraries, help files, source code and example/sample code 
# for the individual functions as well as the general use motherboard memory function access."""})
    
#     memory.save_context({"input": "Respond to Section 3.2 \"Hardware I/O\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.2 \"Hardware I/O\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Hardware I/O
# 	* The Rocket Motor Controller will support the following types of I/O:
# 1) Analog Input (1x ADF)
# 2) Analog Output (1x DA3)
# 3) Excitation Outputs (1x PS2)
# 4) Digital I/O (1x DT1)
# 5) Resistance Temperature Detector (RTD) Inputs (2x RT1)
# 6) Digital Outputs (5A) (1x 68SR1: 1x SW1)
# 7) Current Output (pulse)(O) (from 68SR1: 1x SW1) or, (2 x DA5) lose an RT1 above.
# Additionally, for completeness, the following communications I/O: 
# 8) CAN Bus controllers (O) (1x CB3)
# 2) Gigabit Ethernet interfaces (T) (provided from 68ARM2 motherboard)
# 3) Serial Communication (1x SC3)
# 4) USB 2.0 (T) or higher (O). (provided from 68ARM2 motherboard)"""})
    
#     memory.save_context({"input": "Respond to Section 3.2.1 \"Analog Inputs (ADF)\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.2.1 \"Analog Inputs (ADF)\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Analog Inputs (ADF)
# 	* To meet the requirements for the Analog Inputs as detailed in the RFP:
# The RMC will acquire data from sensors outputting analog voltages in a usable form.
# The specification for the analog inputs of the RMC are as follows:
# 1) There SHALL be a minimum of 16 analog inputs channels.
# 2) The analog inputs SHALL be differential inputs (DIFF).
# 3) The analog inputs SHALL have an acquisition resolution of 16 bits or higher, with accuracy 
# of at least 2% RSS (Root of the Sum of the Squares) FSO (Full Scale Output).
# 4) The analog inputs SHALL have a minimum hardware sample rate of 32 Ks/s.
# 5) The analog inputs SHALL have at least 1 channel with a range of 0-40VDC, at least 1 
# channel with a range of 0-10VDC and at least 14 channels with a range of at least 0-5VDC.
# NAI will provide the ADF Analog Input function module.
# Analog-to-Digital module ADF is a 16-Channel A/D module that features independent 16-bit 
# Successive Approximation Register (SAR) A/D converters with programmable full-scale range input 
# of ±100V (programmable to ±6.25V for greater LSB resolution). The A/D converters also have 
# programmable sample rates of up to 200 kHz.
# Features
# • The input range and polarity is field programmable for each channel. The ability to set lower 
# expected, full-scale voltage gain ranges assures the use of the maximum resolution.
# • Each channel includes a fixed, second-order, anti-aliasing input filter and a digital, secondorder IIR 
# • Low-pass output filter with a programmable break frequency that enables users to field-adjust 
# the filtering for each channel.
# • All channels have continuous background Built-In-Test (BIT).
# The modules also include extended A/D FIFO buffering capabilities for greater storage/management 
# of the incoming signal samples (data) for post processing applications. Programmable FIFO buffer 
# thresholds maximize data flow control (in and out of the FIFO). Incremental relative time-stamping 
# between samples is also provided as a programmable option."""})
    
#     memory.save_context({"input": "Respond to Section 3.2.2 \"Analog Outputs (DA3)\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.2.1 \"Analog Outputs (DA3)\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Analog Outputs (DA3)
# 	* To meet the requirements for the Analog Inputs as detailed in the RFP:
# The RMC will output voltages to devices that require voltage control. The specification for the analog 
# outputs of the RMC are as follows:
# 1) There SHALL be a minimum of 1 analog output channel with range of at least 0-10VDC that can 
# source at least 100mA of current.
# 2) The analog output SHALL have an output resolution of 16 bits or higher, with accuracy of at least 
# 2% RSS (Root of the Sum of the Squares) FSO (Full Scale Output).
# NAI will provide the DA3 Analog Input function module.
# The Digital-to-Analog (D/A) module DA3 provides 4 independent D/A output channels with a fullscale range ±40 VDC (V-control mode) and ±100 mA (I-control mode). Linearity/accuracy is ±0.10% 
# FS range over temperature. The DA3 provides either voltage or current control loop modes, which are 
# programmable for the application.
# The DA3 module includes extensive Background Built-in-Test (BIT). In addition to output signal 
# read-back (wrap) capabilities, overloaded outputs are detected with automatic channel shut-down 
# protection, and the results are displayed in a status word. DA3 also include D/A FIFO buffering for 
# greater control of the output voltage and signal data. Once enabled and triggered, the D/A FIFO 
# buffer accepts, stores, and outputs the voltage (and/or current) commands for applications requiring 
# simulation of waveform generation (single or periodic). The output data command word is formatted 
# as a percentage of the Full Scale (FS) range selection, which allows maximum resolution and 
# accuracy at lower voltage ranges."""})
    
#     memory.save_context({"input": "Respond to Section 3.2.3 \"General Digital I/O\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.2.1 \"DC Excitation Outputs (PS2)\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: DC Excitation Outputs (PS2)
# 	* To meet the requirements for the Excitation Outputs,
# 1) The 10VDC excitation voltage source SHALL regulate to 10 ± 0.01VDC and provide at least 
# 500mA of current with a maximum output noise of 33μVrms.
# 2) The 20VDC excitation voltage SHALL regulate to 20 ± 0.1VDC and provide at least 100mA of 
# current with a maximum output ripple of 10mVpp.
# NAI will provide the PS2 function module based upon a repackaged COTS circuit. The PS2 will 
# provide the required 1x 10 ±0.01 VDC/500mA (min.)/33µVrms (max noise) and 1x 20 ±0.1
# VDC/100mA (min.)/10mVp-p (max ripple) (one channel) excitation voltage to feedback sensors. The 
# PS2 will be designed to meet or exceed the requirements as outlined in the RFP:
# The PS2 is expected to incorporate LDO & very low noise DC/DC converters. The PS2 is expected to 
# implement continuous output voltage and output current monitoring. It is also expected that the 
# output voltage and current will be monitored in BIT circuits as well as provided to the user."""})

#     memory.save_context({"input": "Respond to Section 3.2.4 \"General Digital I/O (DT1)\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.2.1 \"General Digital I/O (DT1)\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: General Digital I/O (DT1)
# 	* To meet the threshold requirements for the Digital I/O:
# 1) There SHALL be a minimum of 14(T) and 26(O) digital I/O channels
# 2) The digital I/O SHALL be capable of being configured as inputs or outputs in software.
# 3) The digital inputs SHALL be configurable with pull-up resistors allowing a range of at least 0 
# to 5VDC.
# 4) The digital outputs SHALL be open drain output channels capable of sinking current up to 
# 100mA using solid state switching.
# NAI will provide the DT1 function module.
# The DT1-type function provides 24 fundamental Discrete interface function channels. The discrete 
# function provides full featured programmable discrete I/O channels, for either input (voltage or 
# contact sensing with programmable, on-module pull-up/pull down current sources), or output (current 
# source, sink, or push-pull) from an applied external VCC source. 
# The Discrete I/O functions provides full circuitry to program and configure to almost any common 
# platform discrete I/O input or output functions, Typically, they are defined as conversion of:
# - Inputs (programmable thresholds between 0 – 60 VDC) 
# o High contact sense inputs (28 VDC/Open) to a binary value (1 or 0)
# o Low contact sense inputs (Ground/Open) to a binary value (1 or 0)
# o Direct voltage sense input (as compared to programmed thresholds) 
# to a binary value (1 or 0)
# o Condition input discrete signals as required (e.g. filter/debounce, etc.)
# - Outputs (3 – 60 VDC typical external VCC source or GND)
# o Command binary values (1 or 0) to discrete high outputs (VCC/Open)
# o Command binary values (1 or 0) to discrete low outputs (Open/GND)
# o Command binary values (1 or 0) to discrete push-pull outputs (VCC/GND)
# When channels are programmed or defined as inputs, they can be used for either voltage or contact 
# sensing. Channels set for contact sensing (e.g. sensing a relay contact position; OPEN-CLOSED) can 
# be configured with a programmable “pull-up” or “pull-down” (current source or sink) which 
# effectively provides the proper voltage level change to sense the open state of the contact. Essentially, 
# this unique design eliminates the need for external resistors or mechanical jumpers. Instead, this 
# design offers a current source/sink (in banks of 6 channels) that the user programs to a desired current 
# (0-5 mA) level. 
# When channels are programmed as outputs, each channel can be set for high-side (current-source),
# low-side (current-sink) or push-pull (current-source-sink) operation. The load impedance determines 
# the delivered switched output current drive or sink – up to 500 mA per channel. Diode clamping is 
# provided (useful for inductive loads, such as relays) and thermal protection. 
# Overcurrent protection is implemented using current sensing technology. When the current exceeds a 
# programmed threshold of 650 mA steady-state, or a higher peak for short duration, the 
# overcurrent/short-circuit protection is triggered, shutting down the output drivers for safety. The 
# overcurrent fault status will be indicated for the affected channels and will require a reset operation to 
# restore output. To reset this condition, a reset command needs to be issued to the Overcurrent Reset 
# register, which will restore drive output and allow the latched status to be reset. This is separate from 
# the reset for the Overcurrent Interrupt Enable register on this module. It is recommended that a reset 
# command is done whenever status is cleared to avoid a non-apparent output reset condition.
# The 24 channels are configured as 4 banks of 6 channels. Each bank is provided with a separate 
# external input VCC and a ground return (GND) pin. The GND pins are common within the module 
# but are isolated from system (power) GND.
# The DT4 provides additional enhanced Discrete I/O functionality:
# • Additional Enhanced Input Mode Operation: Pulse Measurements, Transition Timestamps, 
# Transition Counters, Period Measurement and Frequency Measurement 
# • Additional Enhanced Output Mode Operation: PWM Output and Pattern Generator Output."""})

#     memory.save_context({"input": "Respond to Section 3.2.5 \"Resistance Temperature Detector Inputs (RT1)\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.2.1 \"Resistance Temperature Detector Inputs (RT1)\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Resistance Temperature Detector Inputs (RT1)
# 	* To meet (and exceed) the threshold channel requirements as outlined within the RFP for the RTD
# Inputs:
# support Resistance Temperature Detector (RTD) inputs specified as follows:
# 1) The RMC SHALL support a minimum of 9 RTD – 3 or 4 wire, PT100 input channels.
# 2) The RTD inputs SHALL have an acquisition resolution of 16 bits or higher.
# 3) The RTD inputs SHALL have a minimum hardware sample rate of 50 Hz.
# The module provides 8 measurement channels, and can be programmed for interfacing to 2, 3, and 4-
# wire platinum RTD sensor configurations. The RTD channels feature individual A/D converters and 
# precision excitation/current drive. Programmable lead-wire compensation is provided for inherently 
# less accurate 2 and 3-wire configurations. All RTD channels are self-aligning because each channel is 
# automatically "aligned" on a rotating basis to eliminate offset and gain errors throughout the 
# operating envelope. Programmability for expected resistance range and wire modes allows for 
# optimization of scaling/resolution, as well as flexibility in reading many RTD types"""})

#     memory.save_context({"input": "Respond to Section 3.2.6 \"Power Switching Outputs (O) (68SR1/SW1)\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.2.1 \"Power Switching Outputs (O) (68SR1/SW1)\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Power Switching Outputs (O) (68SR1/SW1)
# 	* To meet the requirements as outlined within the RFP for the Power Switching Outputs, 
# 1) The RMC SHALL support a minimum of 4 open drain power switching output channels.
# 2) The Power Switching Output channels SHALL be capable of sinking current up to 5A using 
# solid state switching.
# 3) The Power Switching Output should have current monitoring for safety (O).
# NAI will provide the 68SR1 motherboard fitted with the SW1 power-switching function module –
# please see following details."""})
    
#     memory.save_context({"input": "Respond to Section 3.2.7 \"Current Output (O)\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.2.7 \"Current Output (O)\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Current Output (O)
# 	* To meet the requirements as outlined within the RFP for the Current Output as defined:
# NOTE: These outputs need to be protected against inadvertent triggering. Please provide if and how 
# this could be implemented with your solution.
# The RMC SHALL have the capability to trigger a device with a current pulse. The specification for 
# the current pulse of the RMC is as follows:
# 1) The RMC SHALL provide 3(O) Current Output Channels with the capability of providing a 5A ± 
# 2% pulse.
# 2) The RMC SHALL provide the pulse for a duration of >= 50ms.
# There are (2) potential solutions:
# 1. If the current pulse does NOT require current control (if it can be used as another high current 
# discrete solid realy switch, delivering current that is load determined), then an additional SW1 
# module on the 68SR1 board can suffice.
# 2. If the current pulse is required to be controlled (delivering exact current, as specified) AND is 
# the current can be limited to 4A (instead of 5A), the high-efficiency (PWM based) DA5 highcurrent D/A module could be considered, connected with two channels (paired) in parallel for 
# one Current Output channel. This solution would require two modules for delivering 3(O) 
# Current Output Channels – to remain within the four board SIU34 solution, one module would 
# be required to be substituted with the DA5 (potentially one RT1)."""})

#     memory.save_context({"input": "Respond to Section 3.3 \"Communication\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.3 \"Communication\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Communication
# 	* As outlined within the RFP, the RMC SHALL support the following type of I/O:
# 1) Two CAN Bus controllers with at least 1 Mb/s, supporting the CAN 2.0, J1939, and/or 
# ARINC-825 standards. (O)
# 2) Two Gigabit Ethernet interfaces (T)
# 3) Serial Communication – At least 7 channels of RS-422 Ports capable of serial communication 
# in full duplex(O).
# 4) One USB 2.0 (T) or higher (O)."""})
    
#     memory.save_context({"input": "Respond to Section 3.5 \"Power Supply\" of the document RFP-KV-101422-RMC-NAI"},
#                         {"output": """As a program manager at NAI, my response to Section 3.5 \"Power Supply\" of the Request for Proposal (RFP) from Virgin Galactic would include the following: 
# 	* Title: Power Supply
# 	* To meet the basic power supply requirements as outlined within the RFP for the Power Supply, NAI 
# will provide the VPX68 3U OpenVPX power supply unit. The VPX68 meets or exceeds the RFP 
# requirements of: Minimum 90% efficiency (met at specific load conditions), EMI/RFI Input Filter, 
# Input Transient Protection, Input Reverse Polarity Protection, Output Over/Undervoltage, ShortCircuit Protections, Minimum 50 ms Holdup Time (as configured with the 50 ms Hold-up Time 
# option), Input/Output and Chassis Isolation and is designed to meet MIL-STD-704 or equivalent.
# The NAI’s VPX68-3 is an up-to 400 Watt DC/DC Converter that plugs directly into a standard 3U 
# VPX chassis with a VITA 62, 1.0” pitch power supply slot. This off-the-shelf solution for VITA 46.0 
# and VITA 65 systems is compatible with VPX specifications; supports all VITA standard I/O, 
# signals, and features; and conforms to the VITA 62 mechanical and electrical requirements for 
# modular power supplies.
# The VPX68-3 switching power supply is conduction-cooled through the card edge/wedge-lock. It 
# accepts +28 VDC input voltage and provides six outputs at up-to 400 Watts and has Optional, 
# integrated Holdup Time.
# The VPX68-3 can be used either as a single-stage module or a back-end module in a multiple power 
# supply configuration. It supports a variety of standard features, including continuous Background 
# Built-in-Test (BIT); remote error sensing; and protection against transients, over-voltage, overcurrent, and short-circuits. With its intelligent design, the VPX68-3 also has the flexibility to address 
# special needs. This COTS converter is specifically designed with component derating for rugged 
# defense and industrial applications. It is also designed to meet the many harsh environmental 
# requirements of military applications.
# Additionally, to meet the RFP requirement of :
# 2 power inputs in the 18-36Vdc range
# for the production RMC units, NAI will provide the SIU power input with dual 18-36 VDC Power 
# Inputs. NAI plans to tailor the J5 SIU input with:
# 1. A connector board with a single 13-pin connector, pinned for PSU-1 and PSU-2 inputs.
# 2. High-efficiency redundant power supply voltage supervisor to effectively provide switchover
# 3. PSU-1 and PSU-2 input voltage monitoring; such that the input state of the inputs can be 
# monitored and reported to the SBC.
# 4. Support dual independent front-end transient protection and support comparator."""})





# BOEING RESPONSES (ALL)

    # Design and Development

    memory.save_context({"input": """Section: Interface Control Documents (ICD) 
The Supplier shall prepare an Interface Control Document (ICD) that describes the interfaces 
between the Supplier-developed systems/components as defined in the Specification and other 
interfacing systems/components to support interface development, allocation, derivation, 
maintenance, and impact assessments. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.05 – Interface Control Document (ICD) """},
{"output": """NAI plans to prepare and deliver an ICD, in accordance with SDRL E-75.05."""})
    
    memory.save_context({"input": """Section: Human Factors Engineering Program 
The Supplier shall conduct a human engineering program commensurate with the magnitude of 
the human interface modification activity, equipment design complexity and the criticality of the 
soldier-equipment interface. 
The Supplier shall comply with MIL-STD-1472 safety guidelines for operators and maintainers. 
The Supplier shall include Human Factors as an agenda item at Preliminary Design Review 
(PDR) and Critical Design Review (CDR) and present the following: 
a) Report on the application of human factors engineering principles to minimize task 
complexity, personnel hazards, and maintainer workload 
b) Address design impacts on improving task completion, safety and training deficiencies"""},
{"output": """NAI takes exception to providing the requested items in this section of the SSOW. The proposed 
solution is comprised of COTS products."""})
    
    memory.save_context({"input": """Section: Human Factors Engineering in Equipment Design 
The Supplier shall design all Supplier provided equipment to enhance human performance in 
operation, maintenance and support activities in all anticipated operational and environmental 
conditions including: 
 Accommodating the physical anthropometry as defined in the Specification for the 
projected user population 
 Compatibility with operational/protective clothing and gear 
The Supplier shall apply requirements and guidelines from MIL-STD-1472 to the development of 
equipment items and associated operating procedures. The Supplier shall understand and define 
the installation of the equipment in the air vehicle and make necessary accommodations to ensure 
an effective human-machine interface for operation, inspection, removal, replacement and 
servicing. 
The Supplier shall prepare a Human Engineering Requirements Compliance Report (HERCR) 
that documents human engineering guideline compliance, non-compliance, or not applicable, 
based on guidelines defined in MIL-STD-1472. The Supplier may coordinate the requirements 
analysis and HERCR preparation with Boeing Human Factors Engineering. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-12.14 – Human Engineering Requirements Compliance Report (HERCR)"""},
{"output": """Not applicable per the previous section."""})
    
    memory.save_context({"input": """Section: Design for Maintainability 
The Supplier shall incorporate human engineering provisions and adhere to human engineering 
principles of MIL-STD-1472 in the equipment design, for maintainability purposes, including: 
a) Accommodating anthropometry as defined in the Specification 
b) Reducing maintenance task complexity through consideration of accessibility, 
modularity, interchangeability and compatibility with standard tools, support equipment 
and personal gear 
c) Limitations of maintenance personnel skill requirements through maximum use of system 
diagnostic/prognostic capabilities, accessibility of test points, minimization of calibration 
requirements, utilization of ‘throw away’ components and simplified maintenance aids 
and displays 
d) Reduction of potential maintenance errors by designing to eliminate the possibility of 
incorrect connection, assembly and installation, awkward maintenance task sequencing 
and ambiguous labeling and coding 
e) Reduction or elimination of special tools for removal and replacement of the Supplier 
provided equipment 
The Supplier shall prepare Human Engineering Design Approach Document - Maintainer 
(HEDAD-M) data to the level of detail that reflects the design for maintainer activity with a focus 
on describing new equipment or modified elements of existing equipment which impacts the 
human-system maintenance task sequencing and installation and removal of components using 
DI-HFAC-80747 as a guide. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-12.13 – Human Engineering Design Approach Document - Maintainer 
(HEDAD-M)"""},
{"output": """Not applicable per the previous section."""})
    
    memory.save_context({"input": """Section: Reliability and Maintainability (R&M) 
The Supplier shall establish (or update), document, and execute a Reliability and Maintainability 
(R&M) program using MIL-STD-785 Task 101 as a guide. The Supplier shall ensure reliability 
maturation and achievement of the reliability requirements as stated in the Specification by 
conducting and incorporating all applicable analyses such as allocations, predictions, models, 
failure mode effects and criticality analysis, built-in test, demonstrations, reliability growth, 
derating, thermal analysis, fault tree analysis, and electronic part circuit tolerance analysis. The 
Supplier shall perform all analyses for the worst case environments in accordance with the 
Specification. 
The Supplier shall present the R&M program plan and status at System Requirement Review 
(SRR) and PDR and shall provide updates at each technical review."""},
{"output": """NAI plans to present the overall R&M plan at SRR. This will not include reliability growth, not a 
Software/Firmware FMECA, as indicated in their respective sections, below."""})
    
    memory.save_context({"input": """Section: Reliability Prediction 
The Supplier shall perform reliability predictions in accordance with MIL-STD-785 Task 203 
under the appropriate environment as defined in the Specification. The Supplier shall base 
cooling conditions on worst-case temperature and flow rate for continuous conditions as outlined 
in the Specification. The Supplier shall conduct derating analysis to verify components are 
applied on a derated basis in accordance with the Specification. Results of the derating analysis 
shall be provided in the reliability prediction report.
The Supplier shall perform reliability predictions using legacy data with adjustments as 
appropriate for design and usage differences. Where legacy source data is used, the prediction 
process will include estimated impacts due to differences between the FLRAA 
systems/components and the equivalent fielded systems/components. Legacy field data is subject 
to adjustments to account for technical design changes (especially those that eliminate specific 
failure modes), improvements, ship-set quantities, operating environments, and duty cycles. 
Substantiation of the data is required. 
For cases in which legacy data is not available, the Supplier shall use other sources that include 
(but are not limited to): 
 System and Part Integrated Data Resource (SPIDR) database. The SPIDR database 
includes: 
o Non-electronic Parts Reliability Data (NPRD) 
o Electronic Parts Reliability Data 
o Failure Mode Distribution Data 
o Electrostatic Discharge Susceptibility Data 
 MIL-HDBK-217 Reliability Prediction of Electronic Equipment 
 Supplier Predictions 
 Naval Surface Warfare Center (NSWC) HDBK of Reliability Prediction for Mechanical 
Equipment 
 NPRD Publication 
The Supplier shall present the prediction methodology at SRR. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-14.03 – Reliability Prediction Report"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-14.03 – Reliability Prediction Report"""})
    
    memory.save_context({"input": """Section: Failure Modes, Effects, and Criticality Analysis (FMECA) 
The Supplier shall develop a Failure Modes Effects and Criticality Analysis (FMECA) to provide 
an analysis of all plausible independent single item failures and the resulting potential impact on 
mission success, performance, safety, and maintainability. The Supplier shall develop the 
FMECA with the identification of all failure modes, as defined below, and proposed elimination 
or mitigation for Category I and II failure modes. The Supplier shall identify existing design 
criteria or other procedures to mitigate identified Category I, and II failure modes. Where such 
criteria and procedures are not in place, the Supplier shall develop and implement corrective 
actions to eliminate or mitigate these conditions. 
Category Severity Description 
I Catastrophic A failure which may cause death or system loss (i.e., aircraft, 
tank, missile, ship) 
II Critical A failure which may cause severe injury, major property 
damage, or major system damage which will result in mission 
loss 
III Marginal A failure which may cause minor injury, minor property 
damage, or minor system damage which will result in delay or 
loss of availability or mission degradation
Category Severity Description 
IV Minor A failure not serious enough to cause injury, property, or 
system damage, but which results in unscheduled maintenance 
or repair 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-14.04 – Failure Modes, Effects, and Criticality Analysis (FMECA) Report"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-14.04 – Failure Modes, Effects, and Criticality Analysis (FMECA) Report"""})
    
    memory.save_context({"input": """Section: Software and Firmware Failure Modes, Effects, and Criticality Analysis 
(FMECA) 
The Supplier shall perform a FMECA for any software or firmware in accordance with 
ANSI/AIAA-S-102.2.4 and IEEE 1633 Recommended Practices for Software Reliability as a 
guide. 
The Supplier shall identify the operational impacts that computing hardware and hardware / 
software interface failures could have on the software and the software response to the failure. 
The Supplier shall include a Single Event Effect analysis using the methodology of 
DOT/FAA/TC-15/62. As applicable, the Supplier shall identify Multi-Core Processors (MCP) 
and Programmable hardware or firmware failure modes associated with interference channels in 
the chip fabric, shared resources, the configuration settings, and any other unique failures that 
could result in anomalous non-deterministic behavior of the MCP/Programmable 
hardware/firmware. 
The Supplier shall document software and firmware FMECA as part of SDRL Data Item E-14.04 
– Failure Modes, Effects, and Criticality Analysis (FMECA) Report."""},
{"output": """Exception taken."""})
    
    memory.save_context({"input": """Section: Failure Reporting, Analysis and Corrective Action System (FRACAS) 
The Supplier shall establish a closed loop Failure Reporting, Analysis, and Corrective Action 
System (FRACAS) in accordance with MIL-HDBK-2155 to document failures, root cause, and 
corrective action taken. The Supplier may use its existing FRACAS with modification as 
necessary to meet the requirements specified in this SSOW. 
The Supplier shall document all failures that occur during formal testing in the Supplier 
FRACAS. Formal testing includes acceptance tests, manufacturing screening, performance 
testing, qualification testing, and reliability testing. The Supplier shall also document failures for 
components returned to the Supplier for discrepancies which occurred during system integration 
testing and flight testing. 
The Supplier shall prepare a FRACAS plan that includes a complete description of the Supplier 
FRACAS. 
The Supplier shall include provisions to facilitate failure reporting in all test plans and procedures 
utilized during development. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-14.46 – Failure Reporting, Analysis and Corrective Action System 
(FRACAS) Plan"""},
{"output": """NAI has a FRACAS system in place. Generating a FRACAS plan adds no value to the program 
or platform. In the event of a failure, NAI plans to generate a FRACAS report and deliver it to 
Boeing. Exception taken."""})
    
    memory.save_context({"input": """Section: Failure Reporting, Analysis, and Corrective Action 
The Supplier shall complete a failure analysis report for any failure that requires reporting in the 
Supplier FRACAS in accordance with the guidelines defined in the FRACAS section of this 
SSOW. The Supplier shall submit a preliminary report within 2 business days after the failure is 
discovered. At a minimum, the Supplier shall include all known details at the time of the failure 
in the preliminary report. The Supplier shall provide updates as progress is made in determining 
root cause and corrective action. The Supplier shall prepare a final failure analysis report after 
root cause and corrective action have been implemented. During the test phase, the Supplier shall 
provide the status of all failure reports at scheduled teleconferences as appropriate. 
At the completion of all developmental testing, the Supplier shall prepare a Failure Summary and 
Analysis Report. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-14.09 – Failure Analysis Report 
 Data Item E-14.28 – Failure Summary and Analysis Report"""},
{"output": """NAI agrees with the information provided in this section of the SSOW. A combined report shall 
satisfy both SDRLs E-14.09 and E-14.28."""})
    
    memory.save_context({"input": """Section: Built-In Test (BIT) Data 
The Supplier shall implement an integrated diagnostic process, using Society of American 
Engineers (SAE) JA 6268 as a guide, to ensure that the design meets the fault detection/fault 
isolation specified diagnostic performance and maintenance data collection requirements of the 
Specification. 
The Supplier shall prepare a Built-In Test (BIT) Fault Detection / Isolation Analysis Report for the 
product at the Operational Level of Maintenance as part of Data Item E-35.08. 
The Supplier shall identify the recommended method(s) for detecting, isolating, and reporting 
each relevant failure mode to operators and maintainers unless the following criteria are satisfied: 
A) Automated monitoring of that failure mode would cause a significant detrimental impact 
on program cost, schedule, or risk. The Supplier shall work with Boeing to assess the 
technical feasibility, maturity, hardware/software cost, and reliability of automated BIT 
failure monitors during this assessment. 
B) A mutually acceptable alternate means of detecting and isolating the failure is available, 
based on the anticipated impact to system/vehicle operations, including availability, 
mission reliability, repair time, and down time. Viable alternatives may include the use of 
system level BIT tests, flight line support equipment or manual troubleshooting 
procedures to augment internal equipment BIT capabilities. 
For failure modes automatically detected, the Supplier shall enumerate the specific BIT test(s) or 
other applicable failure monitors. For failure modes not automatically detected, the Supplier shall 
document both the rationale and the alternate method for detecting and reporting the failure in the 
field. For failure modes not automatically isolated, the Supplier shall document both the rationale 
and the alternate method for manually isolating the failure in the field.
The Supplier shall document all external interface signals that are required to control equipment 
BIT operations, receive summary BIT status and test results, access internal failure logs, and 
collect data to support maintenance and maturation activities. 
The Supplier shall prepare BIT Data as specified in the Specification and submit in accordance 
with the following data item(s): 
 Data Item E-35.08 – Built-In Test (BIT) Data """},
{"output": """Exception. NAI plans on delivering manuals for its COTS products comprising this solution. BIT 
operation is described in those documents, along with sample code. Additional support is 
available upon request."""})
    
    memory.save_context({"input": """Section: Reliability Growth 
The Supplier shall conduct a reliability growth program to find and eliminate failure modes 
discovered during the Product’s development, qualification, and acceptance testing. 
The Supplier shall prepare a Reliability Growth Test Plan that describes the test and development 
activities to be conducted. 
The Supplier shall define the test methods by which the Product reliability will be improved and 
document in the Reliability Growth Plan. 
Methods may include, but are not limited to, the following:
 Endurance test using the combined environmental test condition profile as 
defined in the Specification
 Highly Accelerated Life Testing (HALT) – HALT testing subjects the component beyond 
Specification stress levels to identify weaknesses and to correct the weaknesses 
 Accelerated Life Testing (ALT) – For equipment where wear-out is the dominant failure 
mode 
The Supplier shall prepare a Reliability Growth Test Report that document the results of the 
testing activity. The Supplier shall develop and maintain a reliability growth planning curve 
which provides an initial Mean Time Between Failure (MTBF) projection based on test results 
and tracks achievement towards attainment of the Specification MTBF requirement as testing 
proceeds in accordance with MIL-HDBK-781 and MIL-HDBK-189. 
The Supplier shall perform root cause failure analysis and recommend corrective action for the 
failures discovered during testing, document and report in accordance with the FRACAS activity 
as defined in this SSOW. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-14.16a – Reliability Growth Test Plan 
 Data Item E-14.16b – Reliability Growth Test Report"""},
{"output": """Exception. NAI strongly recommends not performing a reliability growth program, particularly 
without first having performed a full reliability prediction. The additional cost and schedule 
impact will be significant and therefore are not quoted in this response."""})
    
    memory.save_context({"input": """Section: Manufacturing Screening 
The purpose of manufacturing screening is to find latent defects in equipment prior to delivery. 
The Supplier shall employ manufacturing screening in accordance with requirements set forth in 
the equipment Specification. Screening methods may include but are not limited to: 
 Environmental Stress Screening (ESS)
 Highly Accelerated Stress Screening (HASS)
 Burn-in testing 
The Supplier shall document the planned manufacturing screening methods as part of SDRL Data 
Item E-59.05, Acceptance Test Procedures (ATP). 
The Supplier shall document manufacturing screening results as part of SDRL Data Item E-59.06, 
Acceptance Test Records, and make the Acceptance Test Records available upon Boeing request."""},
{"output": """NAI intends to perform ESS on the proposed units. A procedure will be submitted as part of 
SDRL E-59.05."""})
    
    memory.save_context({"input": """Section: Maintainability Prediction 
During the design of the equipment, the Supplier shall evaluate the physical maintainability 
design features and verify compliance with requirements specified in the Specification and record 
in a Maintainability Prediction Report. 
The Supplier shall perform maintainability analysis to facilitate an early assessment of the 
maintainability of the design, and enable early decisions concerning the compatibility of a 
proposed design with specified requirements or the choice of better alternatives. 
The Supplier shall present the maintainability prediction methodology and approach at SRR. 
The Supplier shall present the qualitative assessment of equipment maintainability prediction at 
PDR. 
The Supplier shall present the quantitative assessment of equipment maintainability prediction at 
CDR. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-13.04 – Maintainability Prediction Report"""},
{"output": """NAI will generate a maintainability prediction report, in accordance with SDRL E-13.04."""})
    
    memory.save_context({"input": """Section: Circuit Tolerance Analysis 
The Supplier shall complete a circuit tolerance analysis in accordance with MIL-STD-785 Task 
206. The Supplier shall incorporate lessons learned from the analysis into the design and 
development of the Product. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-14.05 – Electronic Part Circuit Tolerance Analysis Report """},
{"output": """Exception. The proposed solution is COTS."""})
    
    memory.save_context({"input": """Section: Thermal Analysis 
For development components, the Supplier shall perform a thermal analysis to predict equipment 
temperatures based on the worst-case environment temperature conditions defined in the 
Specification. The Supplier shall perform the thermal analysis using MIL-STD-2218 as guidance 
for steady state and transient conditions including those present during normal flight, pre-flight, 
post-flight, ground maintenance operation, emergency flight, and storage to ensure that the 
mechanical design has included all reasonable provisions to minimize the impact of temperature 
on equipment reliability. 
For non-developmental items, modified Commercial off the Shelf (COTS), or COTS components, 
the Supplier shall provide existing thermal analysis data to ensure that the mechanical design has 
included all reasonable provisions to minimize the impact of temperature on equipment 
reliability. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-38.01 – Thermal Analysis Report """},
{"output": """NAI will generate a Thermal Analysis report, in accordance with SDRL E-38.01."""})
    
    memory.save_context({"input": """Section: Vibration Analysis 
For development components, the Supplier shall perform an analysis of the equipment’s dynamic 
response to the combination of vibration and static loads as defined in the Specification. The 
Supplier shall base the analysis on the dynamic environment defined in the Specification at the 
equipment’s interface with the aircraft and any dynamic loads that may be generated by the 
equipment and the air vehicle. The Supplier shall use the analysis data to establish and refine 
design requirements for the system and components. The Supplier shall present results of this 
analysis, as applicable, during Technical Interchange Meetings (TIMs) and at PDR. 
For non-developmental items, modified COTS, or COTS components, the Supplier shall provide 
existing vibration analysis data to ensure that the design has included all reasonable provisions to 
minimize the impact of vibration on equipment reliability. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-14.48 – Vibration Analysis """},
{"output": """NAI will generate a Vibration Analysis, in accordance with SDRL E-14.48"""})
    
    memory.save_context({"input": """Section: Power Analysis and Wiring Interface Requirements 
The Supplier shall prepare power requirements analysis and wiring interface data that documents 
primary input current requirements to the equipment along with connector, pin, and signal data. 
The Supplier shall contact the Boeing technical point of contact for resolutions to any questions 
related to this data item. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-26.01 – Power Requirements and Wiring Interface Data"""},
{"output": """NAI will generate a Power Requirements and Wiring Interface Data report, in accordance with 
SDRL E-26.01."""})
    
    memory.save_context({"input": """Section: General Software/Firmware Requirements 
Boeing will define the Design Assurance Level (DAL) of the Product in the Specification or upon 
request. The Supplier shall design, develop, test, verify, document, and maintain all software and 
programmable hardware in accordance with the applicable requirements, based on the Product’s 
Design Assurance Level (DAL), found in the Specification, RTCA/DO-178, RTCA/DO-330, 
RTCA/DO-331, RTCA/DO-332, and RTCA/DO-254, and their applicable annex, where “should” 
and “must” are to be considered “shall” requirements regardless of the language used, unless 
otherwise agreed to on a case by case basis and documented. 
For the purposes of this SSOW, any electronic hardware that contains firmware shall be 
considered to be complex electronic hardware as defined by DO-254. The term hardware is 
understood to mean firmware when used in data deliverables referencing DO-254. Firmware is 
defined as the micro-code and/or logic contained in programmable components such as 
Application Specific Integrated Circuit (ASIC) and Programmable Logic Devices (PLD), 
including any associated macro functions. The PLD/ASIC devices are typically programmed in 
Hardware Definition Language (HDL) such as Verilog or Very High Speed Integrated Circuit 
(VHSIC) Hardware Description Language (VHDL). PLDs include, but are not limited to, 
Electrically Programmable Logic Device, Programmable Array Logic (PAL), Programmable 
Logic Arrays (PLA), and Field Programmable Gate Array (FPGA). ASIC is an Integrated Circuit 
customized for a particular use, rather than intended for general purpose use. Modern ASICs 
include entire 32 bit processors, memory devices such as Read Only Memory (ROM), Random 
Access Memory (RAM), Electrically Erasable Programmable Read-Only Memory (EEPROM), 
and Flash. 
The Supplier shall define the software and firmware approaches in the Plan for Software Aspects 
of Certification (PSAC) and the Plan for Hardware Aspects of Certification (PHAC), 
respectively. The Supplier shall measure progress to those plans in the Software Accomplishment 
Summary (SAS) and the Hardware Accomplishment Summary (HAS), respectively. 
The Supplier shall document the changes necessary between existing Supplier software and the 
software Product as defined by the Specification in the Software Change Impact Analysis. The 
Software Change Impact Analysis shall evaluate, mitigate and document all impacts associated 
with the change and that the changes are flowed to affected requirements, design, architecture, 
code and testing artifacts. 
The Supplier shall provide existing PSAC, PHAC, SAS, and HAS documents in accordance with 
the SDRL(s) for reused, off-the-shelf, or non-developmental software or firmware. For new and 
modified software or firmware, the Supplier shall prepare and deliver documents in accordance 
with the SDRL(s) incorporating required changes. 
If the Supplier has data supporting previously certified equipment installations, including 
Technical Standard Orders (TSOs), Military Standard Orders (MSOs), compliance to DO-178 
(software), and/or DO-254 (firmware), data may be presented to Boeing at the initial meeting for 
review and approval in lieu of software and firmware data item submittals as identified 
throughout this SSOW. 
The Supplier shall submit the following data item(s) in accordance with the SDRL:
 Data Item E-66.89 – Software Change Impact Analysis 
 Data Item E-77.21 – Plan for Hardware Aspects of Certification (PHAC) 
 Data Item E-77.49 – Hardware Accomplishment Summary (HAS) 
 Data Item E-78.71 – Plan for Software Aspects of Certification (PSAC) 
 Data Item E-78.81 – Software Accomplishment Summary (SAS) """},
{"output": """NAI understands that this effort comprises a full flight certification. An initial alignment meeting 
with the certification authority (responsible DER) is required before this portion of the program 
can be properly estimated and proposed. We are unable to provide this pricing component at the 
moment, as we require further conversation with Boeing engineering. NAI will estimate all 
aspects of this portion of the program after the aforementioned meeting has taken place, and all 
requirements have been finalized.
NAI agrees to generate and deliver the following data items:
• Data Item E-66.89 – Software Change Impact Analysis
• Data Item E-77.21 – Plan for Hardware Aspects of Certification (PHAC)
• Data Item E-77.49 – Hardware Accomplishment Summary (HAS)
• Data Item E-78.71 – Plan for Software Aspects of Certification (PSAC)
• Data Item E-78.81 – Software Accomplishment Summary (SAS)"""})
    
    memory.save_context({"input": """Section: Stages of Involvement (SOI) Reviews 
The Supplier shall collaborate with Boeing in scheduling, preparing for, hosting, and providing 
all required data to successfully satisfy the four Stages of Involvement (SOI) reviews in 
accordance with FAA Order 8110.49 Chg. I (for software) and FAA Order 8110.105 (for 
firmware), where “should” and “must” for supplier and applicant guidance shall be considered 
“shall” for the Supplier in this guidance. The Supplier shall address all deficiencies and findings 
from each SOI Review within 45 days of the SOI event submitting the corresponding 
documentation requiring revision as SDRL submissions. The Supplier may request extensions to 
this deadline on a case by case basis for Boeing approval. The Supplier shall include all SOI 
review events (SOI #1, SOI #2, SOI #3, and SOI #4) in the first and all subsequent submissions 
of the Supplier Schedule. The scope and timing of SOI reviews will be mutually agreed to based 
on the schedule, degree of modification, and development process. The Supplier shall ensure all 
DO-178 (for Software) and DO-254 (for firmware) objectives are satisfied and where applicable, 
the objectives of DO-278, DO-330, DO-331, DO-332, DO-333 are satisfied."""},
{"output": """NAI agrees fundamentally to support Boeing through the SOI process. As previously mentioned, 
an initial alignment meeting with Boeing’s DER will provide clarity and direction in this area."""})
    
    memory.save_context({"input": """Section: Software and Firmware Development 
The Supplier shall develop software and firmware in a manner consistent with the reference 
documents and specifications outlined in the General Software/Firmware Requirements Section. 
The Supplier shall satisfy the relevant software and firmware development process requirements 
and align them with the program and technical reviews and activities as well as the Stages of 
Involvement (SOI) reviews, if applicable. 
The Supplier shall document software and firmware problem reports and safety issues through a 
software/firmware/change tracking database The Supplier shall prepare Software Problem 
Reports and Firmware Problem reports in accordance with DO-178 and DO-254, respectively. 
The Supplier shall provide existing development documents in accordance with the SDRL(s) for 
reused, off-the-shelf, or non-developmental software or firmware. For new and modified software 
or firmware, the Supplier shall prepare and deliver development documents in accordance with 
the SDRL(s) incorporating required changes. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-77.22 – Hardware Design Plan 
 Data Item E-77.46 – Hardware Problem Reports 
 Data Item E-78.01 – Software Development Plan (SDP) 
 Data Item E-78.83 – Software Problem Reports"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-77.22 – Hardware Design Plan
• Data Item E-77.46 – Hardware Problem Reports
• Data Item E-78.01 – Software Development Plan (SDP)
• Data Item E-78.83 – Software Problem Reports"""})
    
    memory.save_context({"input": """Section: Software and Firmware Design 
The Supplier shall design software and firmware in a manner consistent with DO-178 and DO254, respectively, along with the reference documents and specification outlined in the General 
Software/Firmware Requirements Section. If implementing a database as part of the Product, the 
Supplier shall prepare a database design description. 
The Supplier shall leverage existing products, designs, and artifacts to maximize reuse of 
commercial or flight-tested products. The Supplier shall inform Boeing of any COTS software or 
firmware and reusable software or firmware used in the Product/design to meet the end item 
performance requirements. The Supplier shall identify all licenses and maintenance agreements 
related to these products and ensure that all required licenses and maintenance agreements are 
delivered with the Supplier’s Product. 
The Supplier shall provide existing design documents in accordance with the SDRL(s) for reused, 
off-the-shelf, or non-developmental software or firmware. For new and modified software or 
firmware, the Supplier shall prepare and deliver design documents in accordance with the 
SDRL(s) incorporating required changes. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-66.88 – Database Design Description (DbDD) 
 Data Item E-77.28 – Hardware Design Standards 
 Data Item E-77.52 – Hardware Design Description (HDD ) 
 Data Item E-78.05 – Software Design Description (SDD) 
 Data Item E-78.06 – Interface Design Description (IDD) 
 Data Item E-78.26 – Software Transition Plan (STrP)"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-66.88 – Database Design Description (DbDD)
• Data Item E-77.28 – Hardware Design Standards
• Data Item E-77.52 – Hardware Design Description (HDD)
• Data Item E-78.05 – Software Design Description (SDD)
• Data Item E-78.06 – Interface Design Description (IDD)
• Data Item E-78.26 – Software Transition Plan (STrP)"""})
    
    memory.save_context({"input": """Section: Programming Language and Operating System Requirements 
The Supplier shall document, as part of the SDP and/or the PSAC, the proposed compilers, 
programming languages, and Operating Systems (OS). The Supplier shall include the 
programming languages methods, rules, and tools to be used to code the software. The Supplier 
shall ensure the OS and driver software have all appropriate security patches applied. """},
{"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Software and Firmware Requirements Analysis 
The Supplier shall capture and provide traceability for all software and firmware requirements 
including the derived, low-level design and interface requirements as part of the Software 
Requirements Specification (SRS), Hardware Requirements Specification (HRS), and Interface 
Requirements Specification (IRS). The Supplier shall identify the standards, methods, and tools 
used to develop, capture and manage requirements and to maintain traceability information. The 
Supplier is encouraged to utilize automated tools in the performance of requirements 
management. The Supplier shall maintain complete traceability of all system requirements to 
requirements to design to code to testing, and requirements to testing in a bi-directional fashion 
(top down and bottom up). 
The Supplier shall provide existing requirements analysis documents in accordance with the 
SDRL(s) for reused, off-the-shelf, or non-developmental software or firmware. For new and 
modified software or firmware, the Supplier shall prepare and deliver requirements analysis 
documents in accordance with the SDRL(s) incorporating required changes. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-77.31 – Hardware Requirements Specification (HRS) 
 Data Item E-78.03 – Software Requirements Specification (SRS) 
 Data Item E-78.04 – Interface Requirements Specification (IRS) """},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-77.31 – Hardware Requirements Specification (HRS)
• Data Item E-78.03 – Software Requirements Specification (SRS)
• Data Item E-78.04 – Interface Requirements Specification (IRS)"""})
    
    memory.save_context({"input": """Section: Software Programmer’s Manual (SPM) 
The software programmer’s manual shall define all software interfaces to the hardware to be 
delivered. These interfaces shall be described at a high, functional level down to a low, register 
level, including individual bit-field descriptions, with levels of detail in between as appropriate. 
The software programmer’s manual shall also define the application software interfaces to all 
subcontractor-developed software to be delivered (e.g., device drivers). 
The software programmer’s manual shall have a consistent format and content for each section. 
References to bits, registers, software routines, and other proper and unique elements shall be 
unambiguous. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-78.13 – Software Programmer’s Manual (SPM) """},
{"output": """NAI agrees to generate and deliver the following data items:
 • Data Item E-78.13 – Software Programmer’s Manual (SPM)
NAI may elect to submit a standard device manual in lieu of creating a new document. This 
would be decided upon after initial discussions with Boeing’s DER."""})
    
    memory.save_context({"input": """Section: Software Metrics 
The Supplier shall report on and provide the software metrics set at TIMs, SOI Reviews, and 
program/technical reviews, as part of status updates or presentation materials and meeting 
minutes, as applicable. The final set of software and firmware metrics will be agreed to by Boeing 
and the Supplier. Common software metrics include: 
 Planned and actual size; presented in source lines of code 
 Software personnel 
 Software volatility 
 Design progress 
 Code and integration progress 
 Test progress 
 Schedule progress 
 Product quality 
 Process performance and computer resource utilization 
The Supplier may propose tailoring based upon the level of development required or propose 
additional metrics for Boeing approval that would provide insight into software cost, schedule, 
progress, size, quality, and reliability. 
Software metrics estimation, data measurement, collection and reporting shall be described in the 
Supplier SDP. """},
{"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Software and Firmware Development Testing 
The Supplier shall develop and document plans for software and firmware testing, including plans 
for all software and firmware testing and formal software and firmware verification activities 
including inspections, reviews, analyses, demonstrations, and tests in accordance with the 
Specification. The Supplier’s Software Test Plan (STP) shall address the development testing and 
verification of all software products. 
The Supplier shall perform adequate testing to provide the necessary coverage required by DO178 for the assigned Design Assurance Level (DAL) of the associated high-level requirements, 
low level requirements, or software structure. 
Prior to software release for formal integration, the Supplier shall verify satisfaction of software 
requirements, IRS requirements (if applicable) and ICD criteria. 
For any reused, off-the-shelf, or non-developmental software or firmware, the Supplier may 
provide the existing software and/or firmware test documentation. 
The Supplier shall provide a system level and software level functional Software Test Description 
(STD) and Software Test Report (STR). The Supplier shall document and address all software 
resets. The Supplier shall review the status of software reset resolution during Technical 
Interchange Meetings (TIMs) and design reviews (refer to the Reviews and Audits section, 
herein). 
The Supplier shall develop hardware test procedures and test in accordance with the approved 
hardware test procedures. The Supplier shall document all hardware test results. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-77.23 – Hardware Validation Plan 
 Data Item E-77.43 – Hardware Test Procedures 
 Data Item E-77.44 – Hardware Test Results 
 Data Item E-77.41 – Hardware Review and Analysis Procedures (HRAP) 
 Data Item E-77.42 – Hardware Review and Analysis Results (HRAR) 
 Data Item E-78.07 – Software Test Plan (STP) 
 Data Item E-78.08 – Software Test Description (STD) 
 Data Item E-78.09 – Software Test Report (STR) """},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-77.23 – Hardware Validation Plan
• Data Item E-77.43 – Hardware Test Procedures
• Data Item E-77.44 – Hardware Test Results
• Data Item E-77.41 – Hardware Review and Analysis Procedures (HRAP)
• Data Item E-77.42 – Hardware Review and Analysis Results (HRAR)
• Data Item E-78.07 – Software Test Plan (STP)
• Data Item E-78.08 – Software Test Description (STD)
• Data Item E-78.09 – Software Test Report (STR)"""})
    
    memory.save_context({"input": """Section: Cybersecurity 
To ensure that industry partners are protecting government data, the Supplier shall implement a 
Cybersecurity program for the Supplier’s Information Technology (IT) Environment in 
accordance with National Institute of Standards and Technology (NIST) Special Publication (SP) 
800-171 and Defense Federal Acquisition Regulation Supplement (DFARS) clause 252.204-
7012. As part of the cybersecurity program, the Supplier shall create and submit a System 
Security Plan (SSP). 
If the Supplier identifies any deficiencies in their implementation of NIST SP 800-171 security 
requirements, the Supplier shall include a Plan of Action and Milestones (POAM) for the 
correction of the identified deficiencies within the SSP. The POAM shall be developed in 
accordance with DI-MGMT-82190 and Department of Defense Instruction (DoDI) 8510.01. The 
Supplier shall immediately notify Boeing of any failure or anticipated failure to meet a milestone 
in the POAM. 
The Supplier shall submit the following data item(s) in accordance with the requirements above 
and the SDRL: 
 Data Item E-75.41 – System Security Plan (SSP) """},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-75.41 – System Security Plan (SSP)
It should be pointed out that Cybersecurity as a whole is not being priced as of the date of this 
document. NAI can estimate once an initial alignment meeting has taken place. SDRL 
compliance follows"""})
    
    memory.save_context({"input": """Section: Cybersecurity Risk Assessment 
The Supplier shall implement methodologies to ensure the delivery of a secure product to Boeing 
in accordance with NIST 800-30, Guide for Conducting Risk Assessments, NIST SP 800-53, 
Security and Privacy Controls for Federal Information Systems and Organizations.
The Supplier shall perform an initial system security assessment in accordance with NIST SP 800-
30, NIST SP 800-37, and NIST SP 800-53A, that:
 Identifies potential threats (human intentional/unintentional, natural, and environmental) 
to the information system component/sub system;
 Identifies flaws/weaknesses in the information system component/subsystem that could 
be exploited by a potential threat;
 Recommends additional security controls to mitigate identified vulnerabilities;
 Identifies the likelihood or probability of a potential threat exploiting a vulnerability;
 Identifies the impact of exploitation for each vulnerability;
 Documents the initial and residual risk based on threat, likelihood, and impact;
 Identifies all logic bearing components responsible for any programmable behavior in the 
system; 
 Documents a Key Management Plan (KMP) for any cryptographic keys, as applicable; 
 Identifies weaknesses for all developed code (new, and legacy and modified) for the 
delivered product; 
 Plan of Action and Milestones (POAM) describing current disposition of any discovered 
vulnerabilities and security findings in the delivered product and intended corrective 
actions for those findings. 
Upon Boeing approval, the Supplier shall implement the additional Supplier recommended security 
controls. 
The Supplier shall participate in periodic System Assessment & Authorization (A&A) working 
group teleconferences in support of the A&A process throughout the period of performance. This 
is in support of Boeing obtaining Authorization to Operate (ATO) from the U.S. Department of 
Defense. Frequency of working group meetings will not exceed once per month for a duration of 
up to one (1) hour per meeting. 
The Supplier shall submit the following data item(s) in accordance with the requirements above 
and the SDRL:
 Data Item E-75.94 – Cybersecurity Risk Assessment"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-75.94 – Cybersecurity Risk Assessment"""})
    
    memory.save_context({"input": """Section: Supply Chain Risk Management (SCRM) 
The Supplier shall develop and implement a Supply Chain Risk Management (SCRM) program 
in accordance with the most current version of NIST SP 800-161 to ensure that all items the 
Supplier provides (including spares and repair parts) do not incorporate counterfeit parts, 
malicious code, or any other elements that would allow adversaries to gain unauthorized access to 
data, alter data, interrupt communications, or otherwise disrupt operations. 
The Supplier shall notify Boeing of any identified threatened, attempted, or successful breach of 
the Supplier’s components, software/firmware, or systems that have potential adverse impacts to 
the confidentiality, integrity, and availability of information and communication technologies as 
defined in Department of Defense Directive (DoDD) 5200.44. 
The Supplier shall prepare a record of the chain of custody of the software, firmware, or logic 
bearing components (as identified in the Cybersecurity Risk Assessment section) delivered under 
this contract and include records from first tier suppliers. 
For modified components, the chain of custody record shall commence with the initiation of the 
modification of the delivered component. For unmodified components, the chain of custody 
record shall commence with the receipt of the component from the first tier supplier. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.77 – Supply Chain Risk Management (SCRM) Assessment/Report 
 Data Item E-76.49 – Chain of Custody Record"""},
{"output": """NAI takes exception to providing the requested items in this section of the SSOW.67"""})
    
    memory.save_context({"input": """Section: Statement of Volatility 
The Supplier shall prepare a Statement of Volatility outlining all volatile and non-volatile 
memory components (e.g. EEPROM, Flash, battery-backed RAM, FPGA) if contained in 
hardware components delivered under this contract. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.96 – Statement of Volatility"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-75.96 – Statement of Volatility"""})
    
    memory.save_context({"input": """Section: Joint Test Action Group (JTAG) Ports 
The Supplier shall document all Joint Test Action Group (JTAG) ports within the Supplier’s 
component. For all disabled JTAG ports, the Supplier shall provide evidence of being disabled 
(e.g., test report, design drawing). For all enabled JTAG ports, the Supplier shall provide 
justification for leaving the JTAG ports enabled. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-76.50 – Joint Test Action Group (JTAG) Connector Report"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-76.50 – Joint Test Action Group (JTAG) Connector Report"""})
    
    memory.save_context({"input": """Section: Software Assurance Plan (SwAP) 
The Supplier shall comply with security requirements in accordance with DoDI 8500.01 and the 
National Security Agency Guide for Addressing Malicious Code Risk, where applicable. 
The Supplier shall develop a Software Assurance Plan (SwAP) that contains procedures and tools 
that will be used to identify and mitigate vulnerabilities resident in new and modified software 
and firmware. The Supplier shall propose mitigations for vulnerabilities discovered in all new and 
modified software and firmware, and implement mitigations, with Boeing coordination. The 
Supplier SwAP shall describe the following:
 All personnel involved in this effort and that the personnel are appropriately qualified 
with security clearances, certifications, qualifications, training, etc.
 Each entry should include Computer Software Configuration Item (CSCI) unique name 
 Software description 
 Manufacture name and manufacturing country of origin 
 Applicable licenses 
 Dependent code modules, patch level, and most recent patch date 
 Associated compiler with reference to its CSCI 
 The provenance of all third party and non-modified software (Note: provenance includes 
describing the source of the third party software and the software’s country of origin)
 The extent and completion level to which all software and firmware has been tested for 
vulnerabilities
 Descriptions of the development environment tools and countermeasures used to develop 
software
 Identification of all software that was/is developed, modified or remediated by foreign 
nationals or in foreign environments, including COTS software and software specifically 
developed, modified, or remediated for this program 
 Descriptions of all countermeasures employed to minimize the security risks associated 
with foreign nationals who developed, modified or remediated the COTS software in the 
Software Assurance Plan 
 Static Code Analysis results for all developed software
 Dynamic code analysis results for all developed software 
 Malicious code review results for all developed software 
 Any available static code analysis results for third party software, including free and open 
source code 
 Identifies weaknesses for all developed code (new, and legacy and modified) for the 
delivered product
The Supplier shall submit the following data item(s) in accordance with the requirements above 
and the SDRL: 
 Data Item E-78.60 – Software Assurance Plan (SwAP)"""},
{"output": """NAI takes exception to providing the requested items in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Cybersecurity Testing 
The Supplier shall develop a Cybersecurity Test Plan (CTP) and Cybersecurity Test Description 
(CTD) to verify cybersecurity requirements defined in the Specification. 
The Supplier shall conduct cybersecurity testing and evaluation in accordance with the Boeing 
approved CTP and CTD. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-76.45 – Cybersecurity Test Plan (CTP) 
 Data Item E-76.46 – Cybersecurity Test Description (CTD) 
 Data Item E-76.47 – Cybersecurity Test Results (CTR) 
If required, on a separate purchase contract, Boeing may require the Supplier to support Boeing 
cybersecurity testing of the Supplier’s delivered Product(s) and recommend corrective actions if 
issues are identified."""},
{"output": """Cybersecurity Testing 
The Supplier shall develop a Cybersecurity Test Plan (CTP) and Cybersecurity Test Description 
(CTD) to verify cybersecurity requirements defined in the Specification. 
The Supplier shall conduct cybersecurity testing and evaluation in accordance with the Boeing 
approved CTP and CTD. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-76.45 – Cybersecurity Test Plan (CTP) 
 Data Item E-76.46 – Cybersecurity Test Description (CTD) 
 Data Item E-76.47 – Cybersecurity Test Results (CTR) 
If required, on a separate purchase contract, Boeing may require the Supplier to support Boeing 
cybersecurity testing of the Supplier’s delivered Product(s) and recommend corrective actions if 
issues are identified."""})
    
    # Validation and Verification

    memory.save_context({"input": """Section: Requirement Verification Matrix (RVM) 
The Supplier shall develop a Requirements Verification and Validation Plan, including a 
Requirements Verification Matrix (RVM) containing a cross reference that correlates each 
requirement in the Specification with the verification methods used (inspection, analysis, 
demonstration, or test) and the test phase during which the verification will occur. The Supplier 
shall integrate the RVM with the System Architecture Model. 
Where a Supplier’s previously qualified/certified solution has been identified for the program, the 
Supplier shall perform a gap analysis and include in the RVM to identify any requirement 
differences from this SSOW and Specification.
The Supplier shall treat each requirement invoked by the Specification from other specifications 
or reference documents in the same manner as the requirements found directly in the 
Specification. The Supplier may group requirements from an invoked specification or reference 
document as a single item in the matrix if the requirements fit within the same test method and 
test phase. The RVM shall be an integral part of Qualification Test Procedures (QTP) and 
Qualification Test Report and identify the corresponding documentation which substantiates 
qualification. 
The Supplier shall ensure that data included in the RVM is in accordance with DO-178 Section 
11.21 for software and DO-254 Section 10.4.1 for firmware. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-59.55 – Requirements Verification and Validation Plan"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-59.55 – Requirements Verification and Validation Plan"""})
    
    memory.save_context({"input": """Section: Analysis
If qualification of the equipment is by analysis, the Supplier shall submit an analysis report for 
qualification prior to the beginning of preparation of the qualification test procedures in 
accordance with the SDRL. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-59.01 – Report of Requirements Verification by Analysis"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-59.01 – Report of Requirements Verification by Analysis"""})
    
    memory.save_context({"input": """Section: Similarity 
If qualification results are available for items that are similar, the Supplier shall analyze the 
configuration, application and qualification criteria in the Specification to determine if the item is 
similar or identical in design, manufacturing process, and quality. If the Supplier proposes to 
qualify the equipment by similarity, the Supplier shall submit a similarity report for qualification 
prior to the beginning of preparation of the qualification test procedures in accordance with the 
SDRL. The similarity report shall document how the parts are similar and provide the similar-to 
verification data. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-59.02 – Similarity Report for Qualification Tests"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-59.02 – Similarity Report for Qualification Tests"""})
    
    memory.save_context({"input": """Section: Qualification Testing 
The Supplier shall prepare an overall system level Qualification Test Plan which defines and 
references all individual Qualification Test Plans that frame the full qualification approach. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-59.08 – Qualification Test Plan"""},
{"output": """Exception. NAI does not agree to generate Data Item E-59.08 – Qualification Test Plan. Such 
information is redundant and found in Data Item E-59.09."""})
    
    memory.save_context({"input": """Section: Safety of Flight Qualification Testing 
The Supplier shall develop a Qualification Test Procedure (QTP) that documents all necessary 
test procedures to meet the qualification requirements defined in the Specification. It is preferable 
that the Supplier include qualification procedures for Safety of Flight and Full Qualification in the 
initial submittal. At a minimum, however, the Supplier shall submit Safety of Flight Qualification 
Test Procedures for approval in the initial submittal and submit Full Qualification Test 
Procedures in accordance with the requirements in the Full Qualification Testing section of this 
SSOW. 
The Supplier shall conduct Safety of Flight testing defined by the Specification, the Boeing 
approved QTP, and this SSOW on production representative hardware to demonstrate the 
Supplier's equipment satisfies the design and performance requirements established for the 
equipment for Safety of Flight. If failures occur prior to meeting this minimum requirement, the 
Supplier shall perform failure analysis and testing, as required and in accordance with the failure 
reporting section of this SSOW, and achieve minimum qualification. 
The Supplier shall submit a Safety of Flight Qualification Report for approval that contains the 
verification data showing the unit meets the Safety of Flight requirements. 
The Supplier shall submit the following data item(s) in accordance with the SDRL (Note, the 
Supplier shall identify each document on the title page as being for Safety of Flight): 
 Data Item E-59.09 – Qualification Test Procedure (QTP) 
 Data Item E-59.11 – Qualification Test Report """},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-59.09 – Qualification Test Procedure (QTP)
• Data Item E-59.11 – Qualification Test Report"""})
    
    memory.save_context({"input": """Section: Full Qualification Testing 
If the initial submittal of the QTP did not document Full Qualification then the Supplier shall 
update the QTP with all necessary test procedures to meet the Full Qualification requirements 
defined in the Specification. 
The Supplier shall conduct Full Qualification testing in accordance with the Boeing approved 
QTP on production representative hardware to demonstrate the Supplier's equipment satisfies the 
design and performance requirements established for the equipment by the Specification. 
The Supplier shall provide Boeing with a final qualification report which encompasses all 
qualification activity. The Supplier may reference formally submitted data items rather than 
resubmitting. The report should be a comprehensive compiling of various analysis and test 
activities performed for qualification under the contract. 
After qualification is completed, any Supplier-initiated changes to components are subject to be 
re-qualified per the Specification and is the responsibility of the Supplier. Changes include but 
are not limited to using different suppliers or manufacturers for components, changes in 
manufacturing facilities, and or manufacturing processes. The Supplier shall submit all changes to 
Boeing in accordance with the Change Management section herein. All Supplier changes 
submitted to Boeing shall address any qualification testing that is affected by the change.
The Supplier shall positively identify and control hardware subjected to qualification test 
requirements. The Supplier shall not deliver qualification test hardware to Boeing unless 
specifically directed by the Boeing PA. The Supplier shall hold all test samples until authority to 
refurbish, or authority to scrap has been granted by Boeing. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-59.09 – Qualification Test Procedure (QTP) 
 Data Item E-59.11 – Qualification Test Report-Qualification Test Report """},
{"output": """NAI plans to cover the entirety of Qualification Testing within Data Item E-59.09. This 
document will contain a matrix of the tests, outlining the ones required for Safety of Flight. This 
subset will be jointly developed with Boeing, if not directly provided as part of the CIDS."""})
    
    memory.save_context({"input": """Section: Software and Firmware Formal Testing 
The Supplier shall perform formal software and firmware verification to the requirements defined 
in the Specification, DO-178, and DO-254, and to the level of criticality of the Boeing identified 
Design Assurance Level (DAL). Boeing may delegate witness authority to Supplier Software 
Quality Assurance (SQA). The Supplier shall document test results in the Software Test Report 
(STR) and Hardware Test Results. The Supplier shall obtain Boeing approval of the Software 
Test Description (STD) and Hardware Test Procedures prior to conducting verification testing. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-77.24 – Hardware Verification Plan 
 Data Item E-77.43 – Hardware Test Procedures 
 Data Item E-77.44 – Hardware Test Results 
 Data Item E-78.07 – Software Test Plan (STP) 
 Data Item E-78.08 – Software Test Description (STD) 
 Data Item E-78.09 – Software Test Report (STR) """},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-77.24 – Hardware Verification Plan
• Data Item E-77.43 – Hardware Test Procedures
• Data Item E-77.44 – Hardware Test Results
• Data Item E-78.07 – Software Test Plan (STP)
• Data Item E-78.08 – Software Test Description (STD)
• Data Item E-78.09 – Software Test Report (STR"""})
    
    memory.save_context({"input": """Section: Electromagnetic Effects (EME) Control 
The Supplier shall develop an Electromagnetic Interference (EMI) Control Plan documenting the 
EMI Control Program describing design procedures and techniques for control of EMI in 
accordance with MIL-STD-461. 
The Suppler shall perform Electromagnetic Environmental Effects (E3) tests to verify compliance 
with the E3 requirements in accordance with MIL-STD-461, as stated in the Specification. The 
Supplier shall start tests only after the Test Procedures are approved by Boeing and notify Boeing 
one week prior to the start of all E3 testing. Boeing reserves the right to witness any and all E3 
testing. 
For any reused, off-the-shelf, or non-developmental hardware, the Supplier may provide existing 
electromagnetic qualification test procedures and reports. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-80.04 – Electromagnetic Interference (EMI) Control Plan 
 Data Item E-80.05 - Electromagnetic Qualification Test Procedure 
 Data Item E-80.06 - Electromagnetic Qualification Test Report"""},
{"output": """Exception. NAI does not agree to generate Data Item E-80.04 – Electromagnetic Interference 
(EMI) Control Plan. Such information is redundant and found in Data Item E-80.05.
NAI agrees to generate and deliver the following data items:
• Data Item E-80.05 - Electromagnetic Qualification Test Procedure
• Data Item E-80.06 - Electromagnetic Qualification Test Report"""})
    
    memory.save_context({"input": """Section: Test Notification 
The Supplier shall provide the Boeing PA and Technical POC with initial notification at least 
thirty (30) days prior to the start of any verification test and final notification at least seven (7) 
days prior to the start of any verification test."""},
{"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Test Witnessing 
The Supplier shall provide access to Boeing and/or Boeing Customer representatives 
accompanying Boeing to review the procedures and the test environment. Boeing and/or the 
Boeing Customer may send representatives to witness the Supplier’s test."""},
{"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Test Unit 
Boeing Engineering may identify certain deliverable units as "Test Units". These units may not 
be fully compliant to the contract requirements, but are usable as Boeing integration lab units. 
Test Units will be identified by Boeing Engineering via a Test Unit Release (TUR), which will 
identify the configuration of the Test Unit needed. The TUR will identify the allowable 
exceptions to the contractual engineering requirements, the quantity of Test Units, and any 
special requirements for the Test Units. The Supplier shall apply visible adhesive tape or painted 
stripe of orange color to the Test Units (1 inch wide). The Supplier shall apply a unique part 
number to the Test Unit(s) to signify Test Unit. """},
{"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Acceptance Testing 
The Supplier shall develop an Acceptance Test Procedure (ATP). If the Supplier intends to use 
automated testing, the Supplier shall document the configuration of software used to perform 
automated acceptance tests as part of the ATP. 
The Supplier shall ensure the criteria included in the ATP is in accordance with DO-178 for 
software and DO-254 for firmware. 
The Supplier shall submit all revisions to the ATP, including configuration changes for automated 
testing, prior to use for any formal acceptance or qualification tests. 
The Supplier shall perform acceptance testing on all units used for qualification testing in 
addition to all delivered equipment in the final assembled condition in accordance with the ATP, 
Specification, and this SSOW. 
The Supplier shall not commence testing prior to receipt of Boeing final approval of the test 
procedure unless otherwise directed in writing by Boeing. 
If the Supplier intends to test individual subassemblies, the Supplier shall submit that 
subassembly ATP to Boeing for approval. 
If the Supplier intends to have a sub-supplier manufacture a subassembly, the sub-assembly shall 
be ATP tested. After the sub-supplier ATP is approved by the Supplier, the Supplier shall submit 
the subassembly ATP to Boeing for Approval. The sub-supplier shall not commence testing prior 
to receipt of Boeing final approval of the ATP unless otherwise directed in writing by Boeing. 
The Supplier shall retain all acceptance test records and make available to Boeing upon Boeing 
request.
The Supplier shall notify Boeing of failures in accordance with the requirements outlined in the 
Failure Reporting section of this SSOW. Boeing may request the informal submittal of the 
relevant Acceptance Test Record. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-59.05 – Acceptance Test Procedure (ATP) 
 Data Item E-59.06 – Acceptance Test Records """},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-59.05 – Acceptance Test Procedure (ATP)
• Data Item E-59.06 – Acceptance Test Records"""})

    # Product Support

    memory.save_context({"input": """Section: Logistics Support Data 
The Supplier shall prepare Logistics Support Data with all the necessary operation and 
maintenance data for components being procured sufficient for Boeing to use in developing 
Logistics Support Analysis Records and Technical Manuals. The Supplier shall include any 
existing documentation (e.g., interface control documentation, drawings, solid models, etc.) for 
the system in the format the documentation was originally developed. 
The Supplier shall include a list of all support equipment including all common or peculiar 
support equipment, special tools, and special test and/or inspection equipment. 
For Supplier Line Replaceable Units (LRUs) with a recurring acquisition cost greater than 
$10,000 or with a MTBF lower than 10,000 flight hours, the Supplier shall identify if the item is 
repairable. If an item is repairable, then the Supplier shall prepare Level of Repair Analysis 
(LORA) data, detailed to the Shop Replaceable Unit level, sufficient for Boeing to perform 
economic analysis of the Suppliers recommended maintenance concept. If an item is not 
repairable, no LORA data is needed. 
The Supplier shall include a recommended spares parts list for Organizational Level of 
Maintenance (O-LOM), as applicable. 
If the Supplier has previously submitted Logistics Support Data, then the Supplier shall update 
the existing, approved submittals and resubmit in accordance with SDRL Data Item L-23. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item L-23– Logistics Support Data"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item L-23– Logistics Support Data"""})

    memory.save_context({"input": """Section: Technical Manuals 
The Supplier shall prepare Technical Manual Source Data in accordance with SDRL data item L23. If the information exists from a previously approved Supplier submittal, then the Supplier 
shall update the existing, approved data and submit in accordance with SDRL Data Item L-23."""},
{"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Provisioning Technical Documentation 
The Supplier shall prepare Provisioning Technical Documentation, for all Supplier provided 
items for O-LOM including peculiar and common support equipment and special test and/or 
inspection equipment. Boeing will use the SDRL Data Item E-73.01 for drawings and/or models 
as referenced herein for provisioning analysis.
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item L-57– Provisioning Technical Documentation """},
{"output": """Exception. No special peculiar or common test equipment, special test, or inspection equipment required."""})
    
    memory.save_context({"input": """Section: Spares and Repairs 
The Supplier shall provide repair and/or replacement services for repairable parts within the 
expected turnaround time needed to allow the flight test program to proceed without adverse 
impacts from Supplier equipment. The Supplier shall certify that all repaired parts furnished have 
been repaired or overhauled in accordance with authorized procedures, as identified in 
appropriate repair manuals or Supplier’s internal processes. If returned items are determined to be 
Beyond Economical Repair (BER)/Beyond Physical Repair (BPR), where BER guideline is 70% 
of replacement cost, then the Supplier shall notify Boeing. The Supplier shall keep and maintain 
inspection, test, and repair records and provide the records to Boeing when requested."""},
{"output": """NAI agrees with the information provided in this section of the SSOW"""})

    # Quality Assurance

    memory.save_context({"input": """Section: Quality Assurance (QA) 
Quality requirements are defined by the Terms and Conditions specified in the applicable PC. 
Boeing will provide supplemental notes to the purchase order to provide specific direction and 
requirements for each order placed at the Supplier. 
The Supplier’s Quality Management System is defined as follows: 
a) The Supplier and Sub-tier Suppliers shall maintain a quality management system that is 
compliant with D6-82479, Boeing Quality Management System Requirements for 
Suppliers; OR 
b) In lieu of compliance with D6-82479, the Supplier and their Sub-tier Suppliers shall 
establish, implement, and maintain a quality management system compliant with SAE 
AS9100; OR 
c) Show compliance to an equivalent international standard assured by an accredited 
registrar. """},
{"output": """NAI agrees with the quality requirements outlined in this section of the SSOW, inclusive of 
subcontractors. NAI’s latest ISO:9001 certificate is displayed below for reference."""})
    
    memory.save_context({"input": """Section: Software Quality Assurance (SQA) 
The Supplier shall establish and implement a Software Quality Assurance (SQA) Program in 
accordance with its standard policies, procedures, and processes, as well as with their Quality 
Management System (QMS). 
The SQA Program shall apply to new and modified software identified as deliverable and nondeliverable software essential for qualification, generation, reproduction and/or acceptance of 
deliverable software, hardware and/or systems. 
For each software deliverable item, the Supplier SQA representative shall conduct a Software 
Conformity Review (SCR), or equivalent. The Supplier shall invite Boeing to witness the 
Supplier SCR, and Boeing may audit the SCR if not in attendance. Boeing SQA may provide the 
applicable checklist for guidance. 
For Software that is delivered as an end item or as a part of a deliverable software-supported 
product that is either designed or modified to meet Boeing requirements, the Supplier shall 
demonstrate a minimum compliance with requirements of Boeing Quality Management System 
(BQMS) D6-82479, Addendum 2 (SAE AS9115) and DO-178 as part of the Software Quality 
Assurance Plan (SQAP). The requirements of AS9115 are not applicable to COTS software 
installed in deliverable products. Software modified to Boeing requirements is not considered 
COTS. The requirements of AS9115 are also not applicable to product acceptance software and 
software used in automated systems, except as used to verify developed software. 
The Supplier shall perform product and process compliance audits of the activities defined in its 
Software Development Plan (SDP) for new and modified software development and 
management. The Supplier shall document the results of these audits in software quality records, 
including audit reports, audit checklists, and related audit artifacts. In addition, the SQAP shall 
include provisions for periodic evaluations of the Supplier software QA activities by Boeing. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item Q-03.07 – Software Quality Assurance Plan (SQAP)
 Data Item Q-03.13 – Software Quality Audit Report """},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item Q-03.07 – Software Quality Assurance Plan (SQAP)
• Data Item Q-03.13 – Software Quality Audit Report"""})
    
    # System Safety

    memory.save_context({"input": """Section: System Safety Program 
The Supplier shall execute a System Safety Program following the guidelines of MIL-STD-882, 
SAE ARP 4754, and SAE ARP 4761 as applicable in order to identify, classify, and mitigate 
safety hazards and ensure safety is integrated into the design of the equipment. The Supplier shall 
maintain hazards in a controlled hazard tracking system. If the Supplier executes a Fault Tree 
Analysis (FTA), the Supplier shall use a commercial FTA program with a format importable into 
PTC Windchill Quality Solutions and submit as part of SDRL Data Item E-63.15. FTA diagram 
symbols shall conform to SAE ARP 4761 Figure D2, “Fault Tree Symbols”. 
The Supplier shall prepare a System Safety Program Plan (SSPP) that documents and 
substantiates that the system design includes the necessary mitigations to reduce and maintain 
risk to a level of medium or lower as defined by MIL-STD-882. 
The Supplier shall describe tasking to provide, implement, and maintain a system safety program 
to evaluate hardware and software. The Supplier shall also document a Safety Critical Function 
process and include any relevant lesson(s) learned from past mishap experiences. The Supplier 
shall include safety criteria and methodology used to classify and rank hazards, including any 
assumptions on which the criteria or methodologies were based. 
The Supplier shall participate in and support, as necessary, TIMs with Boeing as well as System 
Safety Working Groups (SSWG) to clarify potential safety issues and associated mitigations. 
The Supplier shall continue to follow the System Safety Program Plan (SSPP) in conjunction 
with any Boeing or Supplier initiated changes that affect the baseline system. 
The Supplier shall submit the following data item(s) in accordance with the SDRL:
 Data Item E-63.10 – System Safety Program Plan (SSPP) """},
{"output": """Exception. This is a system level function that should be partially flowed down to the supplier’s 
requirements. NAI will provide minimal support on this and focus its energy on the SAR."""})
    
    memory.save_context({"input": """Section: Safety Assessment Report (SAR) 
The Supplier shall prepare a Safety Assessment Report (SAR) in accordance with MIL-STD-882 
to provide a comprehensive evaluation of all safety features of the hardware, software (if 
applicable), and system design including support equipment, if applicable. The Supplier shall 
ensure the report covers the entirety of the lifecycle of the system, such as operation, 
maintenance, storage, transportation, training, and disposal. As part of the SAR, the Supplier shall 
incorporate or reference any relevant findings from the FMECA Report and/or Qualification Test 
Report. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-63.15 – Safety Assessment Report (SAR)"""},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-63.15 – Safety Assessment Report (SAR)"""})
    
    memory.save_context({"input": """Section: Hazard Analysis 
The Supplier shall perform hazard analysis and document as part of SDRL Data Item E-63.15. 
The Supplier shall follow MIL-STD-882, paragraph 4.3.4 to identify and document risk 
mitigation measures for satisfying system safety requirements and reducing risks. The Supplier 
shall identify hazards that require resolution as hazard analyses are performed. 
The Supplier shall examine the system shortly after the concept definition effort begins and shall 
compile a Preliminary Hazard List (PHL) identifying possible hazards that may be inherent in the 
concept and their associated mishap potential. The PHL effort shall include a review of safety 
experience on similar systems, including mishap/incident hazard tracking logs (if accessible), 
safety lessons learned, etc., to identify possible hazards and their mishap risks. The Supplier shall 
reference sources of a hazard found in this review in the PHL. The PHL shall meet the intent of 
MIL-STD-882 Task 201 and be provided as part of SDRL Data Item P-02.15 for SRR. The 
Supplier shall further investigate selected hazards or hazardous characteristics identified in the 
PHL as directed by Boeing to determine their significance."""},
{"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Hazardous Material (HAZMAT) 
The Supplier shall implement a Hazardous Materials Management Program (HMMP) using NAS 
411 as a guide. The Supplier shall identify, evaluate, and eliminate or minimize any hazardous 
material (HAZMAT) risks consistent with program cost, schedule, and performance 
requirements. HAZMATs shall include prohibited, restricted, and tracked substances as provided 
in NAS 411-1 Hazardous Material Target List (HMTL). The Supplier shall not use Hexavalent 
Chromium in the delivered product without the expressed contractual authorization of Boeing. 
The Supplier shall submit the following data item(s) in accordance with SDRL: 
 Data Item E-54.16 – Hazardous Materials Management Program (HMMP) Report """},
{"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-54.16 – Hazardous Materials Management Program (HMMP) Report"""})
    
    memory.save_context({"input": """Section: Software/Firmware Safety 
The Supplier shall implement a software and/or firmware safety program in accordance with DO178, DO-254, and ARP 4754 to ensure all software and firmware satisfy the identified safety 
requirements and level of criticality of the Boeing identified Design Assurance Level (DAL). The 
Supplier shall use DoD Joint Software Systems Safety Engineering Handbook to conduct the 
associated level of rigor tasks. The intent of the software safety program is to provide for: 
1. Assessment and identification of safety critical software 
2. Development and maintenance of safety critical software requirements 
3. Developing a software architecture strategy to minimize hazardous condition safety risk, 
including selection of software components such as OS 
4. Selection of programming language, compilers, compiler options and programming 
standards used for reducing the probability of induced software errors resulting in 
hazardous conditions 
5. Software verification techniques to reduce the probability of errors 
6. The use of independence in the evaluation of software products 
The Supplier shall conduct a software requirements hazard analysis in accordance with MILSTD-882 Task 203 and include the results as part of the Safety Assessment Report SDRL Data 
Item E-63.15."""},
{"output": """NAI agrees with the information provided in this section of the SSOW. This task will require a 
considerate amount of effort on Boeing engineering’s side, particularly in terms of flowed down 
requirement analysis"""})
    
    memory.save_context({"input": """Section: Through-Life Safety Support 
The Supplier shall support investigations and provide data in case of failures, near-mishaps, or 
mishaps of the system in the field, once in operation, as defined in MIL-STD-882. The Supplier 
shall provide any relevant data from on-board memory retention systems in an open-source 
format; provide relevant data consisting of, but not limited to the following: 
 Engineering Investigation data 
 Test stand data 
 Unit build-up/ATP data 
 Component sourcing and supplier data 
The Supplier shall have a process to maintain an acceptable level of risk once the system is 
operating in the fleet and to conduct reviews of potential safety issues in order to support the 
Boeing Safety Review Board. The Supplier shall present the details of this process at PDR and 
submit as part of SDRL Data Item P-02.15."""},
{"output": """NAI agrees with the information provided in this section of the SSOW, limiting the scope to the 
period of performance of a potential production or support contract"""})
    

    

# NORTHROP GRUMMAN RESPONSES (ALL)

    # Technical Tasks

    memory.save_context({"input": """Section: Environmental Qualification Testing, PIU
The Supplier shall conduct environmental qualification testing in accordance 
with C72-1100-110 MQ-8C Environmental DRB. For reference, the PIU will be 
installed in zone 2 Main Avionics Bay as shown in Figure 4-1 Fire Scout 
Environmental Zones as shown in the DRB.
The Supplier shall perform ESS Testing on the planned test unit prior to starting 
hardware qualification testing. The Supplier shall perform qualification testing 
as detailed below on the PIU, an NIU3A configured with modules SC3, DT5,
EM1 and 50ms power hold-up installed.
The supplier shall permanently mark the qualification test unit with a solid red 
stripe and the words “NOT FOR FLIGHT” at the completion of qualification 
testing.
Existing NIU qualification data was reviewed, and the following delta 
qualification is required for the PIU:
Environmental: Operating Altitude, Non-Operating Altitude, Temperature, 
Temperature Shock, Humidity, Fungus, Salt Fog, Sand and Dust, 
Acceleration, Vibration, Shock.
Qualification by Test: 
• Operating Altitude. See C72-1100-110A, section 5.1.1
• Non-Operating Altitude. See C72-1100-110A, section 5.1.2
• Temperature. See C72-1100-110A, section 5.2.1
• Non-Operating Temperature. See C72-1100-110A, section 5.2.4
• Temperature Shock. See C72-1100-110A, section 5.2.3
• Vibration Zone 2. See C72-1100-110A, section 5.9.2
• Shock. See C72-1100-110A, section 5.10
NOTE: The heat sink/mounting plate (either NAII or CFE provided) should be 
installed and part of the unit under test assembly for those environments 
listed above under “Qualification by Test”.
Qualification by Analysis or Similarity:
• Humidity. See C72-1100-110A, section 5.4
• Fungus. See C72-1100-110A, section 5.5
• Salt Fog. See C72-1100-110A, section 5.6
• Sand and Dust. See C72-1100-110A, section 5.7
• Acceleration Zone 4. See C72-1100-110A, section 5.8.1
NOTE: The supplier may use existing test data from other units the supplier 
deems as similar enough in design and make a “Qualification by Similarity” 
claim. Such claims will need to be supported in the final report by the 
supplier. If the supplier feels that any environments listed in this section 
cannot be supported by analysis or similarity, supplier shall recommend 
qualification by test.
The Supplier shall prepare an Environmental Qualification Test Procedure for 
the PIU which shall be delivered in accordance with SDRL S061A, 
Qualification Test Procedure.
At the conclusion of testing, the Supplier shall prepare an Environmental 
Qualification Test Report for the PIU and deliver it in accordance with SDRL 
S062, Qualification Test Report. The test report should discuss any 
experienced test failures as well, see SDRL S103 below.
The Supplier shall prepare a Failure Summary & Analysis Report for each 
failure or failure indication that occurs or is discovered during tests that are 
conducted by, or under the cognizance of, the Supplier on the PIU and IDS. 
Failure Summary and Analysis Reports for the Equipment shall be delivered 
in accordance with SDRL S103, Failure Summary & Analysis Report.
The Buyer and Government may witness the qualification testing of the 
Equipment at the Supplier’s facility, or subcontractor, on a non-interference 
basis and will not impact the manufacturing operation and schedule."""},
{"output": """NAI understands and agrees with the PIU testing guidelines outlined in this section of the 
SOW. Options for cost and schedule reductions may be found in section 6 of this document.
Noted: After existing NIU family qualification data was reviewed, the following is required:
Qualification by Test:
• Operating Altitude. See C72-1100-110A, section 5.1.1
• Non-Operating Altitude. See C72-1100-110A, section 5.1.2
• Temperature. See C72-1100-110A, section 5.2.1
• Non-Operating Temperature. See C72-1100-110A, section 5.2.4
• Temperature Shock. See C72-1100-110A, section 5.2.3
• Vibration Zone 2. See C72-1100-110A, section 5.9.2
• Shock. See C72-1100-110A, section 5.10
Noted: NAI is expecting that any heat sink/mounting plate will be CFE."""})
    
    memory.save_context({"input": """Environmental Qualification Testing, IDS (OPTION)
The Supplier shall conduct environmental qualification testing in accordance 
with C72-1100-110 MQ-8C Environmental DRB. For reference, the IDS will be 
installed in zone 1 Payload Bay, as shown in Figure 4-1 Fire Scout 
Environmental Zones as shown in the DRB.
The Supplier shall perform qualification testing as detailed below on the IDS, 
an NIU3A configured with module FM9 and 50ms power hold-up installed.
The supplier shall permanently mark the qualification test unit with a solid red 
stripe and the words “NOT FOR FLIGHT” at the completion of qualification 
testing.
Existing NIU qualification data was reviewed, and the following delta 
qualification is required for the IDS:
Environmental: Operating Altitude, Non-Operating Altitude, Temperature, 
Temperature Shock, Humidity, Fungus, Salt Fog, Sand and Dust, 
Acceleration, Vibration, Shock.
Qualification by Test:
• Operating Altitude. See C72-1100-110A, section 5.1.1
• Non-Operating Altitude. See C72-1100-110A, section 5.1.2
• Temperature. See C72-1100-110A, section 5.2.1
• Non-Operating Temperature. See C72-1100-110A, section 5.2.4
• Temperature Shock. See C72-1100-110A, section 5.2.3
• Vibration Zone 2. See C72-1100-110A, section 5.9.2
• Shock. See C72-1100-110A, section 5.10
NOTE: The NGC supplied heat sink/mounting plate (either NAII or CFE 
provided) should be installed and part of the unit under test assembly for 
those environments listed above under “Qualification by Test”.
Qualification by Analysis or Similarity:
• Humidity. See C72-1100-110A, section 5.4
• Fungus. See C72-1100-110A, section 5.5
• Salt Fog. See C72-1100-110A, section 5.6
• Sand and Dust. See C72-1100-110A, section 5.7
• Acceleration Zone 4. See C72-1100-110A, section 5.8.1
NOTE: The supplier may use existing test data from other units the supplier 
deems as similar enough in design and make a “Qualification by Similarity” 
claim. Such claims will need to be supported in the final report by the 
supplier. If the supplier feels that any environments listed in this section 
cannot be supported by analysis or similarity, supplier shall recommend 
qualification by test.
The Supplier shall prepare an Environmental Qualification Test Procedure for 
the IDS which shall be delivered in accordance with SDRL S061A, 
Qualification Test Procedure.
At the conclusion of testing, the Supplier shall prepare an Environmental 
Qualification Test Report for the IDS and deliver it in accordance with SDRL 
S062, Qualification Test Report. The test report should discuss any 
experienced test failures as well, see SDRL S103 below.
The Supplier shall prepare a Failure Summary & Analysis Report for each 
failure or failure indication that occurs or is discovered during tests that are 
conducted by, or under the cognizance of, the Supplier on the PIU and IDS. 
Failure Summary and Analysis Reports for the Equipment shall be delivered 
in accordance with SDRL S103, Failure Summary & Analysis Report.
The Buyer and Government may witness the qualification testing of the 
Equipment at the Supplier’s facility, or subcontractor, on a non-interference 
basis and will not impact the manufacturing operation and schedule"""},
{"output": """NAI understands and agrees with the IPS testing guidelines outlined in this section of the 
SOW. Options for cost and schedule reductions may be found in section 6 of this document.
Noted: IPS Environmental Qualification Testing is being considered “optional” as the IPS
configuration is actually a ‘subset’ and variation of the hardware fitted in the PIU.
Noted: NAI is expecting that any required heat sink/mounting plate will be CFE"""})
    
    memory.save_context({"input": """Section: EMI Qualification Testing, PIU
The Supplier shall conduct EMI qualification testing in accordance with C72-
1100-110 MQ-8C Environmental DRB.
The Supplier shall perform qualification testing as detailed below on the PIU, 
an NIU3A configured with smart function modules SC3, DT5 and EM1 and 
50ms power hold-up installed.
The supplier shall permanently mark the qualification test unit with a solid red 
stripe and the words “NOT FOR FLIGHT” at the completion of qualification 
testing.
Existing NIU qualification data was reviewed, and the following delta 
qualification is required:
EMI: CE102, CS101, CS114, CS115, CS116, RE102, RS103 (1,2), MIL-STD704.
Qualification by Test: 
• CE102. See C72-1100-110A, section 5.11
• CS101. See C72-1100-110A, section 5.11
• CS114. See C72-1100-110A, section 5.11
• CS115. See C72-1100-110A, section 5.11
• CS116. See C72-1100-110A, section 5.11
• RE102. See C72-1100-110A, section 5.11
• RS103 (1,2). See C72-1100-110A, section 5.11
• MIL-STD-704. See C72-1100-110A, section 5.11 (Note: since the NIU is 
outfitted with the 50ms power hold-up option, it is expected that the NIU 
will operate normally during the 704 power interrupt testing)
The Supplier shall prepare an EMI Qualification Test Procedure for the PIU 
which shall be delivered in accordance with SDRL S061A, Qualification Test 
Procedure.
At the conclusion of testing, the Supplier shall prepare an EMI Qualification 
Test Report for the PIU and deliver it in accordance with SDRL S062, 
Qualification Test Report. The test report should discuss any experienced 
test failures as well, see SDRL S103 below.
The Supplier shall prepare a Failure Summary & Analysis Report for each 
failure or failure indication that occurs or is discovered during tests that are 
conducted by, or under the cognizance of, the Supplier on the PIU. Failure 
Summary and Analysis Reports for the Equipment shall be delivered in 
accordance with SDRL S103, Failure Summary & Analysis Report.
The Buyer and Government may witness the qualification testing of the 
Equipment at the Supplier’s facility, or subcontractor, on a non-interference 
basis and will not impact the manufacturing operation and schedule."""},
{"output": """NAI understands and agrees with the PIU testing guidelines outlined in this section of the 
SOW. NAI strongly recommends coordination of EMI cabling right after kickoff. Options for 
cost and schedule reductions may be found in section 7 of this document.
Noted: After existing NIU family qualification data was reviewed, the following is required:
Qualification by Test:
Qualification by Test:
• CE102. See C72-1100-110A, section 5.11
• CS101. See C72-1100-110A, section 5.11
• CS114. See C72-1100-110A, section 5.11
• CS115. See C72-1100-110A, section 5.11
• CS116. See C72-1100-110A, section 5.11
• RE102. See C72-1100-110A, section 5.11
• RS103 (1,2). See C72-1100-110A, section 5.11
• MIL-STD-704. See C72-1100-110A, section 5.11 
(Note: since the NIU is outfitted with the 50ms power hold-up option, it is expected that the 
NIU will operate normally during the 704-power interrupt testing).
Clarified: NIU is expected to operate and ride through any MIL-STD-704 testing with power 
interruption duration < 50ms."""})
    
    memory.save_context({"input": """Section: EMI Qualification Testing, IDS (OPTION)
The Supplier shall conduct EMI qualification testing in accordance with C72-
1100-110 MQ-8C Environmental DRB.
The Supplier shall perform qualification testing as detailed below on the IDS, 
an NIU3A configured with module FM9 and 50ms power hold-up installed.
The supplier shall permanently mark the qualification test unit with a solid red 
stripe and the words “NOT FOR FLIGHT” at the completion of qualification 
testing.
Existing NIU qualification data was reviewed, and the following delta 
qualification is required:
EMI: CE102, CS101, CS114, CS115, CS116, RE102, RS103 (1,2), MIL-STD704.
Qualification by Test: 
• CE102. See C72-1100-110A, section 5.11
• CS101. See C72-1100-110A, section 5.11
• CS114. See C72-1100-110A, section 5.11
• CS115. See C72-1100-110A, section 5.11
• CS116. See C72-1100-110A, section 5.11
• RE102. See C72-1100-110A, section 5.11
• RS103 (1,2). See C72-1100-110A, section 5.11
• MIL-STD-704. See C72-1100-110A, section 5.11 (Note: since the NIU is 
outfitted with the 50ms power hold-up option, it is expected that the NIU 
will operate normally during the 704 power interrupt testing)
The Supplier shall prepare an EMI Qualification Test Procedure for the IDS
which shall be delivered in accordance with SDRL S061A, Qualification Test 
Procedure.
At the conclusion of testing, the Supplier shall prepare an EMI Qualification 
Test Report for the IDS and deliver it in accordance with SDRL S062, 
Qualification Test Report. The test report should discuss any experienced 
test failures as well, see SDRL S103 below.
The Supplier shall prepare a Failure Summary & Analysis Report for each 
failure or failure indication that occurs or is discovered during tests that are 
conducted by, or under the cognizance of, the Supplier on the PIU. Failure 
Summary and Analysis Reports for the Equipment shall be delivered in 
accordance with SDRL S103, Failure Summary & Analysis Report.
The Buyer and Government may witness the qualification testing of the 
Equipment at the Supplier’s facility, or subcontractor, on a non-interference 
basis and will not impact the manufacturing operation and schedule."""},
{"output": """NAI understands and agrees with the IPS testing guidelines outlined in this section of the 
SOW. NAI strongly recommends coordination of EMI cabling right after kickoff. Options for 
cost and schedule reductions may be found in section 7 of this document.
Noted: IPS EMI Qualification Testing is being considered “optional” as the IPS configuration 
is actually a ‘subset’ and variation of the hardware fitted in the PIU."""})
    
    memory.save_context({"input": """Section: Secure and Measured Boot Development
The Supplier shall enable the NIU3A device’s capability as described in this 
section below.
The Supplier shall perform requirement analysis, decomposition, and 
allocation from source requirements to the lowest Configuration Item. The 
Supplier shall maintain traceability through all systems, software, and test 
documentation. The Supplier shall deliver a Requirements Traceability 
Document demonstrating this traceability in accordance with SDRL S246, 
Requirements Traceability Document.
The Supplier shall generate Software Qualification Verification Plans and 
Procedures, and a Software Qualification Verification Report. The Supplier 
shall deliver a Software Qualification Plan and Procedure and the Verification 
Report in accordance with SDRL S061A, Qualification Test Procedure and 
SDRL S062, Qualification Test Report.
The Supplier shall create sequence diagrams of the Secure and Measured 
Boot implementation and label them to show which physical component(s) will 
be utilized to meet each of the applicable requirements. The diagrams will 
include the data transfer, the timing, and the sequence order between 
components in the Secure and Measured Boot implementation. The Supplier 
shall provide notional data-flow paths and steps of how software and firmware 
will be loaded and monitored to meet security requirements. The Supplier 
shall include these diagrams and data flow information in the TIM #1 
presentation and deliver in accordance with SDRL S092, Conference Meeting 
Minutes."""},
{"output": """NAI is planning to implement the “security requirements” with TPM and Xilinx Zynq 
UltraScale+ (US+) eFUSE only, up to U-boot (for common secure and measured boot) -
initially with PetaLinux following with VxWorks 7.x, as the target local OS.
It is expected that the PetaLinux sub-effort will provide the basis of the Secure and Measured 
Boot development outline, as initial research finds the Xilinx UltraScale+ and TPM integration 
may be more mature. 
Noted: The VxWorks 7.x sub-effort is expected to be an additional set of development support 
requirements. Support for VxWorks 7.x will require some additional development and 
integration work, including enabling of the SPI interface access to the TPM component, to 
ensure all the software component access is compatible with the industry standard TPM 
command and control library as is identified in the PetaLinux sub-effort support.
Noted: With TPM and US+ eFUSE, BBRAM (and associated batteries) is not required.
Noted: Secure and Measured Boot Development is expected to require NGC and NAI 
collaboration and consensual detail definition on the architecture implementation. 
Noted: Paragraph 3.6 (and associated sub-paragraph requirements) will be addressed and 
handled as a separate software-security implementation integration task effort. The NIU3A 
configurations include:
1. Payload Interface Unit (PIU)
NIU3A-2-SC3DT5EM11417T0H-52
2. Intrusion Protection System (IPS)
NIU3A-2-Z00FM9Z001111T0H-52
The NIU3A “T” part number option ensures that the hardware security capabilities 
(UltraScale+ and TPM) are fitted, with the purpose and intent of providing a path toward the 
security functions implementation as defined within the following requirement sub-paragraphs. 
NAI and NGC will define/work-together through the “-52” definition, which includes the 
eventual functional implementation of the software security “update/upgrade” task effort.
As detailed within the SOW, NAI shall enable the NIU3A capability as described in this 
section to ensure the authenticity, integrity, and confidentiality of hardware, software, 
firmware, and data prior to processing. This secure and measured boot section is applicable to 
both the PIU and IPS.
As detailed within the SOW, NAI shall perform requirement analysis, decomposition, and 
allocation from source requirements to the lowest Configuration Item. NAI shall maintain 
traceability through all systems, software, and test documentation. A Requirements 
Traceability Document shall be delivered demonstrating this traceability, in accordance with:
SDRL S246. 
All items delivered under this effort shall be qualified either by qualification inspections, 
analyses, demonstrations, and tests performed by NAI or a similarity report prepared by NAI 
and agreed to by NGC. NAI shall generate Qualification Verification Plans and Procedures, 
and a Qualification Verification Report. The Qualification Plans and Procedures and the 
Verification Report shall be delivered in accordance with:
SDRL S061A and 
SDRL S062. 
NAI shall create sequence diagrams of the Secure and Measured Boot implementation and 
label them to show which physical component(s) will be utilized to meet each of the applicable 
requirements. The diagrams will include the data transfer, the timing, and the sequence order 
between components in the Secure and Measured Boot implementation. Notional data flow 
paths and steps of how software and firmware will be loaded and monitored to meet security 
requirements shall also be provided. These diagrams and data flow information shall be 
included in the TIM #1 presentation and delivered in accordance with: 
SDRL S092."""})
    
    memory.save_context({"input": """Section: Heat Sink Design (OPTION)
The supplier shall design and qualify a combination heat sink / mounting plate 
to allow the conduction cooled NIU3A to operate at temperatures up to 71C 
without any loss of functionality. The PIU installation location shall be the 
version that drives the design of the heat sink. PIU installation location is in 
the forward faraday cage. Expected airflow is 6 feet per second originating 
from vents on the left side of the trapezoidal side of the faraday cage and
exiting through the top middle of the cage structure The available volume for 
the NIU with heat sink installed is 8.5” L x 6.0” W x 7.5” H.
The seller shall consider additional factors in the heat sink design, including 
weight, maintainability, reliability, human factors, cost and schedule as part of 
the design. Specific details regarding installation requirements to be 
discussed during weekly status meetings.
The heat sink shall be compatible with both the PIU and IDS.
The heat sink design shall be approved by the Buyer prior to manufacture. 
The Supplier shall develop a Technical Data Package (TDP) containing the 
released heat sink drawings and shall deliver in accordance with SDRL S194, 
Technical Data Package"""},
{"output": """Noted: Exception. NAI does not have any insight into the customer system platform installation location(s) or any 
of the physical and environmental constraints and variables to adequately design and qualify a 
combination heat sink / mounting plate to allow the conduction cooled NIU3A to operate at 
ambient air temperatures up to 71ᵒC without any loss of functionality. 
NAI will provide NGC estimated power dissipation, outline and installation drawings, solid 
model volumetric files (.stp) and other basic thermal information for the NIU3A, to assist NGC 
in their efforts for an air-cooled NIU3A heat sink design"""})
    
    memory.save_context({"input": """Section: Software Configuration Management
The Supplier shall maintain strict integrity of the software product (i.e., 
software, firmware and associated documentation) consistent with SAE/GEIAHB-649.
The Supplier shall identify the software configuration at each software 
release, control changes to the configuration, and maintain the integrity and 
traceability of the configurations and include Supplier software configurations."""},
{"output": """NAI agrees to maintain configuration management at each software release, as well as the 
traceability of the configurations."""})
    
    memory.save_context({"input": """Section: Software Interface Design Document (IDD)
The Supplier shall provide a software IDD for the PIU and IDS including the 
added cyber functionality and detailed BIT information and how it can be read 
by user software programs in accordance with DI-IPSC-81436 and submitted 
under SDRL S194, Technical Data Package."""},
{"output": """NAI agrees to generate a Software IDD and include it in SDRL S194 (TDP)."""})
    
    memory.save_context({"input": """Section: Software Version Description (SVD)
The Supplier shall provide a software and firmware SVD for the DPIU 
including the added cyber functionality for each version of either software or 
firmware delivered to Buyer in accordance with DI-IPSC-81442A and 
submitted under SDRL S023A, Software Version Description Document."""},
{"output": """NAI agrees to generate an SVD in accordance with SDRL S023A"""})
    
    memory.save_context({"input": """Section: Software Deliverables
At the completion of the contract, the Supplier shall deliver all Software and 
Firmware executables, installation instructions, and deliverable 
documentation associated with the final release in accordance with SDRL 
S021, Software Product Specification."""},
{"output": """NAI agrees to generate a Software Product Specification, in accordance with SDRL S021"""})
    
    memory.save_context({"input": """Section: Safety Assessment Report
The Supplier shall generate a combined Safety Assessment Report (SAR) 
that follows the guidelines of DI-SAFT-80102C for the PIU and IDS. A
Subsystem Hazard Analysis (SSHA) shall be included as an appendix in this
report. The report shall be delivered in accordance with SDRL S212, Safety 
Assessment Report."""},
{"output": """NAI agrees to generate a Safety Assessment Report, in accordance with SDRL S212. 
Collaboration with NGC engineering early in the effort is strongly recommended to achieve 
proper alignment in terms of safety requirements."""})
    



# Program Management Responses
    
    # Boeing
    
    memory.save_context({"input": """Section: Schedule Requirements 
The Supplier shall identify milestones and activities that will be integrated into the Boeing 
Program Integrated Master Schedule (IMS), including subsequent iterations that would optimize 
the cost, schedule, performance reporting, quality and technical performance for the work scope 
defined by this SSOW and the PC that invokes this SSOW. The Supplier milestones and activities 
shall include all IMS related risks, issues and opportunities relative to the Boeing program work 
scope, the Supplier work scope, and the elements of the program that interface with the Supplier 
work scope. 
The Supplier shall develop an IMS that supports the Boeing Program IMS. 
The Supplier shall, within its scheduling activities, perform critical path analysis, Schedule Risk 
Analysis and develop and maintain a Critical Path Network (CPN). The CPN shall contain the 
end-to-end horizontal sequence of activities required to achieve its product and service 
deliverables. The CPN shall contain the appropriate level of detail to accurately reflect activity 
interrelationships and be a reliable predictor of schedule performance against future milestones. 
Dynamic scheduling of critical elements shall be added as necessary to reflect an accurate 
depiction of the critical path drivers. The Supplier shall participate in and provide inputs to any 
schedule risk analysis. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
     Data Item P-02.14 – Integrated Master Schedule (IMS) 
"""},
                        {"output": """NAI agrees with the contents of this section of the SSOW. NAI agrees to generate and deliver 
the following data items:
• Data Item P-02.14 – Integrated Master Schedule (IMS)"""})
    
    memory.save_context({"input:": """Section: Teleconferences 
The Supplier shall participate in weekly teleconferences at a mutually agreed upon time and day 
for up to (1) one hour each meeting through development to support Boeing program needs.
The Supplier shall prepare program status charts and provide the charts to the Boeing PA and 
Technical POC electronically prior to the scheduled teleconferences to be used as talking points. 
The program status charts should indicate the progress of the work, indicate the status of the 
program and of assigned tasks, indicate status of SDRL data item submittals, inform of existing 
or potential problem areas and the associated risks, and identify any help needed. Boeing will 
establish the format/template at the initial Teleconference. """},
                        {"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Program Management Reviews (PMRs) 
Boeing will develop a standard agenda and a list of Boeing and Boeing Customer representative 
invitees. The Supplier shall issue invitations at least 14 days prior to each meeting. 
The Supplier shall hold Program Management Reviews (PMRs) quarterly commencing after 
notice to proceed. PMRs will typically require WebEx support, but in the event of significant 
program issues the Supplier shall support the PMR at Boeing facilities. 
PMRs and TIMs will be held concurrently when the two meetings are closely scheduled. 
The Supplier shall address significant program accomplishments including schedule, technical 
status, results of analyses and tests, PC status, Risk, Issue, and Opportunity (RI&O) Management, 
data status, PC correspondence status, action items, and help needed. The Supplier shall provide a 
meeting agenda, minutes of the meeting, and administrative services for each formal review. 
The Supplier shall implement an integrated RI&O management process to identify, analyze, 
handle, document, track, and communicate risks, issues, and opportunities as part of the program 
status report using the Department of Defense (DoD) Risk, Issue, and Opportunity Management 
Guide for Defense Acquisition Programs as a guide (http://acqnotes.com/wpcontent/uploads/2017/07/DoD-Risk-Issue-and-Opportunity-Management-Guide-Jan-2017.pdf). 
The Supplier shall present their RI&O management process at the initial TIM and assessment of 
RI&Os at each PMR. 
In addition to the minutes provided in SDRL Data Item P-02.15, the Supplier shall provide 
preliminary minutes of the PMR including action item responsibilities and scheduling of 
resolutions at the conclusion of the meeting to the Boeing Technical POC and the Boeing PA. 
Preliminary handwritten minutes are permissible. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item P-02.15 – Presentation Materials, Agenda, Minutes and Action Item Responses 
for Meetings and Reviews"""},
{"output": """Exception. NAI agrees to provide updates via a variety of ways, namely Schedule, Weekly Calls, 
E-mail and ad-hoc phone calls, in addition to the TIMs and Reviews. NAI respectfully feels that 
this amount of information is more than sufficient for the Boeing-assigned PM to present at 
PMRs."""})
    
    memory.save_context({"input": """"Section: Technical Interchange Meetings (TIMs) 
The Supplier shall participate in monthly Technical Interchange Meetings (TIMs) between the 
Supplier and Boeing technical personnel to monitor and support technical and affordability 
activities, as necessary, and resolve technical issues. Boeing will determine, and the Supplier may 
suggest, topics to be discussed during each TIM. The meetings will be held virtually for calendar 
year (CY) 2021. Thereafter, the meetings are to be hosted alternately at Supplier facilities and 
Boeing facilities. TIMs will commence no later than 60 days after notice to proceed and continue 
until the successful completion of Final Review. Customer representatives may also attend at 
their discretion. Boeing and the Supplier will identify the standard TIM agenda items at the first 
TIM. 
The Supplier shall provide at the initial TIM, as applicable: 
 RI&O Management Process 
 Corrosion Prevention and Control Plan 
 Lead-Free Control Plan 
 Configuration Management (CM) Process or Configuration Management Plan (CMP) 
PMRs and TIMs will be held concurrently when the two meetings are closely scheduled. 
The Supplier shall furnish engineering drawings and data for use during TIMs. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item P-02.15 – Presentation Materials, Agenda, Minutes and Action Item Responses 
for Meetings and Reviews"""},
{"output": """NAI agrees with the information provided in this section of the SSOW"""})
    
    memory.save_context({"input": """Section: System Requirements Review (SRR) 
The Supplier shall participate in a System Requirements Review (SRR) with Boeing to validate 
the intent and understanding of each requirement contained in the PC. During the SRR, the 
Supplier shall identify RI&O, affordability and technology readiness associated with 
requirements compliance pertaining to the product being developed. The Supplier shall review 
the initial submittal of the Requirements Verification and Validation Plan and discuss test and 
evaluation responsibilities. During the review, the Supplier shall provide alternatives 
(requirements and solutions) to resolve RI&O. 
The review will occur at the Supplier’s facility and last no more than three days. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item P-02.15 – Presentation Materials, Agenda, Minutes and Action Item Responses 
for Meetings and Reviews 
"""},
{"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Preliminary Design Review (PDR) 
The Supplier shall host a Preliminary Design Review (PDR) at the Supplier’s Facility. The intent 
of the PDR is to confirm that the design approach (as an integrated composite of people, product 
and process solutions) satisfies the functional baseline. The Supplier shall review program RI&O 
and identify closure plans to resolve these risks. Boeing will determine at PDR whether the 
‘design to’ baseline is approved. An approved PDR authorizes the Supplier to proceed to detailed 
design. The Supplier shall resolve any issues identified by Boeing during the review. 
At a minimum, the following should be discussed (as applicable): 
Part description including functional and wiring schematics 
Preliminary drawing package including the assembly drawing and notes (e.g., 
material process callouts and material selection) 
Critical Characteristic suggestions for any Critical Safety Items (CSI) 
ICD 
Redundancy Management Implementation 
Connectors and Wiring 
Installation Drawing and Characteristics 
Development testing (e.g., ballistic testing, impulse testing, etc.) 
Ballistic design philosophy 
Electromagnetic Environmental Effects (E3) 
Environmental threats (natural and induced) 
Design analysis (e.g., stress, DDV thermal, performance) 
Accuracy and Tolerances 
Safety, Reliability, Maintainability and Human Factors 
Failure modes and effects 
Testability 
Preliminary Hazard Analyses 
Weights 
Prototype program support equipment 
Growth 
Status and schedule 
Plan updates 
Management 
Quality Assurance 
Obsolescence Strategy 
Configuration Control 
Hardware 
Software 
Design Substantiation
Requirements Verification Matrix (RVM) 
Schedule 
Risks 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item P-02.15 – Presentation Materials, Agenda, Minutes and Action Item Responses 
for Meetings and Reviews """},
{"output": """NAI agrees with the information provided in this section of the SSOW"""})

    memory.save_context({"input": """Section: Critical Design Review (CDR) 
The Supplier shall host a Critical Design Review (CDR) to demonstrate that the detailed designs 
(as an integrated composite of people, product and process solutions) are complete and meet 
requirements, and that the system and subsystem are ready for fabrication, assembly and 
integration. The Supplier shall review program risks and identify closure plans to resolve these 
risks. Boeing will determine at CDR whether the ‘build-to’ baseline is approved. An approved 
CDR authorizes the Supplier to proceed with fabrication, system qualification testing and 
integration. The Supplier shall resolve any issues identified by Boeing during the review. 
Prior to CDR, the Supplier shall provide updated data from PDR, as well as the following 
analyses: 
1. Tolerance and accuracy 
2. Sensitivity to supply voltage variations 
3. Subsystem Hazard Analysis 
4. EMI Control Plan 
5. Qualification Test Plan 
The Supplier shall ensure all drawings are fully signed off and ready to submit to manufacturing 
to begin manufacturing. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item P-02.15 – Presentation Materials, Agenda, Minutes and Action Item Responses 
for Meetings and Reviews """},
 {"output": """NAI agrees with the information provided in this section of the SSOW"""})
    
    memory.save_context({"input": """Section: Test Readiness Review (TRR) 
The Supplier shall conduct a Test Readiness Review (TRR). The intent of the TRR is to confirm 
that the Product is ready for testing and to demonstrate that the people, Product, and process 
solutions are complete and meet QTP requirements. This includes verifying the completeness of 
the test procedures, test fixtures, test instrumentation, data acquisition, and test hardware and 
ensuring they conform to the QTP. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item P-02.15 – Presentation Materials, Agenda, Minutes and Action Item Responses 
for Meetings and Reviews"""},
 {"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Functional Configuration Audit (FCA) 
The Supplier shall support a Functional Configuration Audit (FCA) conducted by Boeing. The 
FCA is conducted following completion of qualification and related testing, submission of the test 
reports to Boeing, and Boeing approval of all compliance related SDRL data items and is 
expected to last no longer than two days at the Supplier’s facility. The FCA is a formal audit of a 
Configuration Item (CI), (hardware, software, and firmware as appropriate) performed at the 
subsystem level to assure that the CI meets the functional and performance requirements as 
specified in the Specification.
FCA may be held concurrently with Physical Configuration Audit (PCA) upon mutual agreement 
by Boeing and the Supplier. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.17 – Configuration Item (CI) List and Audit Plan 
 Data Item E-75.39 – Design Certification 
 Data Item P-02.15 – Presentation Materials, Agenda, Minutes and Action Item Responses 
for Meetings and Reviews """},
 {"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Physical Configuration Audit (PCA) 
The Supplier shall support a Physical Configuration Audit (PCA) conducted by Boeing. The PCA 
is conducted after the completion of qualification and prior to the initiation of the Low Rate 
Initial Production (LRIP) phase and is expected to last no longer than two days at the Supplier’s 
facility. The PCA is a formal examination of the as-built version of a Configuration Item (CI) 
against its design documentation to establish the CI’s product baseline. The PCA confirms the 
final performance, mechanical, and electrical configuration of the CI before beginning 
production. 
PCA may be held concurrently with FCA upon mutual agreement by Boeing and the Supplier. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.17 – Configuration Item (CI) List and Audit Plan 
 Data Item E-75.39 – Design Certification 
 Data Item P-02.15 – Presentation Materials, Agenda, Minutes and Action Item Responses 
for Meetings and Reviews"""},
 {"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Parts, Materials, and Processes Management 
The Supplier shall prepare data containing an as-designed parts and materials list in an indentured 
format and include identification of processes used in the design. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-54.04 - Material and Process Selection and Justification Data"""},
 {"output": """Exception. NAI’s proposed solution is comprised of COTS products."""})
    
    memory.save_context({"input": """Section: Obsolescence Management 
The Supplier shall develop an obsolescence management strategy and incorporate the strategy 
into the design philosophy and process in order to minimize obsolescence risk to the program. 
The Supplier shall present the obsolescence management strategy to Boeing at as part of PDR. 
The Supplier shall prepare an Obsolescence Management Bill of Materials (OM-BOM) List and 
regularly monitor the obsolescence status of component content in the equipment to minimize the 
impact of all known obsolescence and Diminishing Manufacturing Sources and Material 
Shortages (DMSMS) issues. The Supplier is not required to include in this submittal BOM data 
for COTS assemblies integrated into the equipment. 
Upon identification of an obsolescence issue, the Supplier shall prepare an alert notification in 
accordance with SDRL Data Item L-127. 
If the Supplier is storing Boeing-owned last-time buy stock, the Supplier shall submit Last-Time 
Buy Inventory Usage Reports in accordance with the SDRL Data Item E-75.80. 
The Supplier shall flow all requirements in this paragraph to all sub-tier Suppliers above the piece 
part level. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.49 – Obsolescence Management Bill of Materials (OM-BOM) 
 Data Item E-75.80 – Last-Time Buy Inventory Usage Reports 
 Data Item L-127 – Obsolescence Notification """},
 {"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Government-Industry Data Exchange Program (GIDEP) 
U.S. and Canadian Suppliers shall support the Government-Industry Data Exchange Program 
(GIDEP) as a GIDEP member. 
U.S. and Canadian Suppliers shall monitor SAFE Alerts, Alerts, problem advisories, and agency 
action notices from the Government Industry Data Exchange Program which warn of deficient, 
suspect counterfeit, or problem parts, processes or materials. If a GIDEP identifies a part, process 
or material that, has been, is, or will be used on deliverable mission hardware, then the Supplier 
shall provide Boeing with detailed data and recommendations. 
U.S. and Canadian Suppliers shall prepare GIDEP Alerts or problem advisories for parts, 
processes, or materials which are determined to be non-compliant or to have a consistent problem 
condition, and may have implications elsewhere in industry. Upon identification of an 
obsolescence issue, the Supplier shall use the GIDEP DMSMS notices to provide notification of 
obsolete items within ten (10) days of identification."""},
 {"output": """NAI utilizes SiliconExperts, which monitors the alerts mentioned in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Corrosion Prevention and Control 
The Supplier shall present the corrosion prevention and control plan in Supplier format at the 
initial TIM and include as part of the SDRL Data Item P-02.15."""},
 {"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Electrostatic Discharge Sensitive (ESDS) Control Program 
The Supplier shall use an Electrostatic Discharge Sensitive (ESDS) control program in 
accordance with MIL-STD-1686 for hardware that contains electrostatic discharge sensitive parts."""},
 {"output": """NAI agrees with the information provided in this section of the SSOW."""})
    
    memory.save_context({"input": """Section: Lead-Free Electronics 
If the Product contains electronics, the Supplier shall control the introduction of lead-free solder 
alloys by implementing a Lead-Free Control Plan compliant with GEIA-STD-0005-1, 
“Performance Standard for Aerospace and High Performance Electronic Systems Containing PbFree Solder” and the GEIA-STD-0005-2, “Standard for Mitigating the Effects of Tin Whiskers in 
Aerospace and High Performance Electronic Systems.” 
If applicable, the Supplier shall present the Lead-Free Control Plan in Supplier format at the 
initial TIM and include as part of the SDRL Data Item P-02.15. 
If the Supplier uses or transitions to lead-free solder alloys, the Supplier shall notify Boeing via 
SDRL Data Item E-75.03. """},
 {"output": """NAI agrees with the information provided in this section of the SSOW"""})
    
    memory.save_context({"input": """Section: Counterfeit Prevention Plan 
The Supplier shall prepare a Counterfeit Prevention Plan to address counterfeit issues in 
accordance with SAE AS 5553 for electronic parts and SAE AS 6174 as a guide for all other 
materials, parts, assemblies, other procured items, and elements. The Supplier shall include in the 
plans all aspects of the System, including but not limited to, counterfeit parts, malicious code, or 
any other elements that would allow adversaries to gain unauthorized access to data, alter data, 
interrupt communications, or otherwise disrupt operations. 
The Supplier shall notify Boeing within 24 hours of becoming aware of, or has reason to suspect, 
counterfeit issues regardless of how the Supplier received notification. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-69.13 – Counterfeit Prevention Plan """},
 {"output": """NAI plans to submit its QMS chapter covering counterfeit component screening"""})
    
    memory.save_context({"input": """Section: Additive Manufacturing 
The Supplier shall obtain Boeing written approval prior to the usage of additive manufacturing 
for any components. The Supplier’s request shall include the applicable design allowables or the 
plan to provide the applicable design allowables, and must be specific to, at a minimum, 
powder/wire source, printing machine, and settings to be utilized for component production"""},
 {"output": """Exception. NAI’s proposed solution is comprised of COTS products."""})
    
    memory.save_context({"input": """Section: Electronic Component Management Plan (ECMP) 
The Supplier shall have a Boeing approved Electronic Component Management Plan (ECMP) in 
accordance with SAE EIA-STD-4899 or third party approved ECMP in accordance with IEC 
62239-1. The Supplier may submit existing plans for approval if available. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-69.12 – Electronic Component Management Plan (ECMP)"""},
 {"output": """Exception. NAI’s proposed solution is comprised of COTS products."""})
    
    memory.save_context({"input": """Section: Restricted Parts 
The Supplier shall not use the following parts for new designs without approval by Boeing 
and the customer: 
 Silver-Tantalum capacitors, such as per MIL-C-39006, except for series /22 or /25
 Nichrome surface mount technology resistors, such as per MIL-R-55342, which 
are either not hermetically sealed or not coated and qualified to prevent 
deterioration under humidity conditions when powered 
 Variable capacitors, resistors, and magnetic devices 
 Semiconductors not equivalent to or better than JANTX or AEC-Q101 
 Microcircuits not equivalent to or better than QML/SMD or AEC-Q100 
 Open type magnetic devices 
 Socketed devices which do not have staked features for mechanical robustness 
 Non-hermetic microcircuits and semiconductors without an approved 
selection and control process 
 Parts, materials, and processes as stated in MIL-STD-11991 Appendix C"""},
 {"output": """NAI Agrees with the documents outlined in this section of the SOW."""})
    
    memory.save_context({"input": """Section: Non-Standard Electronics Parts List 
The Supplier shall prepare a separate Non-Standard Electronics Parts List in accordance with DIMISC-80508 listing those electronic parts determined to be high risk due to material, process, 
and obsolescence including any hybrids, microprocessors, controllers and Application Specific 
Integrated Circuits (ASIC), oscillators and custom devices which are Original Equipment 
Manufacturer (OEM) specific and cannot be found in standard electronic part catalogs. The 
Supplier shall address these electronic parts in risk management planning and submit as part of 
Data Item E-69.12."""},
 {"output": """Exception. NAI’s proposed solution is comprised of COTS products."""})
    
    memory.save_context({"input": """Section: Replacement Electronic Parts Qualification 
If using replacement electronic parts, the Supplier shall select replacement electronic parts in 
accordance with the selection process described in the Supplier’s Parts Management Plan using 
vendor certification of electronic parts specifications, qualification tests, and analysis, as 
required, to satisfy design requirements. For each new replacement part or modification, the 
Supplier shall prepare an Electronic Part Qualification Report in accordance with DI-MISC80508 and deliver as part of Data Item E-69.12. The report shall describe the basis for selection 
including vendor certifications, test results or analysis, as appropriate. """},
 {"output": """Exception. NAI’s proposed solution is comprised of COTS products."""})
    
    memory.save_context({"input": """Section: Configuration Management (CM) 
The Supplier shall establish and maintain a Configuration Management (CM) program to assure 
proper Configuration Item (CI) identification, engineering change control, configuration auditing 
and status accounting for deliverable hardware/software/firmware and configuration data 
management in accordance with the requirements contained herein and use SAE EIA 649-1 and 
MIL-HDBK-61 as guides. 
The Supplier shall document software and firmware configuration management records in 
accordance with DO-178 Section 11.18 and DO-254 section 10.7 and make available to Boeing 
upon request. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.25 – Configuration Management Plan (CMP) 
If the Supplier has an existing CM Plan, the Supplier shall submit the existing plan in accordance 
with SDRL Data Item E-75.25."""},
 {"output": """NAI agrees with the information provided in section 3.5.4 of the SSOW"""})
    
    memory.save_context({"input": """Section: Baseline Configuration Control 
Baseline configuration control is an evolutionary process under which the configuration is 
controlled by increasingly detailed technical data (specifications, models, etc.) and evolves from 
informal data, to controlled data (Supplier configuration controlled), and eventually to base-lined 
data (Boeing controlled). Each baseline consists of key documentation placed under contractual 
control at the appropriate time in the life cycle of the CI. The configuration of the CI is defined by 
its base-lined configuration plus approved changes to the baseline. 
Throughout the life cycle of the CI, the Supplier shall establish, develop, and control the 
following baselines in accordance with EIA 649-1. 
Functional Baseline 
The Functional baseline is established at contract award and is defined by the Functional 
Configuration Documentation which consists of the Specification, SSOW, and SDRL, as 
applicable. 
Allocated Baseline 
The Allocated Baseline is established at successful completion of the PDR and defines the 
functional characteristics allocated to the CI (Allocated Configuration Documentation) from the 
system level requirements, progressively expanding as the Supplier progresses deeper into the 
design. The Allocated Configuration Documentation consists of any Boeing approved data, the 
Supplier's lower tiered specifications, and other related data which describes the hardware. 
Product Baseline 
The Product Baseline is established at the successful completion of the CDR and is finalized at 
successful completion of the PCA on a production representative end item. The Product Baseline 
is defined by the Product Configuration Documentation which consists of the technical 
documentation describing the CI at the time of the CDR and progresses to include all of the 
Boeing approved technical documentation, including models, which define the CI at the time of 
PCA. Product Configuration Documentation is the "build-to" set of technical requirements to be 
used during the fabrication of flight hardware, test, operation, maintenance, and logistics support 
phase of the CI life cycle. """},
 {"output": """Please see above."""})
    
    memory.save_context({"input": """Section: Change Management"""},
 {"output": """Please see above."""})
    
    memory.save_context({"input": """Section: Class I Changes / Major Changes 
Class I changes (or Major changes) are those changes which affect the established baseline(s). 
For Class I changes, as defined in EIA 649-1 and MIL-HDBK-61, the Supplier shall prepare 
SDRL Data Item E-75.03 with a detailed description of the proposed change including an 
assessment of the impact on drawings, specifications, acceptance or test procedures and plans, 
qualification test procedures and plans, manufacturing processes and documentation identified as 
part of an approved baseline (i.e. released and approved configuration data). The Supplier shall 
not incorporate a Class I change prior to receiving approval from Boeing. The Supplier shall 
obtain Boeing approval prior to the Supplier taking any action to incorporate the subject change 
into the appropriate baseline(s). The Supplier shall not ship deliverable end-items with 
unauthorized and/or unapproved Class I changes incorporated. 
The Supplier shall submit the following data item(s) in accordance with the SDRL:
 Data Item E-75.03 – Change Proposal Data """},
 {"output": """Please see above."""})
    
    memory.save_context({"input": """Section: Class II Changes / Minor Changes 
The Supplier shall prepare and submit Class II changes, as defined in EIA 649-1 and MILHDBK-61, for approval of classification. Class II changes by definition do not affect a Boeing 
approved baseline. Any change that the Supplier implements as a Class II, and which Boeing later 
determines is a Class I, may require removal of the change at the Supplier's expense. The 
Supplier shall not ship hardware to Boeing with unapproved changes incorporated. The Supplier 
may implement a Class II change concurrent with submittal of the Supplier Minor Change 
Proposal. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.90 – Supplier Minor Change Proposal """},
 {"output": """Please see above"""})
    
    memory.save_context({"input": """Section: Requests for Variance 
The Supplier shall submit Requests for Variance in accordance with SAE EIA-649-1 and MILHDBK-61 criteria. The Supplier shall assign variance classification (i.e., Minor, Major, or 
Critical) in accordance with DD Form 1694 (Rev 4/2015 or most recent). The Supplier shall 
disposition Minor Variances internally at the Supplier by a duly constituted Material Review 
Board (MRB), which is coordinated by Supplier Quality Assurance, however, the Supplier shall 
not approve any nonconforming critical characteristics via the Supplier MRB. The Supplier shall 
submit all nonconforming Critical Safety Item (CSI) Critical Components (CCs), regardless of 
Variance classification, to Boeing for disposition. If the Variance affects a Boeing requirement, 
the Variance is considered Major to the Supplier. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-75.11 – Request for Variance"""},
 {"output": """Please see above."""})
    
    memory.save_context({"input": """Section: Item Unique Identification (IUID) Marking of Parts and Assemblies 
For end items or major assemblies over $5000, plus all embedded items which are/will be serially 
managed inventory, and any other parts identified as requiring Item Unique Identification (IUID), 
the Supplier shall mark parts using an IUID part marking tool/method per MIL-STD-130, D210-
13613-1, and/or D210-13613-2. 
For parts that require IUID, the Supplier shall prepare a serialization procedure, verification 
report, and sample label/nameplate or direct part mark in accordance with D210-13613-1 or 
D210-13613-2. 
The Supplier shall identify and report compliant IUID marked production parts into the Boeing 
Unique Identification (UID) System (BUS) and use Boeing contract clause “Q112P Seller 
Serialization” for instructions on registering IUID marked parts into the BUS. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-56.31 – Item Unique Identification (IUID) Report
 Data Item E-56.32 – Item Unique Identification (IUID) Sample with Verification Report 
and Serialization Procedure"""},
 {"output": """Please see above."""})
    
    memory.save_context({"input": """Section: Supplier Export Jurisdiction and Classification 
All U.S. Suppliers shall provide export jurisdiction and classification determinations as identified 
on the United States Munitions List (USML) and Commerce Control List (CCL) of any 
assemblies, software, parts and components down to the serviceable level, and technical data to 
be delivered under this contract in accordance with the latest International Traffic In Arms and 
Export Administration Regulations (ITAR - Title 22 CFR Ch. I Sub-Ch. M, EAR - Title 15 CFR 
Ch. VII Sub-Ch. C). 
U.S. Suppliers shall provide export jurisdiction and classification of all data delivered through the 
export disclosure fields of CSDT. 
U.S. Suppliers shall provide export jurisdiction and classification of any assemblies, software, 
parts, and components through the Export Classification Determination Matrix. U.S. Suppliers 
shall notify and provide corrections to Boeing within 30 days of any significant changes as a 
result of error, Regulatory revisions, or special regulatory guidance or clarification. Within the 
context of this paragraph, significant is defined as changes that result in a change in the level of 
required control of the data. 
Foreign Suppliers shall work with Boeing, as requested, to ensure the proper U.S. export 
jurisdiction and classification are applied. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item L-99 – Export Classification Determinations Matrix """},
 {"output": """NAI agrees to generate and deliver the following data items:
• Data Item L-99 – Export Classification Determinations Matrix"""})
    
    memory.save_context({"input": """Section: Data Accession List (DAL) 
The Supplier shall list data generated to fulfill contractual tasks for the PC on the Data Accession 
List (DAL) that is not being formally submitted as a data item in accordance with the SDRL. This 
list includes engineering and management data required by the Supplier to develop, test, and 
manage the program, as well as any data called out here in this SSOW that does not have an 
explicit delivery requirement in the SDRL. The Supplier is not required to place on the Data 
Accession List (DAL), pre-existing, commercial data not generated in the performance of this 
SSOW. 
Per the Deferred Ordering Clause 252.227-7027, Boeing’s customer can use the list to order data 
at any time during the performance of this PC or within a period of three (3) years after acceptance 
of all items (other than technical data or computer software) to be delivered under this contract or 
the termination of this PC or order any technical data or computer software generated in the 
performance of this PC. 
The Supplier shall submit the following data item(s) in accordance with the SDRL: 
 Data Item E-76.11 – Data Accession List (DAL) """},
 {"output": """NAI agrees to generate and deliver the following data items:
• Data Item E-76.11 – Data Accession List (DAL)"""})
    

    # Northrop Grumman

    memory.save_context({"input": """Section: Program Management Plan
The Supplier shall provide management oversight for all in-house and other 
sub-contractor activities. The Supplier shall identify a single point of contact 
who will be responsible for the program management of this effort. The 
Supplier's efforts shall encompass the overall planning, directing, and 
qualification of the Equipment."""},
 {"output": """NAI will assign a program manager to this effort. This individual will be responsible for 
overall execution, staffing, and deliverables associated with the program."""})
    
    memory.save_context({"input": """Section: Configuration Management
The Supplier shall utilize the existing Configuration Management (CM) 
program to control products, processes, and related documentation to ensure 
the integrity of design and supportability for both hardware and software 
configuration items (CIs) consistent with SAE/GEIA-HB-649. The CM effort 
shall include identification and control of all system functional, allocated, and 
product baselines; establishment of a configuration status accounting system 
to provide an audit trail of all configuration changes; and identification, 
documentation, and verification of the functional and physical characteristics 
of each CI.
The Supplier shall flow down configuration management requirements on all 
subcontractors to ensure that configuration integrity of the procured items will 
be maintained throughout system life."""},
 {"output": """NAI agrees with the statements found in this section of the SOW"""})
    
    memory.save_context({"input": """Section: Variance
A variance is a written authorization to depart from the performance or design 
requirement of a specification, drawing, Engineering Change Proposal (ECP), 
or other contractual document for a specified number of items or period of 
time. The Supplier shall not deliver any product with a known 
nonconformance without having received prior Northrop Grumman approval 
of the variance. The Supplier shall submit all major Requests for Variance to 
Northrop Grumman for review via the CM Manager for processing through the 
Configuration Control Board. Disposition of minor deviations shall be in 
accordance with SAE/EIA-649, SAE GEIA-HB-649."""},
 {"output": """NAI agrees with the statements found in this section of the SOW."""})
    
    memory.save_context({"input": """Section: Program Management Review/Reporting
The Supplier shall conduct weekly program status meetings. During these 
meetings, the Supplier shall present integrated schedule and technical 
performance status, cost/schedule trends, significant cost/schedule/technical 
variances, projected impacts, quantified risk assessments, and corrective 
action plans."""},
 {"output": """NAI agrees with the statements found in this section of the SOW, except for cost reporting. As 
a small business, NAI is exempt from earn value management. Should the need arise for a 
significant technical change, NAI will initiate a discussion around a variance or engineering 
change proposal."""})
    
    memory.save_context({"input": """Section: Program Schedule
During the weekly status meeting, Supplier shall present a detailed schedule 
of upcoming tasks critical to program success. These should include, but are 
not limited to hardware procurement milestones, individual qualification 
testing dates, programmatic meetings, SDRL deliverables, etc."""},
 {"output": """NAI agrees with the statements found in this section of the SOW"""})
    
    memory.save_context({"input": """Section: Supplier Quality Assurance (SQA)
The Supplier shall establish, document, implement, and maintain a quality 
management system and continually improve its effectiveness in accordance 
with the requirements of ANSI/American Society for Quality 
(ASQ)/International Organization for Standardization (ISO) 9001, Quality 
Management Systems, supplemented by SAE/AS 9100D or equivalent. The 
Supplier shall:
• Identify the processes needed for the quality management system and 
their application throughout the organization;
• Determine the sequence and interaction of these processes;
• Determine criteria and methods needed to ensure that both the operation 
and control of these processes are effective;
• Ensure the availability of resources and information necessary to support 
the operation and monitoring of these processes;
• Monitor, measure, and analyze these processes; and
• Implement actions necessary to achieve planned results and continual 
improvement of these processes.
When the Supplier chooses to outsource any process that affects product 
conformity with requirements, the Supplier shall ensure control over such 
processes. Control of such outsourced processes shall be identified within the 
quality management system.
The Quality system procedures, planning, and all other documents and data 
that comprise the Supplier’s Quality system shall be made available to the 
Buyer for review, as required. Upon reasonable notification to the Supplier, 
the Buyer shall have the right to send representatives to the Supplier’s or their 
sub-tier Subcontractor’s facility to verify contract compliance, and perform 
such activities as pre award surveys, Quality audits, inspections, test 
witnessing or other evaluations, as necessary"""},
 {"output": """NAI Agrees with the documents outlined in this section of the SOW."""})
    
    memory.save_context({"input": """Section: Data Rights
All delivered data shall be marked in accordance with the applicable DFARS 
clauses. Company proprietary markings shall be prohibited on submitted 
documentations. The Buyer will reject any SDRL delivery if the data markings 
are not marked in accordance with the applicable Defense Federal 
Acquisition Regulation Supplement (DFARS) clauses. The Supplier shall resolve all inappropriate markings not 
in accordance with the applicable DFARS clauses at no additional cost to the Buyer and within five business 
days of reporting of the inappropriate marking."""},
 {"output": """The statements found in this paragraph of the SOW are understood to only be applicable to 
SDRLs for this program."""})
    
    memory.save_context({"input": """Section: Security
The Supplier shall implement and maintain security procedures and controls 
to prevent unauthorized disclosure of controlled unclassified information and 
to control distribution of controlled unclassified information in accordance with
the National Industrial Security Program Operating Manual and DoDM 
5200.01, Information Security Manual and applicable DFARS clauses. All 
controlled unclassified information shall be appropriately identified and 
marked as Controlled Unclassified Information (CUI) in accordance with
DoDM 5200.01, Information Security Program: Controlled Unclassified 
Information (CUI) Volume 4 (enclosure 3) and DoD 5400.7-R (Freedom of 
Information Act Regulation) (Chapter 3). All Supplier facilities shall provide an 
appropriate means of storage for controlled unclassified documents, 
equipment, and materials."""},
 {"output": """NAI agrees with the statements found in this section of the SOW."""})
    
    memory.save_context({"input": """Section: Operations Security (OPSEC)
The Supplier shall update and maintain its existing facility OPSEC program to 
protect controlled unclassified activities, information, and material used or 
developed by the Supplier and any Subcontractor during performance of the 
contract. The Supplier shall be responsible for the subcontractor 
implementation of the OPSEC requirements. This program may include 
Information Assurance and Communications Security.
The OPSEC program shall be in accordance with National Security Decision 
Directive 298, DoDD 5205.02, DoD OPSEC Program, DoD 5205.02-M, DoD 
OPSEC Program Manual, OPNAVINST 3432.1A series, and SECNAV 
3070.02 Operation Security and at a minimum shall include:
1. Assignment of responsibility for OPSEC direction and implementation.
2. Issuance of procedures and planning guidance for the use of OPSEC 
techniques to identify vulnerabilities and apply applicable 
countermeasures.
3. Establishment of OPSEC education and awareness training.
4. Provisions for management, annual review, and evaluation of OPSEC 
programs.
5. Flow down of OPSEC requirements to subcontractors when applicable.
The Supplier’s plan and procedures to update and maintain OPSEC shall be 
in accordance with the PPIP (C72- 6100-205)"""},
 {"output": """NAI agrees with the statements found in this section of the SOW"""})
    
    memory.save_context({"input": """Section: Information Security
If the work is performed at the Supplier's facility, the Supplier shall implement 
and maintain security procedures and controls to prevent unauthorized 
disclosure of classified information and controlled unclassified information and 
to control distribution of CUI in accordance with DoD 5220.22- M (NISPOM), 
and SECNAV M-5510.36."""},
 {"output": """NAI agrees with the statements found in this section of the SOW."""})
    
    memory.save_context({"input": """Section: Public Release
Any controlled unclassified information pertaining to this contract shall not be 
released for public dissemination, including posting to any social media sites 
such as Facebook or Twitter, unless it has been approved for public release 
by Northrop Grumman."""},
 {"output": """NAI agrees with the statements found in this section of the SOW."""})
    
    memory.save_context({"input": """Section: Meetings
The Supplier shall support three (3) Technical Interface Meetings (TIMs), and 
weekly meetings during contract period, as required. All TIMs and weekly 
meetings will be conducted via telephone conference or in a collaborative 
environment. The agendas, presentations, minutes, and actions of the TIMs 
shall be delivered in accordance with the SDRL S092, Conference Meeting 
Minutes. A notional meeting schedule is outlined in Table 1. Final dates will 
be agreed upon by the Buyer and Supplier.
Table 1: Meeting Schedule
Meeting Schedule Purpose
Status Weekly Recurring meeting during contract period of 
performance
TIM 1 6 Weeks ARO System Requirements Review (SRR) -
Planned Requirements and Verification 
Methods Review, heatsink design effort
TIM 2 3 Months ARO Design Review
TIM 3 4 Months ARO Test Readiness Review (TRR)
The Government may be in attendance for each of these meetings. Supplier’s 
subcontractors shall support as necessary"""},
 {"output": """NAI agrees with the meetings outlined in this section of the SOW, in accordance with SDRL 
S092. Should the need arise, additional ad-hoc discussions or meetings may be coordinated via 
the program manager after kick-off."""})
    
    memory.save_context({"input": """Section: Subcontractor Quality Assurance 
The Supplier shall require its Subcontractors to maintain an equivalent Quality 
Management System that achieves control of the quality of its supplies and 
services. Subcontractors and suppliers shall be compliant with or certified to 
ISO 9001 standards, except for level of design authority. The Supplier shall 
notify Buyer if any Subcontractors are not certified to ISO standards"""},
 {"output": """NAI agrees with the statements found in this section of the SOW."""})
    
    