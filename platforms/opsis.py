# Support for the Numato Opsis - The first HDMI2USB production board

from mibuild.generic_platform import *
from mibuild.xilinx import XilinxPlatform
from mibuild.xilinx import XC3SProg, iMPACT, Adept, UrJTAG

_io = [
    ## FXO-HC536R - component U17
    # 100MHz - CMOS Crystal Oscillator
    #NET "clk"                  LOC =   "AB13"       |IOSTANDARD =            None;     #                      (/FPGA_Bank_1_2/USRCLK)
    ("clk100", 0, Pins("AB13"), IOStandard("LVCMOS33")),

    ## FXO-HC536R - component U26
    # 27MHz - CMOS Crystal Oscillator
    #NET "clk"                  LOC =    "N19"       |IOSTANDARD =            None;     #                      (/SPI_Flash/27MHz)
    ("clk27", 0, Pins("N19"), IOStandard("LVCMOS33")),

    ## SW_PUSH - component SW1
    # Connected to Bank 3 - 1.5V bank
    #NET "???"                  LOC =     "Y3"       |IOSTANDARD =            None;     #                      (/FPGA_Bank_0_3/SWITCH | Net-(R54-Pad2))
    ("cpu_reset", 0, Pins("Y3"), IOStandard("LVCMOS15"), Misc("PULLUP")),

    # CY7C68013A_100AC - component U2
    ("fx2", 0,
        #NET "fx2_ifclk"            LOC =    "P20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY-IFCLK)
        Subsignal("ifclk", Pins("P20"), IOStandard("LVCMOS33")),
        #NET "fx2_fd<0>"            LOC =    "C20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD0)
        #NET "fx2_fd<1>"            LOC =    "C22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD1)
        #NET "fx2_fd<2>"            LOC =    "L15"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD2)
        #NET "fx2_fd<3>"            LOC =    "K16"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD3)
        #NET "fx2_fd<4>"            LOC =    "D21"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD4)
        #NET "fx2_fd<5>"            LOC =    "D22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD5)
        #NET "fx2_fd<6>"            LOC =    "G19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD6)
        #NET "fx2_fd<7>"            LOC =    "F20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD7)
        #NET "fx2_fd<8>"            LOC =    "H18"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD8)
        #NET "fx2_fd<9>"            LOC =    "H19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD9)
        #NET "fx2_fd<10>"           LOC =    "F21"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD10)
        #NET "fx2_fd<11>"           LOC =    "F22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD11)
        #NET "fx2_fd<12>"           LOC =    "E20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD12)
        #NET "fx2_fd<13>"           LOC =    "E22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD13)
        #NET "fx2_fd<14>"           LOC =    "J19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD14)
        #NET "fx2_fd<15>"           LOC =    "H20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_FD15)
        Subsignal("data", Pins("C20 C22 L15 K16 D21 D22 G19 F20 H18 H19 F21 F22 E20 E22 J19 H20"), IOStandard("LVCMOS33")),
        #NET "fx2_fifoadr<0>"       LOC =    "B21"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PA4)
        #NET "fx2_fifoadr<1>"       LOC =    "B22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PA5)
        Subsignal("addr", Pins("B21 B22"), IOStandard("LVCMOS33"), Misc("DRIVE=12")),
        #NET "fx2_flaga"            LOC =    "N16"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_CTL0)
        #NET "fx2_flagb"            LOC =    "P16"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_CTL1)
        #NET "fx2_flagc"            LOC =    "R15"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_CTL2)
        Subsignal("flaga", Pins("N16"), IOStandard("LVCMOS33"), Misc("DRIVE=12")),
        Subsignal("flagb", Pins("P16"), IOStandard("LVCMOS33"), Misc("DRIVE=12")),
        Subsignal("flagc", Pins("R15"), IOStandard("LVCMOS33"), Misc("DRIVE=12")),
        #NET "fx2_flagd/slcs_n"     LOC =    "J17"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PA7)
        Subsignal("cs_n", Pins("J17"), IOStandard("LVCMOS33"),  Misc("DRIVE=12")),
        #NET "fx2_slrd"             LOC =    "P19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RD0)
        Subsignal("rd_n", Pins("P19"), IOStandard("LVCMOS33"), Misc("DRIVE=12")),
        #NET "fx2_slwr"             LOC =    "R19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RD1)
        Subsignal("wr_n", Pins("R19"), IOStandard("LVCMOS33")),
        #NET "fx2_sloe"             LOC =    "H16"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PA2)
        Subsignal("oe_n", Pins("H16"), IOStandard("LVCMOS33"), Misc("DRIVE=12")),
        #NET "fx2_pktend"           LOC =    "J16"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PA6)
        Subsignal("pktend_n", Pins("J16"), IOStandard("LVCMOS33"),  Misc("DRIVE=12")),

        #NET "fx2_ctl<3>"           LOC =    "M18"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_CTL3)
        #NET "fx2_ctl<4>"           LOC =    "M17"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_CTL4)
        #NET "fx2_ctl<5>"           LOC =    "R16"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_CTL5)
        #NET "fx2_init5_n"          LOC =    "T19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_INT5)
        #NET "fx2_int<0>"           LOC =    "F18"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PA0)
        #NET "fx2_int<1>"           LOC =    "F19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PA1)
        #NET "fx2_wu<2>"            LOC =    "H17"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PA3)
        #NET "fx2_gpifadr<0>"       LOC =    "U20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PC0)
        #NET "fx2_gpifadr<1>"       LOC =    "U22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PC1)
        #NET "fx2_gpifadr<2>"       LOC =    "V21"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PC2)
        #NET "fx2_gpifadr<3>"       LOC =    "V22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PC3)
        #NET "fx2_gpifadr<4>"       LOC =    "W20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PC4)
        #NET "fx2_gpifadr<5>"       LOC =    "W22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PC5)
        #NET "fx2_gpifadr<6>"       LOC =    "Y21"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PC6)
        #NET "fx2_gpifadr<7>"       LOC =    "Y22"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_PC7)
        #NET "fx2_gpifadr<8>"       LOC =   "AB21"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Power/DONE | Net-(R28-Pad1))
        # Timers
        #NET "fx2_t<0>"             LOC =    "G17"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/SPI_Flash/TDO-FPGA/TDO-JTAG | Net-(P3-Pad8) | Net-(R14-Pad1))
        ## \/ Strongly pulled (4k) to VCC3V3 via R56
        #NET "fx2_t<1>"             LOC =    "AB2"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Power/PROG_B | Net-(R15-Pad1))
        #NET "fx2_t<2>"             LOC =    "E18"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/SPI_Flash/TDO-USB/TDI-FPGA | Net-(P3-Pad10) | Net-(R23-Pad1))
        #NET "fx2_rd_n"             LOC =    "K19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RD)
        #NET "fx2_rdy<2>"           LOC =    "M16"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RD2)
        #NET "fx2_rdy<3>"           LOC =    "N15"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RD3)
        #NET "fx2_rdy<4>"           LOC =    "U19"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RD4)
        #NET "fx2_rdy<5>"           LOC =    "T20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RD5)
        ## UART0
        #NET "fx2_rxd0"             LOC =    "P18"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RXD1)
        #NET "fx2_txd0"             LOC =    "T17"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_TXD1)
        ## UART1
        #NET "fx2_rxd1"             LOC =    "P17"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_RXD0)
        #NET "fx2_txd1"             LOC =    "R17"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_TXD0)
        #
        #NET "fx2_t0"               LOC =    "G20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_T0)
        #NET "fx2_wr_n"             LOC =    "K18"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/CY_WR)
	# JTAG
        #  - TMS?
        #NET "fx2_rxd<0>"           LOC =    "D20"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Power/TMS | Net-(P3-Pad4) | Net-(R24-Pad1))
        #  - TCK
        #NET "fx2_rxd<1>"           LOC =    "A21"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Power/TCK | Net-(P3-Pad6) | Net-(R26-Pad1))
        ## \/ Strongly pulled (4k) to VCC3V3 via R52
        #NET "fx2_t<2>"             LOC =     "Y4"       |IOSTANDARD =        LVCMOS33 |SLEW=SLOW            |DRIVE=12            ;     #                      (/FPGA_Bank_1_2/INIT_B | Net-(R27-Pad1))

        ## Same pins as the EEPROM
        ## \/ Strongly pulled (2k) to VCC3V3 via R34
        #NET "fx2_scl"              LOC =     "G6"       |IOSTANDARD =             I2C;     #                      (/Ethernet/MAC_SCL)
        #Subsignal("scl", Pins("G6"), IOStandard("I2C")),
        #NET "fx2_sda"              LOC =     "C1"       |IOSTANDARD =             I2C;     #                      (/Ethernet/MAC_SDA)
        #Subsignal("sda", Pins("C1"), IOStandard("I2C")),
    ),

    ## onBoard Quad-SPI Flash
    ## W25Q128FVEIG - component U3
    ## 128M (16M x 8) - 104MHz
    ("spiflash4x", 0,
        ## \/ Strongly pulled (10k) to VCC3V3 via R18
        #NET "???"                  LOC =    "AA3"       |IOSTANDARD =            None;     #                      (/FPGA_Bank_1_2/SPI_CS_N)
        Subsignal("cs_n", Pins("AA3")),
        #NET "???"                  LOC =    "Y20"       |IOSTANDARD =            None;     #                      (/FPGA_Bank_1_2/SPI_CLK)
        Subsignal("clk", Pins("Y20")),
        #NET "???"                  LOC =   "AB20"       |IOSTANDARD =            None;     #                      (/FPGA_Bank_1_2/SPI_MOSI_CSI_N_MISO0)
        ## \/ Strongly pulled (10k) to VCC3V3 via R19
        #NET "???"                  LOC =   "AA20"       |IOSTANDARD =            None;     #                      (/FPGA_Bank_1_2/SPI_DO_DIN_MISO1 | Net-(R16-Pad1))
        ## \/ Strongly pulled (10k) to VCC3V3 via R20
        #NET "???"                  LOC =    "R13"       |IOSTANDARD =            None;     #                      (/FPGA_Bank_1_2/SPI_D1_MISO2 | Net-(R17-Pad1))
        ## \/ Strongly pulled (10k) to VCC3V3 via R21
        #NET "???"                  LOC =    "T14"       |IOSTANDARD =            None;     #                      (/FPGA_Bank_1_2/SPI_D2_MISO3)
        Subsignal("dq", Pins("AB20", "AA20", "R13", "T14")),
        IOStandard("LVCMOS33"), Misc("SLEW=FAST")
    ),

    ## onBoard Leds
    # NET "Led<0>" LOC = "U18"; # Bank = 1, Pin name = IO_L52N_M1DQ15,       Sch name = LD0
    #("user_led", 0, Pins("U18")),

    ## TEMAC Ethernet MAC - FIXME
    # 10/100/1000 Ethernet PHY
    ## RTL8211E-VL - component U20 - RGMII
    #NET "eth_intb"             LOC =     "V9"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_INT_B)
    #NET "eth_mdc"              LOC =     "V7"       |IOSTANDARD =             I2C;     #                      (/Ethernet/ETH_MDC)
    ## \/ Strongly pulled (1k) to /Ethernet/ETH_VCC3V3 via R50
    #NET "eth_mdio"             LOC =     "T8"       |IOSTANDARD =             I2C;     #                      (/Ethernet/ETH_MDIO)
    ## \/ Strongly pulled (4k) to VCC3V3 via R51
    #NET "eth_phyrstb"          LOC =     "U8"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_RESET_B)
    #NET "eth_rxc"              LOC =   "AA12"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_RXCLK)
    ## \/ Strongly pulled (4k) to GND via R48
    #NET "eth_rxctl"            LOC =     "U9"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_RXCTL)
    ## \/ Strongly pulled (4k) to /Ethernet/ETH_VCC3V3 via R49
    #NET "eth_rxd[0]"           LOC =     "R9"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_RXD0)
    ## \/ Strongly pulled (4k) to /Ethernet/ETH_VCC3V3 via R65
    #NET "eth_rxd[1]"           LOC =     "R8"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_RXD1)
    ## \/ Strongly pulled (4k) to /Ethernet/ETH_VCC3V3 via R66
    #NET "eth_rxd[2]"           LOC =     "W6"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_RXD2)
    ## \/ Strongly pulled (4k) to /Ethernet/ETH_VCC3V3 via R67
    #NET "eth_rxd[3]"           LOC =     "Y6"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_RXD3)
    #NET "eth_txc"              LOC =   "AB12"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_TXCLK)
    #NET "eth_txctl"            LOC =     "W8"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_TXCTL)
    #NET "eth_txd[0]"           LOC =     "W9"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_TXD0)
    #NET "eth_txd[1]"           LOC =     "Y8"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_TXD1)
    #NET "eth_txd[2]"           LOC =    "AA6"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_TXD2)
    #NET "eth_txd[3]"           LOC =    "AB6"       |IOSTANDARD =        LVCMOS33;     #                      (/Ethernet/ETH_TXD3)
    ## 24AA02E48 - component U23
    ## 2 Kbit Electrically Erasable PROM
    ## Pre-programmed Globally Unique, 48-bit Node Address
    ## The device is organized as two blocks of 128 x 8-bit memory with a 2-wire serial interface.
    ##
    ## \/ Strongly pulled (2k) to VCC3V3 via R34
    #NET "eeprom_scl"           LOC =     "G6"       |IOSTANDARD =             I2C;     #                      (/Ethernet/MAC_SCL)
    #NET "eeprom_sda"           LOC =     "C1"       |IOSTANDARD =             I2C;     #                      (/Ethernet/MAC_SDA)

    ## DDR3
    # MT41J128M16JT-125:K - 16 Meg x 16 x 8 Banks - DDR3-1600 11-11-11
    # FBGA Code: D9PSL, Part Number: MT41J128M16 - http://www.micron.com/support/fbga
    #NET "mcb3_dram_ck"         LOC =     "K3"       |IOSTANDARD =  DIFF_SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_CK_N | /DDR3/DDR0_CK_P)
    #NET "mcb3_dram_ck"         LOC =     "K4"       |IOSTANDARD =  DIFF_SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_CK_N | /DDR3/DDR0_CK_P)
    ("ddram_clock", 0,
        Subsignal("p", Pins("K4")),
        Subsignal("n", Pins("K3")),
        IOStandard("DIFF_SSTL15_II"), Misc("IN_TERM=NONE")
    ),
    ("ddram", 0,
        ## \/ Strongly pulled (4k) to GND via R7
        #NET "mcb3_dram_cke"        LOC =     "F2"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_CKE)
        Subsignal("cke", Pins("F2"), IOStandard("SSTL15_II")),

        #NET "mcb3_dram_ras_n"      LOC =     "M5"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_RAS_N)
        Subsignal("ras_n", Pins("M5"), IOStandard("SSTL15_II")),
        #NET "mcb3_dram_cas_n"      LOC =     "M4"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_CAS_N)
        Subsignal("cas_n", Pins("M4"), IOStandard("SSTL15_II")),
	#NET "mcb3_dram_we_n"       LOC =     "H2"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_WE_N)
        Subsignal("we_n", Pins("H2"), IOStandard("SSTL15_II")),

        #NET "mcb3_dram_ba<0>"      LOC =     "J3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_BA0)
        #NET "mcb3_dram_ba<1>"      LOC =     "J1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_BA1)
        #NET "mcb3_dram_ba<2>"      LOC =     "H1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_BA2)
        Subsignal("ba", Pins("J3 J1 H1"), IOStandard("SSTL15_II")),

        #NET "mcb3_dram_a<0>"       LOC =     "K2"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A0)
        #NET "mcb3_dram_a<1>"       LOC =     "K1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A1)
        #NET "mcb3_dram_a<2>"       LOC =     "K5"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A2)
        #NET "mcb3_dram_a<3>"       LOC =     "M6"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A3)
        #NET "mcb3_dram_a<4>"       LOC =     "H3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A4)
        #NET "mcb3_dram_a<5>"       LOC =     "M3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A5)
        #NET "mcb3_dram_a<6>"       LOC =     "L4"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A6)
        #NET "mcb3_dram_a<7>"       LOC =     "K6"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A7)
        #NET "mcb3_dram_a<8>"       LOC =     "G3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A8)
        #NET "mcb3_dram_a<9>"       LOC =     "G1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A9)
        #NET "mcb3_dram_a<10>"      LOC =     "J4"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A10)
        #NET "mcb3_dram_a<11>"      LOC =     "E1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A11)
        #NET "mcb3_dram_a<12>"      LOC =     "F1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A12)
        ## \/ Strongly pulled (0.0) to VTTDDR0 via R1
        #NET "mcb3_dram_a<13>"      LOC =     "J6"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A13)
        #NET "mcb3_dram_a<14>"      LOC =     "H5"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_A14)
        Subsignal("a", Pins("K2 K1 K5 M6 H3 M3 L4 K6 G3 G1 J4 E1 F1 J6 H5"), IOStandard("SSTL15_II")),
        #NET "mcb3_dram_dq<0>"      LOC =     "R3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ0)
        #NET "mcb3_dram_dq<1>"      LOC =     "R1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ1)
        #NET "mcb3_dram_dq<10>"     LOC =     "U3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ10)
        #NET "mcb3_dram_dq<11>"     LOC =     "U1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ11)
        #NET "mcb3_dram_dq<12>"     LOC =     "W3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ12)
        #NET "mcb3_dram_dq<13>"     LOC =     "W1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ13)
        #NET "mcb3_dram_dq<14>"     LOC =     "Y2"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ14)
        #NET "mcb3_dram_dq<15>"     LOC =     "Y1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ15)
        #NET "mcb3_dram_dq<2>"      LOC =     "P2"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ2)
        #NET "mcb3_dram_dq<3>"      LOC =     "P1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ3)
        #NET "mcb3_dram_dq<4>"      LOC =     "L3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ4)
        #NET "mcb3_dram_dq<5>"      LOC =     "L1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ5)
        #NET "mcb3_dram_dq<6>"      LOC =     "M2"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ6)
        #NET "mcb3_dram_dq<7>"      LOC =     "M1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ7)
        #NET "mcb3_dram_dq<8>"      LOC =     "T2"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ8)
        #NET "mcb3_dram_dq<9>"      LOC =     "T1"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_DQ9)
        Subsignal("dq", Pins(
                    "R3 R1 U3 U1 W3 W1 Y2 Y1",
                    "P2 P1 L3 L1 M2 M1 T2 T1"), IOStandard("SSTL15_II")),
        # U == Upper, L == Lower
        #NET "mcb3_dram_udqs"       LOC =     "V2"       |IOSTANDARD =  DIFF_SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_UDQS_P)
        #NET "mcb3_dram_udqs_n"     LOC =     "V1"       |IOSTANDARD =  DIFF_SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_UDQS_N)
        #NET "mcb3_dram_ldqs"       LOC =     "N3"       |IOSTANDARD =  DIFF_SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_LDQS_P)
        #NET "mcb3_dram_ldqs_n"     LOC =     "N1"       |IOSTANDARD =  DIFF_SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_LDQS_N)
        Subsignal("dqs", Pins("V2 N3"), IOStandard("DIFF_SSTL15_II")),
        Subsignal("dqs_n", Pins("V1 N1"), IOStandard("DIFF_SSTL15_II")),
        #NET "mcb3_dram_udm"        LOC =     "P3"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_UDM)
        #NET "mcb3_dram_ldm"        LOC =     "N4"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_LDM)
        Subsignal("dm", Pins("P3 N4"), IOStandard("SSTL15_II")),
        #NET "mcb3_dram_odt"        LOC =     "L6"       |IOSTANDARD =       SSTL15_II |OUT_TERM = UNTUNED_50;     #                      (/DDR3/DDR0_ODT)
        Subsignal("odt", Pins("L6"), IOStandard("SSTL15_II"))
    ),

    ## onboard HDMI IN1
    ## HDMI - connector J4 - Direction RX
    ("dvi_in", 0,
        #NET "j4_TMDS(3)"           LOC =    "M20"       |IOSTANDARD =         TMDS_33;     #                  CLK (/HDMI/TMDS-RX1-CLK_P)
        #NET "j4_TMDSB(3)"          LOC =    "M19"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-RX1-CLK_N)
        Subsignal("clk_p", Pins("M20")),
        Subsignal("clk_n", Pins("M19")),
        #NET "j4_TMDS(0)"           LOC =    "J20"       |IOSTANDARD =         TMDS_33;     #                 Blue (/HDMI/TMDS-RX1-0_P)
        #NET "j4_TMDSB(0)"          LOC =    "J22"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-RX1-0_N)
        Subsignal("data0_p", Pins("J20")),
        Subsignal("data0_n", Pins("J22")),
        #NET "j4_TMDS(1)"           LOC =    "H21"       |IOSTANDARD =         TMDS_33;     #                Green (/HDMI/TMDS-RX1-1_P)
        #NET "j4_TMDSB(1)"          LOC =    "H22"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-RX1-1_N)
        Subsignal("data1_p", Pins("B11")),
        Subsignal("data1_n", Pins("A11")),
        #NET "j4_TMDS(2)"           LOC =    "K20"       |IOSTANDARD =         TMDS_33;     #                  Red (/HDMI/TMDS-RX1-2_P)
        #NET "j4_TMDSB(2)"          LOC =    "L19"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-RX1-2_N)
        Subsignal("data2_p", Pins("B12")),
        Subsignal("data2_n", Pins("A12")),
        ## \/ Weakly pulled (47k) to VCC3V3 via R135
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R142
        #NET "hdmi_j4_scl"          LOC =    "L17"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P1-SCL | /HDMI/TMDS-RX1-SCL)
        Subsignal("scl", Pins("L17"), IOStandard("LVCMOS25")),
        ## \/ Weakly pulled (47k) to VCC3V3 via R136
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R141
        #NET "hdmi_j4_sda"          LOC =    "T18"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P1-SDA | /HDMI/TMDS-RX1-SDA)
        Subsignal("sda", Pins("T18"), IOStandard("LVCMOS33")),
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R153
        ## \/ Weakly pulled (15k) to GND via R151
        #NET "hdmi_j4_hpd"          LOC =    "V19"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P1-HOT | /HDMI/TMDS-RX1-HOT)
        Subsignal("hpd_notif", Pins("V19"), IOStandard("LVCMOS33")),
        #Subsignal("hpd_en", Pins("G17"), IOStandard("LVCMOS33")),
        ## \/ Weakly pulled (100k) to VCC3V3 via R132
        ## \/ Weakly pulled (27k) to VCC3V3 via R146
        #NET "hdmi_j4_cec"          LOC =    "K17"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P1-CEC | /HDMI/TMDS-RX1-CEC)
    ),

    ## onboard HDMI IN2
    ## HDMI - connector J5 - Direction RX
    ("dvi_in", 1,
        #NET "j5_TMDS(3)"           LOC =    "L20"       |IOSTANDARD =         TMDS_33;     #                  CLK (/HDMI/TMDS-RX2-CLK_P)
        #NET "j5_TMDSB(3)"          LOC =    "L22"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-RX2-CLK_N)
        Subsignal("clk_p", Pins("L20")),
        Subsignal("clk_n", Pins("L22")),
        #NET "j5_TMDS(0)"           LOC =    "M21"       |IOSTANDARD =         TMDS_33;     #                 Blue (/HDMI/TMDS-RX2-0_P)
        #NET "j5_TMDSB(0)"          LOC =    "M22"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-RX2-0_N)
        Subsignal("data0_p", Pins("M21")),
        Subsignal("data0_n", Pins("M22")),
        #NET "j5_TMDS(1)"           LOC =    "N20"       |IOSTANDARD =         TMDS_33;     #                Green (/HDMI/TMDS-RX2-1_P)
        #NET "j5_TMDSB(1)"          LOC =    "N22"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-RX2-1_N)
        Subsignal("data1_p", Pins("N20")),
        Subsignal("data1_n", Pins("N22")),
        #NET "j5_TMDS(2)"           LOC =    "P21"       |IOSTANDARD =         TMDS_33;     #                  Red (/HDMI/TMDS-RX2-2_P)
        #NET "j5_TMDSB(2)"          LOC =    "P22"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-RX2-2_N)
        Subsignal("data2_p", Pins("P21")),
        Subsignal("data2_n", Pins("P22")),
        ## \/ Weakly pulled (47k) to VCC3V3 via R193
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R197
        #NET "hdmi_j5_scl"          LOC =    "T21"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P3-SCL | /HDMI/TMDS-RX2-SCL)
        Subsignal("scl", Pins("T21"), IOStandard("LVCMOS25")),
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R196
        ## \/ Weakly pulled (47k) to VCC3V3 via R194
        #NET "hdmi_j5_sda"          LOC =    "R22"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P3-SDA | /HDMI/TMDS-RX2-SDA)
        Subsignal("sda", Pins("R22"), IOStandard("LVCMOS25")),
        ## \/ Weakly pulled (15k) to GND via R204
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R205
        #NET "hdmi_j5_hpd"          LOC =    "R20"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P3-HOT | /HDMI/TMDS-RX2-HOT)
        Subsignal("hpd_notif", Pins("R20"), IOStandard("LVCMOS33")),
        #Subsignal("hpd_en", Pins("B20"), IOStandard("LVCMOS33"))
        ## HDMI - connector J5 - Direction RX
        ## \/ Weakly pulled (100k) to VCC3V3 via R192
        ## \/ Weakly pulled (27k) to VCC3V3 via R199
        #NET "hdmi_j5_cec"          LOC =    "T22"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P3-CEC | /HDMI/TMDS-RX2-CEC)
    ),

    ## USB UART Connector
    # To Cypress FX2 UART0
    ("debug", 0, Pins("AA2"), IOStandard("LVCMOS15")), # (/FPGA_Bank_0_3/DEBUG_IO0)

    ("serial", 0,
        # CY_RXD1 - P18 - Cypress RXD0
        Subsignal("tx", Pins("P18"), IOStandard("LVCMOS33")),
        # CY_TXD1 - T17 - Cypress TXD0
        Subsignal("rx", Pins("T17"), IOStandard("LVCMOS33")), 
    ),
    #("serial", 1,
    #    Subsignal("rx", Pins("A16"), IOStandard("LVCMOS33")),
    #    Subsignal("tx", Pins("B16"), IOStandard("LVCMOS33")),
    #),
    # To Cypress FX2 UART1
    #("serial", 2,
    #    Subsignal("rx", Pins("A16"), IOStandard("LVCMOS33")),
    #    Subsignal("tx", Pins("B16"), IOStandard("LVCMOS33")),
    #),

    ## onboard HDMI OUT
    ## HDMI - connector J2 - Direction TX
    ("dvi_out", 0,
        #NET "j2_TMDS(3)"           LOC =    "T12"       |IOSTANDARD =         TMDS_33;     #                  CLK (/HDMI/TMDS-TX2-CLK_P)
        #NET "j2_TMDSB(3)"          LOC =    "U12"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-TX2-CLK_N)
        Subsignal("clk_p", Pins("T12"), IOStandard("TMDS_33")),
        Subsignal("clk_n", Pins("U12"), IOStandard("TMDS_33")),
        #NET "j2_TMDS(2)"           LOC =    "U14"       |IOSTANDARD =         TMDS_33;     #                  Red (/HDMI/TMDS-TX2-2_P)
        #NET "j2_TMDSB(2)"          LOC =    "U13"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-TX2-2_N)
        Subsignal("data2_p", Pins("U14"), IOStandard("TMDS_33")),
        Subsignal("data2_n", Pins("U13"), IOStandard("TMDS_33")),
        #NET "j2_TMDS(1)"           LOC =   "AA16"       |IOSTANDARD =         TMDS_33;     #                Green (/HDMI/TMDS-TX2-1_P)
        #NET "j2_TMDSB(1)"          LOC =   "AB16"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-TX2-1_N)
        Subsignal("data1_p", Pins("AA16"), IOStandard("TMDS_33")),
        Subsignal("data1_n", Pins("AB16"), IOStandard("TMDS_33")),
        #NET "j2_TMDS(0)"           LOC =    "Y15"       |IOSTANDARD =         TMDS_33;     #                 Blue (/HDMI/TMDS-TX2-0_P)
        #NET "j2_TMDSB(0)"          LOC =   "AB15"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-TX2-0_N)
        Subsignal("data0_p", Pins("Y15"), IOStandard("TMDS_33")),
        Subsignal("data0_n", Pins("AB15"), IOStandard("TMDS_33")),
        ## \/ Weakly pulled (47k) to VCC3V3 via R129
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R140
        #NET "hdmi_j2_scl"          LOC =    "Y17"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P4-SCL | /HDMI/TMDS-TX2-SCL)
        Subsignal("scl", Pins("Y17"), IOStandard("LVCMOS33")),
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R138
        ## \/ Weakly pulled (47k) to VCC3V3 via R133
        #NET "hdmi_j2_sda"          LOC =   "AB17"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P4-SDA | /HDMI/TMDS-TX2-SDA)
        Subsignal("sda", Pins("AB17"), IOStandard("LVCMOS33")),
        ## \/ Weakly pulled (15k) to GND via R149
        #NET "hdmi_j2_hpd"          LOC =   "AB18"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P4-HOT | /HDMI/TMDS-TX2-HOT)
        Subsignal("hpd_notif", Pins("AB18"), IOStandard("LVCMOS33")),
        #Subsignal("hpd_en", Pins("B20"), IOStandard("LVCMOS33"))
        ## \/ Weakly pulled (27k) to VCC3V3 via R144
        ## \/ Weakly pulled (100k) to VCC3V3 via R126
        #NET "hdmi_j2_cec"          LOC =   "AA18"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P4-CEC | /HDMI/TMDS-TX2-CEC)
    ),

    ## HDMI - connector J3 - Direction TX
    ("dvi_out", 1,
        #NET "j3_TMDS(3)"           LOC =    "Y11"       |IOSTANDARD =         TMDS_33;     #                  CLK (/HDMI/TMDS-TX1-CLK_P)
        #NET "j3_TMDSB(3)"          LOC =   "AB11"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-TX1-CLK_N)
        Subsignal("clk_p", Pins("Y11"), IOStandard("TMDS_33")),
        Subsignal("clk_n", Pins("AB11"), IOStandard("TMDS_33")),
        #NET "j3_TMDS(0)"           LOC =    "W12"       |IOSTANDARD =         TMDS_33;     #                 Blue (/HDMI/TMDS-TX1-0_P)
        #NET "j3_TMDSB(0)"          LOC =    "Y12"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-TX1-0_N)
        Subsignal("data0_p", Pins("W12"), IOStandard("TMDS_33")),
        Subsignal("data0_n", Pins("Y12"), IOStandard("TMDS_33")),
        #NET "j3_TMDS(1)"           LOC =   "AA10"       |IOSTANDARD =         TMDS_33;     #                Green (/HDMI/TMDS-TX1-1_P)
        #NET "j3_TMDSB(1)"          LOC =   "AB10"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-TX1-1_N)
        Subsignal("data1_p", Pins("AA10"), IOStandard("TMDS_33")),
        Subsignal("data1_n", Pins("AB10"), IOStandard("TMDS_33")),
        #NET "j3_TMDS(2)"           LOC =     "Y9"       |IOSTANDARD =         TMDS_33;     #                  Red (/HDMI/TMDS-TX1-2_P)
        #NET "j3_TMDSB(2)"          LOC =    "AB9"       |IOSTANDARD =         TMDS_33;     #                      (/HDMI/TMDS-TX1-2_N)
        Subsignal("data2_p", Pins("Y9"), IOStandard("TMDS_33")),
        Subsignal("data2_n", Pins("AB9"), IOStandard("TMDS_33")),
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R139
        ## \/ Weakly pulled (47k) to VCC3V3 via R134
        #NET "hdmi_j3_scl"          LOC =     "Y7"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P2-SCL | /HDMI/TMDS-TX1-SCL)
        Subsignal("scl", Pins("Y7"), IOStandard("LVCMOS33")),
        ## \/ Weakly pulled (47k) to VCC3V3 via R130
        ## \/ Strongly pulled (1k) to /HDMI/HDMI_VCC5V0 via R137
        #NET "hdmi_j3_sda"          LOC =    "Y10"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P2-SDA | /HDMI/TMDS-TX1-SDA)
        Subsignal("sda", Pins("Y10"), IOStandard("LVCMOS33")),
        ## \/ Weakly pulled (15k) to GND via R148
        #NET "hdmi_j3_hpd"          LOC =    "AB7"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P2-HOT | /HDMI/TMDS-TX1-HOT)
        Subsignal("hpd_notif", Pins("AB7"), IOStandard("LVCMOS33")),
        #Subsignal("hpd_en", Pins("B20"), IOStandard("LVCMOS33"))
        ## \/ Weakly pulled (27k) to VCC3V3 via R143
        ## \/ Weakly pulled (100k) to VCC3V3 via R127
        #NET "hdmi_j3_cec"          LOC =    "W10"       |IOSTANDARD =        LVCMOS33;     #                      (/HDMI/P2-CEC | /HDMI/TMDS-TX1-CEC)
    ),

#        ("fpga_cfg",
#            Subsignal("din", Pins("T14")),
#            Subsignal("cclk", Pins("R14")),
#            Subsignal("init_b", Pins("T12")),
#            Subsignal("prog_b", Pins("A2")),
#            Subsignal("done", Pins("T15")),
#        ),
#        ("jtag",
#            Subsignal("tms", Pins("B2")),
#            Subsignal("tdo", Pins("B16")),
#            Subsignal("tdi", Pins("B1")),
#            Subsignal("tck", Pins("A15")),
#        ),

]

_connectors = [
]

class Platform(XilinxPlatform):
    default_clk_name = "clk100"
    default_clk_period = 10.0

    def __init__(self, programmer="xc3sprog"):
        # XC6SLX45T-3FGG484C
        XilinxPlatform.__init__(self,  "xc6slx45t-fgg484-3", _io, _connectors)

        pins = {
          'ProgPin': 'PullUp',
          'DonePin': 'PullUp',
          'TckPin': 'PullNone', 
          'TdiPin': 'PullNone',
          'TdoPin': 'PullNone',
          'TmsPin': 'PullNone',
          'UnusedPin': 'PullNone',
          }
        for pin, config in pins.items():
            self.toolchain.bitgen_opt += " -g %s:%s " % (pin, config)

        self.programmer = programmer

        # FPGA AUX is connected to the 3.3V supply
        self.add_platform_command("""CONFIG VCCAUX="3.3";""")

    def create_programmer(self):
        if self.programmer == "xc3sprog":
            return XC3SProg("jtaghs1_fast", "bscan_spi_numato_opsis.bit")
        elif self.programmer == "impact":
            return iMPACT()
        elif self.programmer == "fpgalink":
            from mibuild.fpgalink_programmer import FPGALink
            return FPGALink("1443:0007")
        elif self.programmer == "urjtag":
            return UrJTAG(cable="USBBlaster", pld="spartan-6")
        else:
            raise ValueError("{} programmer is not supported".format(programmer))

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        for i in range(2):
            try:
                self.add_period_constraint(self.lookup_request("dvi_in", i).clk_p, 12)
            except ConstraintError:
                pass

        try:
            self.add_period_constraint(self.lookup_request("eth_clocks").rx, 40.0)
        except ConstraintError:
            pass

        try:
            self.add_period_constraint(self.lookup_request("fx2").ifclk, 20.8)
        except ConstraintError:
            pass


