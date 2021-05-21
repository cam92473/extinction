# Calculate mean extinction curve from parameters in Parameters.py
# The curve is a piecewise function composed of an IR region, an optical region and two UV regions

import matplotlib.pyplot as plt
import numpy as np
from extinction.GUI.GUI import ir_shrtst, opt_shrtst, c5, createoutput, scatter, fullplot
import extinction.model_calcs.functions as f

# -----------
# Read in data and convert to microns
# ------------

indata_nm = np.genfromtxt("/wavelengths.csv")

# -----------
# Evaluate wavelengths based on what range (IR, Opt, UV>c5, UV>=c5) they lie in
# ------------

y_vals=[]

for wvlngth in indata_nm:
    if wvlngth > ir_shrtst:
        y_vals.append(f.ir_model(1000 / wvlngth))
    elif wvlngth <= ir_shrtst and wvlngth > opt_shrtst:
        y_vals.append(f.opt_model(1000 / wvlngth))
    elif wvlngth <= opt_shrtst and wvlngth > 1000/c5:
        y_vals.append(f.uv_lng_model(1000 / wvlngth))
    elif wvlngth <= 1000/c5:
        y_vals.append(f.uv_srt_model(1000 / wvlngth))

# ----------
# Plot the results and export the y values to a .csv file created in the same directory
# ----------

x_axis = (1000/indata_nm)
y_axis = np.array(y_vals)
grapharray_unsrt = np.column_stack((x_axis,y_axis))
grapharray_xsrt = grapharray_unsrt[np.argsort(grapharray_unsrt[:, 0])]

if createoutput == 1:
    np.savetxt("/output.csv",y_axis)

if scatter == 1:
    plt.scatter(grapharray_xsrt[:,0],grapharray_xsrt[:,1])
    plt.show()

if fullplot == 1:

    xfin = np.linspace(0, 8, 1000)

    yfin = np.piecewise(xfin, [xfin < 1000/ir_shrtst, xfin >= 1000/ir_shrtst, xfin >= 1000/opt_shrtst, xfin >= c5],
                        [lambda xfin: f.ir_model(xfin),
                         lambda xfin: f.opt_model(xfin),
                         lambda xfin: f.uv_lng_model(xfin),
                         lambda xfin: f.uv_srt_model(xfin)])

    fig, ax = plt.subplots()

    plt.rcParams['figure.figsize'] = [12, 8]
    plt.xlabel(r"1000/(wavelength in nm) [μm$^-$$^1$]")
    plt.ylabel("E(λ-V) / E(B-V)")
    # plt.style.use("dark_background")
    plt.plot(xfin, yfin, color="blue")

    plt.show()
