def adc_to_v(adc_arr):
    v_arr = []
    for adc in adc_arr:
        v = round(1.1896972296199237e-010 + 1.2207031249858410e-003 * adc, 1)
        v_arr.append(v)
    print(v_arr)

def v_to_adc(v_arr):
    adc_arr = []
    for v in v_arr:
        adc = int(-9.7482370620127767e-008 + 8.1920000000950949e+002 * v)
        adc_arr.append(adc)
    print(adc_arr)

v_arr = [0, 1, 2.5, 3, 4, 5]
v_to_adc(v_arr)
adc_arr = [0, 819, 2047, 2457, 3276, 4095]
adc_to_v(adc_arr)