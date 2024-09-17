# High Level Analyzer
# For more information and documentation, please go to https://support.saleae.com/extensions/high-level-analyzer-extensions

from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting

GT316L_register_map = {
    0x00: "CHIP_ID_REG",
    0x01: "MON_RST_TOUCH_REG",
    0x02: "TOUCH_OUT_1_8_REG",
    0x03: "TOUCH_OUT_9_16_REG",
    0x04: "IO_DIR_1_8_REG",
    0x05: "IO_DIR_9_16_REG",
    0x06: "CONFIGURATION_REG",
    0x07: "EXP_TIME_CONFIG_REG",
    0x08: "TOUCH_PERIOD_CAL_REG",
    0x09: "SEN_IDLE_TIME_SUFFIX_REG",
    0x0A: "SENSING_COUNT_REG",
    0x0B: "BUSY_TO_IDLE_TIME_REG",
    0x0C: "SBF1_SEL",
    0x0D: "SBF2_SEL",
    0x0E: "SBF3_SEL",
    0x0F: "SBF4_SEL",
    0x10: "SENSITIVITY1",
    0x11: "SENSITIVITY2",
    0x12: "SENSITIVITY3",
    0x13: "SENSITIVITY4",
    0x14: "SENSITIVITY5",
    0x15: "SENSITIVITY6",
    0x16: "SENSITIVITY7",
    0x17: "SENSITIVITY8",
    0x18: "SENSITIVITY9",
    0x19: "SENSITIVITY10",
    0x1A: "SENSITIVITY11",
    0x1B: "SENSITIVITY12",
    0x1C: "SENSITIVITY13",
    0x1D: "SENSITIVITY14",
    0x1E: "SENSITIVITY15",
    0x1F: "SENSITIVITY16",
    0x20: "PWM_DATA1",
    0x21: "PWM_DATA2",
    0x22: "PWM_DATA3",
    0x23: "PWM_DATA4",
    0x24: "PWM_DATA5",
    0x25: "PWM_DATA6",
    0x26: "PWM_DATA7",
    0x27: "PWM_DATA8",
    0x28: "PWM_DATA9",
    0x29: "PWM_DATA10",
    0x2A: "PWM_DATA11",
    0x2B: "PWM_DATA12",
    0x2C: "PWM_DATA13",
    0x2D: "PWM_DATA14",
    0x2E: "PWM_DATA15",
    0x2F: "PWM_DATA16",
    0x30: "PWMOUT_DATA1",
    0x31: "PWMOUT_DATA2",
    0x32: "PWMOUT_DATA3",
    0x33: "PWMOUT_DATA4",
    0x34: "PWMOUT_POLARITY_REG"
}

GT316L_register_bitmap = {

    0x00 : {
        0x01: "0",
        0x02: "CHIP_ID_1",
        0x04: "CHIP_ID_2",
        0x08: "CHIP_ID_3",
        0x10: "1",
        0x20: "1",
        0x40: "0",
        0x80: "1"
    },

    0x01 : {
        0x01: "TOUCH",
        0x02: "MON_RST",
        0x04: "0",
        0x08: "0",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0x02 :  {
        0x01: "Keypad 1",
        0x02: "Keypad 2",
        0x04: "Keypad 3",
        0x08: "Keypad 4",
        0x10: "Keypad 5",
        0x20: "Keypad 6",
        0x40: "Keypad 7",
        0x80: "Keypad 8"
    },

    0x03 : {
        0x01: "Keypad 9",
        0x02: "Keypad *",
        0x04: "Keypad 0",
        0x08: "Keypad #",
        0x10: "NA",
        0x20: "NA",
        0x40: "NA",
        0x80: "NA"
    },

    0x04 : {
        0x01: "IO_DIR1",
        0x02: "IO_DIR2",
        0x04: "IO_DIR3",
        0x08: "IO_DIR4",
        0x10: "IO_DIR5",
        0x20: "IO_DIR6",
        0x40: "IO_DIR7",
        0x80: "IO_DIR8"
    },

    0x05 : {
        0x01: "IO_DIR9",
        0x02: "IO_DIR10",
        0x04: "IO_DIR11",
        0x08: "IO_DIR12",
        0x10: "IO_DIR13",
        0x20: "IO_DIR14",
        0x40: "IO_DIR15",
        0x80: "IO_DIR16"
    },

    0x06 : {
        0x01: "SEN_IDLE_TIME_1",
        0x02: "SEN_IDLE_TIME_2",
        0x04: "SEN_IDLE_TIME_3",
        0x08: "SEN_IDLE_TIME_4",
        0x10: "INT_MODE",
        0x20: "PWM_EN",
        0x40: "MULTI_MODE",
        0x80: "SOFT_RESET"
    },

    0x07 :  {
        0x01: "EXP_MODE",
        0x02: "EXP_EN",
        0x04: "EXP_TIME_1",
        0x08: "EXP_TIME_2",
        0x10: "EXP_TIME_3",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0x08 :  {
        0x01: "CAL_TIME_1",
        0x02: "CAL_TIME_2",
        0x04: "CAL_TIME_3",
        0x08: "CAL_TIME_4",
        0x10: "TOUCH_PERIOD_1",
        0x20: "TOUCH_PERIOD_2",
        0x40: "TOUCH_PERIOD_3",
        0x80: "TOUCH_PERIOD_4"
    },

    0x09 :  {
        0x01: "SEN_IDLE_TIME_SUFFIX_1",
        0x02: "SEN_IDLE_TIME_SUFFIX_2",
        0x04: "SEN_IDLE_TIME_SUFFIX_3",
        0x08: "SEN_IDLE_TIME_SUFFIX_4",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0xA :  {
        0x01: "SENSING_COUNT_1",
        0x02: "SENSING_COUNT_2",
        0x04: "SENSING_COUNT_3",
        0x08: "0",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0xB :  {
        0x01: "BUSY_TO_IDLE_TIME_1",
        0x02: "BUSY_TO_IDLE_TIME_2",
        0x04: "BUSY_TO_IDLE_TIME_3",
        0x08: "0",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0xC :  {
        0x01: "SBF1_SEL_1",
        0x02: "SBF1_SEL_2",
        0x04: "SBF1_SEL_3",
        0x08: "0",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0xD :  {
        0x01: "SBF2_SEL_1",
        0x02: "SBF2_SEL_2",
        0x04: "SBF2_SEL_3",
        0x08: "0",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0xE :  {
        0x01: "SBF3_SEL_1",
        0x02: "SBF3_SEL_2",
        0x04: "SBF3_SEL_3",
        0x08: "0",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0xF :  {
        0x01: "SBF4_SEL_1",
        0x02: "SBF4_SEL_2",
        0x04: "SBF4_SEL_3",
        0x08: "0",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    },

    0x34 :  {
        0x01: "PWMOUT_POL_1",
        0x02: "PWMOUT_POL_2",
        0x04: "PWMOUT_POL_3",
        0x08: "PWMOUT_POL_4",
        0x10: "0",
        0x20: "0",
        0x40: "0",
        0x80: "0"
    }
}

def decodeRegister(register, bits_list):
    
    active_bits = bits_list

    def MON_RST_TOUCH_REG(bits):
        
        if "TOUCH" in bits:
            print("Keypad touch detected")
        else: 
            print("No keypad touch detected")

        if "MON_RST" in bits:
            print("Monitoring bit is active")
        else:
            print("Monitoring bit is inactive")
    
    def IO_DIR_1_8_REG(bits):
        
        for i in range(1, 9):
            
            pin_name = f"IO_DIR{i}"
            
            if pin_name in bits:
                print(f"Pin {i} set as analog input")
            else:
                print(f"Pin {i} set as digital output")
    
    def IO_DIR_9_16_REG(bits):
        
        for i in range(9, 17):
            
            pin_name = f"IO_DIR{i}"
            
            if pin_name in bits:
                print(f"Pin {i} set as analog input")
            else:
                print(f"Pin {i} set as digital output")
    
    def CONFIGURATION_REG(active_bits):
        
        sense_idle_time = {
            
            0b0000: "1ms",
            0b0001: "6ms",
            0b0010: "17ms",
            0b0011: "33ms",
            0b0100: "55ms",
            0b0101: "110ms",
            0b0110: "165ms",
            0b0111: "220ms",
            0b1000: "275ms",
            0b1001: "330ms",
            0b1010: "385ms",
            0b1011: "440ms",
            0b1100: "495ms",
            0b1101: "550ms",
            0b1110: "1100ms",
            0b1111: "1650ms"
        }

        if "SOFT_RESET" in active_bits:
            print("GT316L is sleeping")
        else:
            print("GT316L is active")

        if "MULTI_MODE" in active_bits:
            print("Multi touch mode is activated")
        else:
            print("Single touch mode is activated")

        if "PWM_EN" in active_bits:
            print("PWM output is enable")
        else:
            print("PWM output is disable")

        sense_idle_bits = 0b0000

        if "SEN_IDLE_TIME_1" in active_bits:
            updated_sense_idle_time = BitCoder.set_bit(sense_idle_bits, 0)
        elif "SEN_IDLE_TIME_2" in active_bits:
            updated_sense_idle_time = BitCoder.set_bit(sense_idle_bits, 1)
        elif "SEN_IDLE_TIME_3" in active_bits:
            updated_sense_idle_time = BitCoder.set_bit(sense_idle_bits, 2)
        elif "SEN_IDLE_TIME_4" in active_bits:
            updated_sense_idle_time = BitCoder.set_bit(sense_idle_bits, 3)
        
        print("Sense idle time : " , sense_idle_time.get(updated_sense_idle_time))
    
    def EXP_TIME_CONFIG_REG(active_bits):
        
        updated_touch_exp_time = 0

        touch_expire_time = {
            
            0b000: "9sec",
            0b001: "18sec",
            0b010: "27sec",
            0b011: "36sec",
            0b100: "45sec",
            0b101: "54sec",
            0b110: "63sec",
            0b111: "72sec"
        }

        if "EXP_EN" in active_bits:
            print("Touch expire enable")
        else:
            print("Touch expire disable")
        
        if "EXP_MODE" in active_bits:
            print("Touch expire count is restarted")
        else:
            print("Touch expire count is not restarted")

        touch_expire_bits = 0b000

        if "EXP_TIME_1" in active_bits:
            updated_touch_exp_time = BitCoder.set_bit(touch_expire_bits, 0)
        elif "EXP_TIME_2" in active_bits:
            updated_touch_exp_time = BitCoder.set_bit(touch_expire_bits, 1)
        elif "EXP_TIME_3" in active_bits:
            updated_touch_exp_time = BitCoder.set_bit(touch_expire_bits, 2)
        
        
        print("Touch expire time : " , touch_expire_time.get(updated_touch_exp_time))

    def TOUCH_PERIOD_CAL_REG(active_bits):
        
        updated_touch_period = 0
        updated_cal_time = 0

        touch_period = {
            
            0b000: "1period",
            0b001: "2period",
            0b010: "3period",
            0b011: "4period",
            0b100: "5period",
            0b101: "6period",
            0b110: "7period",
            0b111: "8period"
        }

        touch_period_bits = 0b000

        if "TOUCH_PERIOD_1" in active_bits:
            updated_touch_period = BitCoder.set_bit(touch_period_bits, 0)
        elif "TOUCH_PERIOD_2" in active_bits:
            updated_touch_period = BitCoder.set_bit(touch_period_bits, 1)
        elif "TOUCH_PERIOD_3" in active_bits:
            updated_touch_period = BitCoder.set_bit(touch_period_bits, 2)
        
        print("Touch period : " , touch_period.get(updated_touch_period))

        cal_time = {
            
            0b0000: "0ms",
            0b0001: "90ms",
            0b0010: "180ms",
            0b0011: "270ms",
            0b0100: "360ms",
            0b0101: "450ms",
            0b0110: "540ms",
            0b0111: "630ms",
            0b1000: "720ms",
            0b1001: "810ms",
            0b1010: "900ms",
            0b1011: "990ms",
            0b1100: "1080ms",
            0b1101: "1170ms",
            0b1110: "1260ms",
            0b1111: "No Calibration"
        }

        cal_time_bits = 0b0000

        if "CAL_TIME_1" in active_bits:
            updated_cal_time = BitCoder.set_bit(cal_time_bits, 0)
        elif "CAL_TIME_2" in active_bits:
            updated_cal_time = BitCoder.set_bit(cal_time_bits, 1)
        elif "CAL_TIME_3" in active_bits:
            updated_cal_time = BitCoder.set_bit(cal_time_bits, 2)
        elif "CAL_TIME_4" in active_bits:
            updated_cal_time = BitCoder.set_bit(cal_time_bits, 3)
        
        print("Calibration time : " , cal_time.get(updated_cal_time))

    def SEN_IDLE_TIME_SUFFIX_REG(active_bits):
            
        sen_idle_time_suffix = {
            
            0b0000: "0ms",
            0b0001: "3ms",
            0b0010: "6ms",
            0b0011: "11ms",
            0b0100: "17ms",
            0b0101: "22ms",
            0b0110: "28ms",
            0b0111: "33ms",
            0b1000: "39ms",
            0b1001: "44ms",
            0b1010: "50ms",
            0b1011: "55ms",
            0b1100: "110ms",
            0b1101: "220ms",
            0b1110: "330ms",
            0b1111: "440ms"
        }

        sense_idle_time_suffix_bits = 0b0000

        if "SEN_IDLE_TIME_SUFFIX_1" in active_bits:
            updated_sense_idle_time_suffix_bits = BitCoder.set_bit(sense_idle_time_suffix_bits , 0)
        elif "SEN_IDLE_TIME_SUFFIX_2" in active_bits:
            updated_sense_idle_time_suffix_bits = BitCoder.set_bit(sense_idle_time_suffix_bits , 1)
        elif "SEN_IDLE_TIME_SUFFIX_3" in active_bits:
            updated_sense_idle_time_suffix_bits = BitCoder.set_bit(sense_idle_time_suffix_bits , 2)
        elif "SEN_IDLE_TIME_SUFFIX_4" in active_bits:
            updated_sense_idle_time_suffix_bits = BitCoder.set_bit(sense_idle_time_suffix_bits , 3)
        
        print("Sense idle time suffix : " , sen_idle_time_suffix.get(updated_sense_idle_time_suffix_bits))

    def SENSING_COUNT_REG(active_bits):
    
        sensing_count_time = {
            
            0b000: "1000 count",
            0b001: "1500 count",
            0b010: "2000 count",
            0b011: "2500 count",
            0b100: "3000 count",
            0b101: "3500 count",
            0b110: "4000 count",
            0b111: "4500 count"
        }

        sensing_count_time_bits = 0b000

        if "SENSING_COUNT_1" in active_bits:
            updated_sensing_count_time = BitCoder.set_bit(sensing_count_time_bits, 0)
        elif "SENSING_COUNT_2" in active_bits:
            updated_sensing_count_time = BitCoder.set_bit(sensing_count_time_bits, 1)
        elif "SENSING_COUNT_3" in active_bits:
            updated_sensing_count_time = BitCoder.set_bit(sensing_count_time_bits, 2)
        
        
        print("Sensing count : " , sensing_count_time.get(updated_sensing_count_time))

    def BUSY_TO_IDLE_TIME_REG(active_bits):
    
        updated_busy_idle_time = 0

        busy_idle_time = {
            
            0b000: "0.9 sec",
            0b001: "1.8 sec",
            0b010: "2.7 sec",
            0b011: "3.6 sec",
            0b100: "4.5 sec",
            0b101: "5.4 sec",
            0b110: "6.9 sec",
            0b111: "7.2 sec"
        }

        busy_idle_time_bits = 0b000

        if "SENSING_COUNT_1" in active_bits:
            updated_busy_idle_time = BitCoder.set_bit(busy_idle_time_bits, 0)
        elif "SENSING_COUNT_2" in active_bits:
            updated_busy_idle_time = BitCoder.set_bit(busy_idle_time_bits, 1)
        elif "SENSING_COUNT_3" in active_bits:
            updated_busy_idle_time = BitCoder.set_bit(busy_idle_time_bits, 2)
        
        
        print("Busy to idle time : " , busy_idle_time.get(updated_busy_idle_time))

    def SBF1_SEL(active_bits):
        
        sbf_freq = {
            
            0b000: "1 Mhz",
            0b001: "2.4 Mhz",
            0b010: "4 Mhz",
            0b011: "5.6 Mhz",
            0b100: "8.8 Mhz",
            0b101: "10.4 Mhz",
            0b110: "10.4 Mhz",
            0b111: "10.4 Mhz"
        }

        sbf_freq_bits = 0b000

        if "SBF1_SEL_1" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 0)
        elif "SBF1_SEL_2" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 1)
        elif "SBF1_SEL_3" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 2)
          
        print("SBF1 frequency : " , sbf_freq.get(updated_sbf_freq))
    
    def SBF2_SEL(active_bits):
        
        sbf_freq = {
            
            0b000: "1 Mhz",
            0b001: "2.4 Mhz",
            0b010: "4 Mhz",
            0b011: "5.6 Mhz",
            0b100: "8.8 Mhz",
            0b101: "10.4 Mhz",
            0b110: "10.4 Mhz",
            0b111: "10.4 Mhz"
        }

        sbf_freq_bits = 0b000

        if "SBF2_SEL_1" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 0)
        elif "SBF2_SEL_2" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 1)
        elif "SBF2_SEL_3" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 2)
          
        print("SBF2 frequency : " , sbf_freq.get(updated_sbf_freq))
  
    def SBF3_SEL(active_bits):
        
        sbf_freq = {
            
            0b000: "1 Mhz",
            0b001: "2.4 Mhz",
            0b010: "4 Mhz",
            0b011: "5.6 Mhz",
            0b100: "8.8 Mhz",
            0b101: "10.4 Mhz",
            0b110: "10.4 Mhz",
            0b111: "10.4 Mhz"
        }

        sbf_freq_bits = 0b000

        if "SBF3_SEL_1" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 0)
        elif "SBF3_SEL_2" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 1)
        elif "SBF3_SEL_3" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 2)
          
        print("SBF3 frequency : " , sbf_freq.get(updated_sbf_freq))

    def SBF4_SEL(active_bits):
        
        sbf_freq = {
            
            0b000: "1 Mhz",
            0b001: "2.4 Mhz",
            0b010: "4 Mhz",
            0b011: "5.6 Mhz",
            0b100: "8.8 Mhz",
            0b101: "10.4 Mhz",
            0b110: "10.4 Mhz",
            0b111: "10.4 Mhz"
        }

        sbf_freq_bits = 0b000

        if "SBF4_SEL_1" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 0)
        elif "SBF4_SEL_2" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 1)
        elif "SBF4_SEL_3" in active_bits:
            updated_sbf_freq = BitCoder.set_bit(sbf_freq_bits, 2)
          
        print("SBF4 frequency : " , sbf_freq.get(updated_sbf_freq))

    def SENSITIVITY_X(active_bits):
        sensitivity_bits = 0b000000
        sensitivity_percentage = 0
        pin = None 

        for x in range(1, 17):
            for i in range(1, 7):
                pin_identifier = f"SENSITIVITY_{x}_{i}"
                if pin_identifier in active_bits:
                    sensitivity_bits = BitCoder.set_bit(sensitivity_bits, (i - 1))
                    pin = x
                    print(f"Pin {x}_{i} sensitivity is active")

        if sensitivity_bits != 0b000000:
            sensitivity_percentage = int(map_value(sensitivity_bits, 0x03, 0x3F, 100, 0))
            print("Pin ", pin, "Sensitivity Percentage:", sensitivity_percentage, "%")
        else:
            print("No sensitivity flags active")

    def PWM_DATA_X(active_bits):
        pwm_data_bits = 0b00000
        pin = None 

        for x in range(1, 17):
            for i in range(1, 6):
                pin_identifier = f"PWMDATA_{x}_{i}"
                if pin_identifier in active_bits:
                    pwm_data_bits = BitCoder.set_bit(pwm_data_bits, (i - 1))
                    pin = x
                    print(f"Pin {x}_{i} sensitivity is active")

        if pwm_data_bits > 0x00 and pwm_data_bits < 0x1F:
            pwm_percentage = int(map_value(pwm_data_bits, 0x03, 0x3F, 100, 0))
            print("Pin ", pin, "PWM Percentage:", pwm_percentage, "%")
        elif pwm_data_bits == 0x00:
            print("Pin ", pin, "LED is ON")
        elif pwm_data_bits == 0x1F:
            print("Pin ", pin, "LED is OFF")

    def PWMOUT_DATA_X(active_bits):
        pwm_data_bits = 0b00000
        pin = None 

        for x in range(1, 17):
            for i in range(1, 6):
                pin_identifier = f"PWMOUT_{x}_{i}"
                if pin_identifier in active_bits:
                    pwm_data_bits = BitCoder.set_bit(pwm_data_bits, (i - 1))
                    pin = x
                    #print(f"Pin {x}_{i} sensitivity is active")

        if pwm_data_bits > 0x00 and  pwm_data_bits < 0x1F:
            pwm_percentage = int(map_value(pwm_data_bits, 0x03, 0x3F, 100, 0))
            print("Pin PWM OUT", pin, " Percentage:", pwm_percentage, "%")
        elif pwm_data_bits == 0x00:
            print("Pin PWM OUT", pin, "LED is ON")
        elif pwm_data_bits == 0x1F:
            print("Pin PWM OUT", pin, "LED is OFF")

    def PWMOUT_POLARITY_REG(active_bits):

        if "PWMOUT_POL_1" in active_bits:
            print("PIN 1 PWMOUT is active")
        else:
            print("PIN 1 PWMOUT is low")
        
        if "PWMOUT_POL_2" in active_bits:
            print("PIN 2 PWMOUT is active")
        else:
            print("PIN 2 PWMOUT is low")

        if "PWMOUT_POL_3" in active_bits:
            print("PIN 3 PWMOUT is active")
        else:
            print("PIN 3 PWMOUT is low")

        if "PWMOUT_POL_4" in active_bits:
            print("PIN 4 PWMOUT is active")
        else:
            print("PIN 4 PWMOUT is low")


    cases = {
        0x01: MON_RST_TOUCH_REG, 
        0x04: IO_DIR_1_8_REG,
        0x05: IO_DIR_9_16_REG,
        0x06: CONFIGURATION_REG,
        0x07: EXP_TIME_CONFIG_REG,
        0x08: TOUCH_PERIOD_CAL_REG,
        0x09: SEN_IDLE_TIME_SUFFIX_REG,
        0x0A: SENSING_COUNT_REG,
        0x0B: BUSY_TO_IDLE_TIME_REG,
        0x0C: SBF1_SEL,
        0x0D: SBF2_SEL,
        0x0E: SBF3_SEL,
        0x0F: SBF4_SEL,   
        0x10: SENSITIVITY_X,
        0x11: SENSITIVITY_X,
        0x12: SENSITIVITY_X,
        0x13: SENSITIVITY_X,
        0x14: SENSITIVITY_X,
        0x15: SENSITIVITY_X,
        0x16: SENSITIVITY_X,
        0x17: SENSITIVITY_X,
        0x18: SENSITIVITY_X,
        0x19: SENSITIVITY_X,
        0x1A: SENSITIVITY_X,
        0x1B: SENSITIVITY_X,
        0x1C: SENSITIVITY_X,
        0x1D: SENSITIVITY_X,
        0x1E: SENSITIVITY_X,
        0x1F: SENSITIVITY_X,
        0x20: PWM_DATA_X,
        0x21: PWM_DATA_X,
        0x22: PWM_DATA_X,
        0x23: PWM_DATA_X,
        0x24: PWM_DATA_X,
        0x25: PWM_DATA_X,
        0x26: PWM_DATA_X,
        0x27: PWM_DATA_X,
        0x28: PWM_DATA_X,
        0x29: PWM_DATA_X,
        0x2A: PWM_DATA_X,
        0x2B: PWM_DATA_X,
        0x2C: PWM_DATA_X,
        0x2D: PWM_DATA_X,
        0x2E: PWM_DATA_X,
        0x2F: PWM_DATA_X,
        0x30: PWMOUT_DATA_X,
        0x31: PWMOUT_DATA_X,
        0x32: PWMOUT_DATA_X,
        0x33: PWMOUT_DATA_X,
        0x34: PWMOUT_POLARITY_REG
        
    }

    case_number = register
    
    result = cases.get(case_number, lambda bits: f"Default case with argument {bits}")(active_bits) 

    print (result)
        
def decodeBits(register, value, register_map):
    # List to store active bits
    active_bits = []
    buf = register_map[register]

    # Check each bit against the register_bit_mask
    for mask, description in buf.items():
        if value & mask:
            active_bits.append(description)
    """
    # Print the active bits
    if active_bits:
        print(f"Active bits in {hex(register)} register:")
        for bit in active_bits:
            print(bit)
    else:
        print(f"No active bits in {hex(register)} register")
    """

    return active_bits

def generate_inner_dict(sensitivity_prefix, num_bits):
    inner_dict = {}
    for i in range(1, num_bits + 1):
        key = 1 << (i - 1)  # Calculate the key based on the bit position
        value = f"{sensitivity_prefix}_{i}"
        inner_dict[key] = value
    return inner_dict

def generate_bits_register_map(bit_prefix, num_bits_in_reg, num_of_reg, start_reg, register_map):
    for i in range(1, num_of_reg + 1):  # Include the last register
        register_prefix = f"{bit_prefix}_{i}"  # Append the register number to the prefix
        register_map[start_reg + i - 1] = generate_inner_dict(register_prefix, num_bits_in_reg)

    # Optionally, you can return the resulting register_map
    return register_map

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


prefix = "SENSITIVITY"
num_bits_in_register = 6
num_of_registers = 16

GT316L_register_bitmap = generate_bits_register_map(prefix, num_bits_in_register, num_of_registers, 0x10 ,GT316L_register_bitmap)

prefix = "PWMDATA"
num_bits_in_register = 5
num_of_registers = 16

GT316L_register_bitmap = generate_bits_register_map(prefix, num_bits_in_register, num_of_registers, 0x20 ,GT316L_register_bitmap)

prefix = "PWMOUT"
num_bits_in_register = 5
num_of_registers = 4

GT316L_register_bitmap = generate_bits_register_map(prefix, num_bits_in_register, num_of_registers, 0x30 ,GT316L_register_bitmap)

class BitCoder:
    @staticmethod
    def set_bit(value, bit_position):
        """
        Set the bit at the specified position to 1.
        
        Args:
            value (int): The original value.
            bit_position (int): The position of the bit to set (0-based).
        
        Returns:
            int: The updated value with the specified bit set.
        """
        return value | (1 << bit_position)

    @staticmethod
    def clear_bit(value, bit_position):
        """
        Clear the bit at the specified position to 0.
        
        Args:
            value (int): The original value.
            bit_position (int): The position of the bit to clear (0-based).
        
        Returns:
            int: The updated value with the specified bit cleared.
        """
        return value & ~(1 << bit_position)

    @staticmethod
    def toggle_bit(value, bit_position):
        """
        Toggle (invert) the bit at the specified position.
        
        Args:
            value (int): The original value.
            bit_position (int): The position of the bit to toggle (0-based).
        
        Returns:
            int: The updated value with the specified bit toggled.
        """
        return value ^ (1 << bit_position)

    @staticmethod
    def get_bit(value, bit_position):
        """
        Get the value of the bit at the specified position.
        
        Args:
            value (int): The original value.
            bit_position (int): The position of the bit to retrieve (0-based).
        
        Returns:
            int: The value of the specified bit (0 or 1).
        """
        return (value >> bit_position) & 1
    
class Transaction:
    is_multibyte_read: bool
    is_read: bool
    start_time: float
    end_time: float
    address: int
    register_ptr: int
    data: bytearray

    def __init__(self, start_time):
        self.start_time = start_time
        self.data = bytearray()
        self.is_multibyte_read = False
        self.register_ptr = 0x00
    
# High level analyzers must subclass the HighLevelAnalyzer class.
class Hla(HighLevelAnalyzer):

    # An optional list of types this analyzer produces, providing a way to customize the way frames are displayed in Logic 2.
    result_types = {
            'error': {
                'format': 'Error!'
            },
            "i2c_w": {
                #'format': 'Device: {{data.address}} | OP : {{data.direction}} | Register[{{data.register}}] | Data[{{data.count}}]: [ {{data.data}} ]'
                'format': 'Device: {{data.address}} | OP : {{data.direction}} | Register[{{data.register}}] ({{data.hex_register}}) | [ {{data.data}} ]'
            }
        }
        
    
    temp_frame = None
   
    
  

    def __init__(self):
        '''
        Initialize HLA.

        Settings can be accessed using the same name used above.
        '''
        self.temp_frame = None

        self.i2c_w_start_time = None
        self.i2c_w_stop_time = None
        self.i2c_address = None
        self.current_transaction = None

    def decode(self, frame: AnalyzerFrame):
        '''
        Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame` or a list of `AnalyzerFrame`s.

        The type and data values in `frame` will depend on the input analyzer.
        '''
        # set our frame to an error frame, which will eventually get over-written as we get data.

        new_frame = None

        if self.temp_frame is None:
            self.current_transaction = Transaction(frame.start_time)

            self.temp_frame = AnalyzerFrame("i2c_w", frame.start_time, frame.end_time, {
                "address": "",
                "direction": "",
                "register": "",
                "hex_register": "",
                "data": "",
                "count": 0
            }
            )


        
        # If start condition is detected
        if frame.type == 'start':
            # Initialize a new transaction object
            #self.current_transaction = Transaction(frame.start_time)
            
            """
            if frame.type == 'address' and frame.data['read'] == True:
                # Start a new transaction   
                self.temp_frame.start_time = frame.start_time
            """

                

        # Else if stop condition is detected  
        elif frame.type == 'stop':
            # End the frame
            self.temp_frame.end_time = frame.end_time
            
            # New Transaction 
            transaction = self.current_transaction
            # Mirror copy 
            transaction.end_time = frame.end_time
            
            

            # Flush state machine variables 
            self.current_transaction = None
            new_frame = self.temp_frame
            self.temp_frame = None
        
        # This block of code is executed when a transaction has been captured [Start Time] ----> [End Time]
        if self.current_transaction is not None:
            
            address_byte = None
    
            # HLA I2C API returned an address block
            if frame.type == 'address':
                
                # Check which kind of operation was executed
                self.direction = "Read" if frame.data['read'] else "Write in"
                self.temp_frame.data["direction"] = self.direction
                
                # Mirror copy 
                self.current_transaction.is_read = True if frame.data['read'] else False

                address_byte = frame.data["address"][0]
                
                # Mirror copy 
                self.current_transaction.address = address_byte

                # Check if the address match our device
                #  [TO DO] Make it as an user setting
                if address_byte == 0x59:
                    #self.temp_frame.data["address"] = hex(address_byte)
                    self.temp_frame.data["address"] = "GT316L"
                else:
                    self.temp_frame.data["address"] = "Unknow"
            
            # HLA I2C API returned data blocks
            elif frame.type == 'data':
                
                # Get the data
                data_byte = frame.data["data"][0]
                
                # Increase the counter
                self.temp_frame.data["count"] += 1

                # Get the register address, usually the first byte of a sequence
                if self.temp_frame.data["count"] == 1 and self.temp_frame.data["address"] == "GT316L":
                    
                    self.current_transaction.register_ptr = data_byte

                    # Get the associated register name 
                    register_name = GT316L_register_map.get(self.current_transaction.register_ptr)
                    
                    # Set the register name in the analyzer frame
                    self.temp_frame.data["register"] = str(register_name)
                    self.temp_frame.data["hex_register"] = hex(self.current_transaction.register_ptr)

                    self.current_transaction.is_multibyte_read = False

                else: 

                    if len(self.temp_frame.data["data"]) > 2:
                        # Add separator
                        self.temp_frame.data["data"] += ", "

                        # If received more than 2 bytes, indicate that we have a multibyte sequence 
                        self.current_transaction.is_multibyte_read = True
                    
                    # Set the byte value in the analyzer frame 
                    self.temp_frame.data["data"] += hex(data_byte)

                # Mirror copy 
                self.current_transaction.data.append(data_byte)
        
        if new_frame is not None:
            
            print ( new_frame.data["address"], 
                    new_frame.data["direction"],
                    new_frame.data["register"],
                    f"({new_frame.data['hex_register']})",
                    #new_frame.data["count"],
                    new_frame.data["data"]   
            )

            # [TO DO] Decode transaction here
            self.decode_transaction(transaction)
            print ("---")

            return new_frame

    def decode_transaction(self, transaction):
        
        # Initialize an empty bytearray for the data to decode
        data_to_decode = bytearray()

        # Check if the transaction contains at least 2 bytes of data and is at destination of GT316L
        if len(transaction.data) > 1 and transaction.address == 0x59:
            
            # Get the register ptr
            reg_ptr = transaction.register_ptr
           
            # Throw away the first byte of the transaction which is usually the register ptr 
            data_to_decode = transaction.data[1:]
            
            for data in data_to_decode:
                
                # Get the active bits for register 
                # bits = decodeBits(reg_ptr, data, GT316L_register_bitmap)
                decodeRegister(reg_ptr, decodeBits(reg_ptr, data, GT316L_register_bitmap))

                # Virtiually increase register pointer address
                reg_ptr += 1



               
            
            

                
